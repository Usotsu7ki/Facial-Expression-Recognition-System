import os
import queue
import threading

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QTimer, Qt, QCoreApplication
from PyQt5.QtGui import QImage, QPixmap, QColor, QPen, QFont
from PyQt5.QtWidgets import QMessageBox, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem
import cv2
import socket
import time

from contactus import ContactUsDialog
import global_settings
from help import HelpDialog


def read_server_address():
    with open("address.txt", "r") as file:
        lines = file.readlines()
        host = lines[0].strip()
        port = int(lines[1].strip())
    return host, port


class CameraWindow(QtWidgets.QMainWindow):
    # back_to_main_signal = QtCore.pyqtSignal()
    update_graphics_signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super().__init__()

        self.x = 0
        self.h = 0
        self.w = 0
        self.y = 0
        self.probability = 0
        self.emotion = "Neural"

        uic.loadUi('cameraWindow\mainwindow.ui', self)
        try:
            with open(global_settings.camera_style_path, "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Error loading stylesheet in CameraWindow: {e}")

        # Ensure the folder for recording exists
        record_path = os.path.join(QCoreApplication.applicationDirPath(), "record")
        os.makedirs(record_path, exist_ok=True)
        print("file path end")

        # socket, from login
        self.client_socket = client_socket

        # recording flags
        self.is_recording = False
        self.video_writer = None
        print("initial camera window end")

        # buttons, actions init
        self.shotButton.clicked.connect(self.takeScreenshot)
        # self.shotButton.clicked.connect(self.back_action)

        self.recordButton.setStyleSheet("border-image: url(:/res/pic/record.png);")
        self.recordButton.clicked.connect(self.toggleRecording)
        # print("2 button loading end")

        self.actionstarry_sky.triggered.connect(self.changeStyleToStarrySky)
        self.actionsea.triggered.connect(self.changeStyleToSea)
        self.actiondesert.triggered.connect(self.changeStyleToDesert)
        self.actiongrassland.triggered.connect(self.changeStyleToGrassland)

        self.actionhelp.triggered.connect(self.helpActionTriggered)
        self.actioncontact_us.triggered.connect(self.contactActionTriggered)
        self.actionOpen_record_folder = self.findChild(QtWidgets.QAction, 'actionOpen_record_folder')
        self.actionOpen_record_folder.triggered.connect(self.openRecordFolder)
        # print("3 action loading end")

        self.graphicsView = self.findChild(QtWidgets.QGraphicsView, 'graphicsView')
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        print("graphview and scene setting end")

        self.is_running = True  # control the thread running
        self.last_ok_received = time.time()  # this used to keep sending and receiving normal

        self.textEdit.setReadOnly(True)

        self.host, self.port = read_server_address()

        self.cameraCheckBox = self.findChild(QtWidgets.QCheckBox, 'Camera')

        self.cap = cv2.VideoCapture(0)
        self.timer_show = QTimer(self)
        self.timer_show.timeout.connect(self.display_frame)
        self.timer_show.start(50)  # update frequence
        print("cap&timer1 loading end")

        self.frame_queue = queue.Queue(maxsize=5)  # queue storing the frame to be sent
        # self.timer_send = QTimer(self)
        # self.timer_send.timeout.connect(self.send_frame)
        # self.timer_send.start(50)
        # print("timer2 loading end")

        self.update_graphics_signal.connect(self.update_graphics_draw)

        threading.Thread(target=self.listen_server_message, daemon=True).start()  # aia



    # change style methods: 5
    def applyStyleSheet(self, styleSheetPath):
        try:
            with open(styleSheetPath, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet: {e}")

    def changeStyleToStarrySky(self):
        global_settings.change_style_sheet("sky")
        self.applyStyleSheet(r"cameraWindow\res\qss\style.qss")

    def changeStyleToSea(self):
        global_settings.change_style_sheet("sea")
        self.applyStyleSheet(r"cameraWindow\res\qss\style1.qss")

    def changeStyleToDesert(self):
        global_settings.change_style_sheet("desert")
        self.applyStyleSheet(r"cameraWindow\res\qss\style2.qss")

    def changeStyleToGrassland(self):
        global_settings.change_style_sheet("grassland")
        self.applyStyleSheet(r"cameraWindow\res\qss\style3.qss")

    def openRecordFolder(self):
        record_path = os.path.join(QCoreApplication.applicationDirPath(), "record")
        # check OS
        if os.name == 'nt':  # Windows
            os.startfile(record_path)
        elif os.name == 'posix':  # macOS和Linux
            try:
                # macos
                os.system(f'open "{record_path}"')
            except:
                # linux
                os.system(f'xdg-open "{record_path}"')

    # take screen shot triggered by shotButton
    def takeScreenshot(self):
        record_path = os.path.join(QCoreApplication.applicationDirPath(), "record")
        if not os.path.exists(record_path):
            os.makedirs(record_path, exist_ok=True)
        screenshot_filename = os.path.join(QCoreApplication.applicationDirPath(), "record",
                                           "screenshot-{}.png".format(time.strftime("%Y%m%d-%H%M%S")))
        screenshot = self.grab()
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

    def append_to_console(self, message):
        self.textEdit.append(message)

    # 本方法因为存在bug废弃
    # this method abandoned because of existence of bugs
    def back_action(self):
        print("back action")
        self.append_to_console("you are kicked")

        self.cleanup_resources()

        QMessageBox.warning(self, 'You are kicked by an admin.', QMessageBox.Ok)

        # self.back_to_main_signal.emit()
        self.close()

    def display_frame(self):
        # show the frames caught by camera
        try:
            ret, frame = self.cap.read()
            if ret:
                self.process_frame(frame)  # process and show main method
        except Exception as e:
            self.append_to_console("error in reading camera" + str(e))

    # process and show frames
    def process_frame(self, frame):
        try:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            cv2.rectangle(frame, (self.x, self.y), (self.x + self.w, self.y + self.h), (255, 0, 0), 2)

            cv2.putText(frame, f"{self.emotion}: {self.probability}%", (self.x+20, self.y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (255, 255, 255), 2)

            h, w, ch = frame.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(convert_to_Qt_format)
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.graphicsView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
            # self.draw_graphics()
        except Exception as e:
            self.append_to_console("error in processing and showing frame" + str(e))
        if self.frame_queue.full():
            self.frame_queue.get()
        self.frame_queue.put(frame)

        # if is recording then also record
        if self.is_recording and self.video_writer is not None:
            self.video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    # this method abandoned
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
    def closeEvent(self, event):  # 重写关闭窗口函数，清理资源
        self.cleanup_resources()
        self.client_socket.send("close".encode())
        event.accept()

    def cleanup_resources(self):
        print("Cleaning up resources")
        if self.is_recording:
            self.toggleRecording()  # 停止录制并保存
        print("recording stop")

        self.is_running = False

        if self.timer_show.isActive():
            self.timer_show.stop()
        print("time show stop")

        # if self.timer_send.isActive():
        #    self.timer_send.stop()

        if self.cap.isOpened():
            self.cap.release()
        print("camera stop")

        if self.timeout_timer is not None:
            self.timeout_timer.cancel()
        print("time out stop")

        # self.client_socket.close()
        # self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client_socket.connect((self.server_host, self.server_port))
        # self.clear_socket_buffer()
        print("Resources cleaned up")

    def update_graphics_draw(self, message):

        faces_data = message.split(',')  # different faces may be divided by ","
        for face_data in faces_data:
            if face_data.strip():
                data_parts = face_data.strip().split(' ')
                if len(data_parts) == 6:
                    self.emotion, probability, x, y, w, h = data_parts
                    self.probability = float(probability)
                    self.x = int(x)
                    self.y = int(y)
                    self.w = int(w)
                    self.h = int(h)

        # clean previous rectangle and emotion text before draw the next faces
        # self.scene.clear()

    # Method sending frames to server
    def send_frame(self):
        if not self.frame_queue.empty() and self.is_running:
            print("try to send")
            frame = self.frame_queue.get()
            try:
                img_encode = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])[1]
                byte_data = img_encode.tobytes()
                length = len(byte_data)
                self.client_socket.sendall(str(length).encode() + b'\n')
                self.client_socket.sendall(byte_data)
            except Exception as e:
                self.append_to_console("error in packing and sending" + str(e))

    """
    listen to server, handling the messages from server
    """

    def listen_server_message(self):
        self.last_ok_received = time.time()
        self.check_for_timeout()
        time.sleep(1)
        while self.is_running:
            try:
                time.sleep(0.2)
                self.send_frame()
                print("listening...")
                server_message = self.client_socket.recv(512).decode()
                print(f"receive message: {server_message}")
                if server_message.startswith("B:"):
                    self.update_graphics_signal.emit(server_message[2:])
                    self.last_ok_received = time.time()
                elif server_message == "disconnect":
                    print("received disconnect from server")
                    self.back_action()
                    break
                else:
                    print("other message...")
                    # self.last_ok_received = time.time()
                    self.append_to_console(server_message)
                    # print(server_message)
            except Exception as e:
                print("Error in receiving message from server: " + str(e))
                break

    def check_for_timeout(self):
        if time.time() - self.last_ok_received > 5:  # try to resend if can not send after 10 secs
            print("sending error, retry")
            self.send_frame()
            # self.append_to_console("Error in sending images to server, try to resend")

        self.timeout_timer = threading.Timer(5, self.check_for_timeout)  # continue checking after 10 secs
        self.timeout_timer.start()

    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()

    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()
