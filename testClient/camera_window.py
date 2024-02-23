import queue
import threading

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox, QGraphicsScene
import cv2
import socket
import time

from contactus import ContactUsDialog
from help import HelpDialog

# 服务端ip地址
HOST = '127.0.0.1'
# 服务端端口号
PORT = 8080
ADDRESS = (HOST, PORT)

class CameraWindow(QtWidgets.QMainWindow):
    back_to_main_signal = QtCore.pyqtSignal()

    def __init__(self,client_socket, main_window):
        super().__init__()
        uic.loadUi('UserClient\mainwindow.ui', self)

        try:
            with open(r"UserClient\res\qss\style.qss", "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Error loading stylesheet in CameraWindow: {e}")

        self.client_socket = client_socket
        self.main_window = main_window

        self.returnButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.returnButton.clicked.connect(self.backAction)

        self.helpAction = self.findChild(QtWidgets.QAction, 'actionhelp')
        self.helpAction.triggered.connect(self.helpActionTriggered)
        self.contactAction = self.findChild(QtWidgets.QAction, 'actioncontact_us')
        self.contactAction.triggered.connect(self.contactActionTriggered)

        self.graphicsView = self.findChild(QtWidgets.QGraphicsView, 'graphicsView')
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

        self.consoleTextEdit = self.findChild(QtWidgets.QTextEdit,'textEdit')
        self.consoleTextEdit.setReadOnly(True)

        self.cameraCheckBox = self.findChild(QtWidgets.QCheckBox, 'Camera')


        self.cap = cv2.VideoCapture(0)
        self.timer_show = QTimer(self)
        self.timer_show.timeout.connect(self.display_frame)
        self.timer_show.start(20)  # 更新间隔，20ms,50fps

        self.frame_queue = queue.Queue(maxsize=5)  # 队列存储待传输的帧
        self.timer_send = QTimer(self)  # 处理队列中的图像帧
        self.timer_send.timeout.connect(self.send_frame)  # 将定时器的timeout信号连接到send_frame函数
        self.timer_send.start(20)

        self.back_to_main_signal.connect(main_window.show)
        #threading.Thread(target=self.listen_server_messages, daemon=True).start()#aia

    def append_to_console(self,message):
        self.consoleTextEdit.append(message)

    def backAction(self):
        print("back action")

        if self.timer_show.isActive():
            self.timer_show.stop()

        if self.timer_send.isActive():
            self.timer_send.stop()

        if self.cap.isOpened():
            self.cap.release()

        self.back_to_main_signal.emit()
        self.close()


    def display_frame(self):
        # 显示摄像头捕获的图像帧
        try:
            ret, frame = self.cap.read()
            if ret:
                self.process_frame(frame)  # 处理和显示图像帧
        except Exception as e:
            self.append_to_console("error in reading camera"+str(e))

    def process_frame(self, frame):
        # 显示图像帧的函数
        try:
            # 显示图像的代码
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(convert_to_Qt_format)
            self.scene.clear()  # 确保场景被清除
            self.scene.addPixmap(pixmap)
            self.graphicsView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        except Exception as e:
            self.append_to_console("error in processing and showing frame"+str(e))
        if self.frame_queue.full():
            self.frame_queue.get()
        self.frame_queue.put(frame)

    def send_frame(self):
        # 处理队列中的图像帧并发送
        if not self.frame_queue.empty():
            frame = self.frame_queue.get()  # 从队列中获取一个图像帧
            try:
                img_encode = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])[1] #压缩
                byte_data = img_encode.tobytes() #转成字节流
                length = len(byte_data)
                self.client_socket.sendall(str(length).encode() + b'\n')
                self.client_socket.sendall(byte_data)
            except Exception as e:
                self.append_to_console("error in packing and sending"+str(e))



    def closeCameraAndTCPConnection(self):
        # 关闭摄像头的代码
        print("Closing camera and TCP connection")
        self.timer_show.stop()
        self.timer_send.stop()
        self.cap.release()
        print("release camera")
        try:
            self.client_socket.close()
        except Exception as e:
            self.append_to_console("error in closing connection " + str(e))


    def closeEvent(self, event):#重写关闭窗口函数，清理资源
        self.cleanup_resources()
        event.accept()

    def cleanup_resources(self):
        print("Cleaning up resources")
        if self.timer_show.isActive():
            self.timer_show.stop()
        if self.timer_send.isActive():
            self.timer_send.stop()
        if self.cap.isOpened():
            self.cap.release()
        self.client_socket.send("close\n".encode())
        print("Resources cleaned up")


    """
    处理服务器发送过来的内容的一些函数：
    """
    def listen_server_messages(self):
        while True:
            try:
                server_message = self.client_socket.recv(1024).decode()
                if server_message == "disconnect":
                    print("Received disconnect from server")
                    self.backAction()
                    break
                else:
                    print("其他消息")
                    self.append_to_console(server_message)
            except Exception as e:
                print("Error in receiving message from server: " + str(e))
                break





    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()

    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()