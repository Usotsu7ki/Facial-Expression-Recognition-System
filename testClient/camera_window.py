import os
import queue
import threading

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QTimer, Qt, QCoreApplication
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox, QGraphicsScene
import cv2
import socket
import time

from contactus import ContactUsDialog
from help import HelpDialog

def read_server_address():
    with open("address.txt", "r") as file:
        lines = file.readlines()
        host = lines[0].strip()
        port = int(lines[1].strip())
    return host, port

class CameraWindow(QtWidgets.QMainWindow):
    back_to_main_signal = QtCore.pyqtSignal()

    def __init__(self,client_socket, main_window,server_host,server_port):
        super().__init__()
        uic.loadUi('cameraWindow\mainwindow.ui', self)

        try:
            with open(r"cameraWindow\res\qss\style.qss", "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Error loading stylesheet in CameraWindow: {e}")

        #确保保存视频的record文件夹存在
        record_path = os.path.join(QCoreApplication.applicationDirPath(), "record")
        os.makedirs(record_path, exist_ok=True)

        self.client_socket = client_socket
        self.main_window = main_window

        self.server_host = server_host
        self.server_port = server_port

        self.returnButton = self.findChild(QtWidgets.QPushButton, 'returnButton')
        self.returnButton.clicked.connect(self.back_action)

        self.recordButton = self.findChild(QtWidgets.QPushButton, 'recordButton')
        self.recordButton.clicked.connect(self.toggleRecording)
        print("2 button loading end")

        self.helpAction = self.findChild(QtWidgets.QAction, 'actionhelp')
        self.helpAction.triggered.connect(self.helpActionTriggered)
        self.contactAction = self.findChild(QtWidgets.QAction, 'actioncontact_us')
        self.contactAction.triggered.connect(self.contactActionTriggered)
        self.actionOpen_record_folder = self.findChild(QtWidgets.QAction, 'actionOpen_record_folder')
        self.actionOpen_record_folder.triggered.connect(self.openRecordFolder)
        print("3 action loading end")

        self.graphicsView = self.findChild(QtWidgets.QGraphicsView, 'graphicsView')
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        print("graphview loading end")

        self.consoleTextEdit = self.findChild(QtWidgets.QTextEdit,'textEdit')
        self.consoleTextEdit.setReadOnly(True)

        self.host, self.port = read_server_address()

        self.cameraCheckBox = self.findChild(QtWidgets.QCheckBox, 'Camera')

        self.cap = cv2.VideoCapture(0)
        self.timer_show = QTimer(self)
        self.timer_show.timeout.connect(self.display_frame)
        self.timer_show.start(20)  # 更新间隔，20ms,50fps
        print("cap&timer1 loading end")

        self.frame_queue = queue.Queue(maxsize=5)  # 队列存储待传输的帧
        self.timer_send = QTimer(self)  # 处理队列中的图像帧
        self.timer_send.timeout.connect(self.send_frame)  # 将定时器的timeout信号连接到send_frame函数
        self.timer_send.start(20)
        print("timer2 loading end")

        self.back_to_main_signal.connect(main_window.show)
        threading.Thread(target=self.listen_server_messages, daemon=True).start()#aia

        self.is_recording = False
        self.video_writer = None
        print("initial camera window end")

    def openRecordFolder(self):
        record_path = os.path.join(QCoreApplication.applicationDirPath(), "record")
        # 检查操作系统平台
        if os.name == 'nt':  # 对于Windows
            os.startfile(record_path)
        elif os.name == 'posix':  # 对于macOS和Linux
            try:
                # 尝试macOS的打开方式
                os.system(f'open "{record_path}"')
            except:
                # 默认使用Linux的打开方式
                os.system(f'xdg-open "{record_path}"')

    def toggleRecording(self):
        if self.is_recording:
            # 停止录制
            self.is_recording = False
            self.recordButton.setText("Record")
            if self.video_writer:
                self.video_writer.release()
                self.video_writer = None
            self.append_to_console("Recording finished")
        else:
            # 开始录制
            self.is_recording = True
            self.recordButton.setText("Stop")
            filename = os.path.join(QCoreApplication.applicationDirPath(), "record",
                                    "recorded-{}.avi".format(time.strftime("%Y%m%d-%H%M%S")))
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.video_writer = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
            self.append_to_console("Recording started")
    def append_to_console(self,message):
        self.consoleTextEdit.append(message)

    def back_action(self):
        print("back action")
        self.append_to_console("back action")

        self.cleanup_resources()

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

        #如果在录制也开始写入视频文件
        if self.is_recording and self.video_writer is not None:
            self.video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

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


    #废弃不用了
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
        self.client_socket.send("close\n".encode())
        event.accept()

    def cleanup_resources(self):
        print("Cleaning up resources")
        if self.is_recording:
            self.toggleRecording()  # 停止录制并保存

        if self.timer_show.isActive():
            self.timer_show.stop()

        if self.timer_send.isActive():
            self.timer_send.stop()

        if self.cap.isOpened():
            self.cap.release()

        #self.client_socket.close()
        #self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client_socket.connect((self.server_host, self.server_port))
        self.clear_socket_buffer()
        print("Resources cleaned up")

    def clear_socket_buffer(self):
        """清除在socket缓冲区中可能残留的数据。"""
        self.client_socket.setblocking(False)
        try:
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break  # 没有更多的数据
        except BlockingIOError:
            pass
        finally:
            self.client_socket.setblocking(True)


    """
    处理服务器发送过来的内容的一些函数：
    """
    def listen_server_messages(self):
        while True:
            try:
                server_message = self.client_socket.recv(1024).decode()
                if server_message == "disconnect":
                    print("Received disconnect from server")
                    self.back_action()
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