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

        # Ensure the folder for recording exists
        record_path = os.path.join(QCoreApplication.applicationDirPath(), "record")
        os.makedirs(record_path, exist_ok=True)

        print("file path end")


        self.client_socket = client_socket
        self.main_window = main_window

        self.server_host = server_host
        self.server_port = server_port

        self.is_recording = False
        self.video_writer = None
        print("initial camera window end")

        # buttons, actions init
        self.shotButton.clicked.connect(self.takeScreenshot)
        #self.shotButton.clicked.connect(self.back_action)

        self.recordButton.setStyleSheet("border-image: url(:/res/pic/record.png);")
        self.recordButton.clicked.connect(self.toggleRecording)
        #print("2 button loading end")

        self.btn_1.clicked.connect(self.changeStyleToStarrySky)
        self.btn_2.clicked.connect(self.changeStyleToSea)
        self.btn_3.clicked.connect(self.changeStyleToDesert)
        self.btn_4.clicked.connect(self.changeStyleToGrassland)

        self.actionhelp.triggered.connect(self.helpActionTriggered)
        self.actioncontact_us.triggered.connect(self.contactActionTriggered)
        self.actionOpen_record_folder = self.findChild(QtWidgets.QAction, 'actionOpen_record_folder')
        self.actionOpen_record_folder.triggered.connect(self.openRecordFolder)
        #print("3 action loading end")

        self.graphicsView = self.findChild(QtWidgets.QGraphicsView, 'graphicsView')
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        print("graphview loading end")


        self.textEdit.setReadOnly(True)

        self.host, self.port = read_server_address()

        self.cameraCheckBox = self.findChild(QtWidgets.QCheckBox, 'Camera')

        self.cap = cv2.VideoCapture(0)
        self.timer_show = QTimer(self)
        self.timer_show.timeout.connect(self.display_frame)
        self.timer_show.start(50)  # update frequence
        print("cap&timer1 loading end")

        self.frame_queue = queue.Queue(maxsize=1)  # queue storing the frame to be sent
        self.timer_send = QTimer(self)
        self.timer_send.timeout.connect(self.send_frame)
        self.timer_send.start(50)
        print("timer2 loading end")

        self.back_to_main_signal.connect(main_window.show)
        threading.Thread(target=self.listen_server_messages, daemon=True).start()#aia



    # change style methods: 5
    def applyStyleSheet(self, styleSheetPath):
        try:
            with open(styleSheetPath, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet: {e}")

    def changeStyleToStarrySky(self):
        self.applyStyleSheet(r"cameraWindow\res\qss\style.qss")

    def changeStyleToSea(self):
        self.applyStyleSheet(r"cameraWindow\res\qss\style1.qss")

    def changeStyleToDesert(self):
        self.applyStyleSheet(r"cameraWindow\res\qss\style2.qss")

    def changeStyleToGrassland(self):
        self.applyStyleSheet(r"cameraWindow\res\qss\style3.qss")


    def openRecordFolder(self):
        record_path = os.path.join(QCoreApplication.applicationDirPath(), "record")
        # check OS
        if os.name == 'nt':  # Windows
            os.startfile(record_path)
        elif os.name == 'posix':  # macOS和Linux
            try:
                #macos
                os.system(f'open "{record_path}"')
            except:
                #linux
                os.system(f'xdg-open "{record_path}"')

    # take screen shot triggered by shotButton
    def takeScreenshot(self):
        record_path = os.path.join(QCoreApplication.applicationDirPath(), "record")
        screenshot_filename = os.path.join(QCoreApplication.applicationDirPath(), "record",
                                           "screenshot-{}.png".format(time.strftime("%Y%m%d-%H%M%S")))
        screenshot = self.grab()
        # 保存截图
        screenshot.save(screenshot_filename, 'PNG')
        self.append_to_console(f"ScreenShot in{record_path}")

    # take recording and change the image of record button
    def toggleRecording(self):
        if self.is_recording:
            # stop recording
            self.is_recording = False
            self.recordButton.setStyleSheet("border-image: url(:/res/pic/record.png);")
            # self.recordButton.setText("Record")
            if self.video_writer:
                self.video_writer.release()
                self.video_writer = None
            self.append_to_console("Recording finished")
        else:
            # begin recording
            self.is_recording = True
            self.recordButton.setStyleSheet("border-image: url(:/res/pic/recording.png);")
            # self.recordButton.setText("Stop")
            filename = os.path.join(QCoreApplication.applicationDirPath(), "record",
                                    "recorded-{}.avi".format(time.strftime("%Y%m%d-%H%M%S")))
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.video_writer = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
            self.append_to_console("Recording started")
    def append_to_console(self,message):
        self.textEdit.append(message)

    #本方法因为存在bug废弃
    #this method abandoned because of existence of bugs
    def back_action(self):
        print("back action")
        self.append_to_console("back action")

        self.cleanup_resources()

        self.back_to_main_signal.emit()
        self.close()


    def display_frame(self):
        # show the frames caught by camera
        try:
            ret, frame = self.cap.read()
            if ret:
                self.process_frame(frame)  # process and show main method
        except Exception as e:
            self.append_to_console("error in reading camera"+str(e))

    # process and show frames
    def process_frame(self, frame):
        try:
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

        # if is recording then also record
        if self.is_recording and self.video_writer is not None:
            self.video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    # Method sending frames to server
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


    #this method abandoned
    def closeCameraAndTCPConnection(self):
        # close camera
        print("Closing camera and TCP connection")
        self.timer_show.stop()
        self.timer_send.stop()
        self.cap.release()
        print("release camera")
        try:
            self.client_socket.close()
        except Exception as e:
            self.append_to_console("error in closing connection " + str(e))


    # Overload the close
    def closeEvent(self, event):#重写关闭窗口函数，清理资源
        self.cleanup_resources()
        self.client_socket.send("close".encode())
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
        """clear socket data in buffer"""
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
    listen to server, handling the messages from server
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
                    #此处添加表情逻辑
                    print("其他消息")
                    self.append_to_console(server_message)
                    print(server_message)
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