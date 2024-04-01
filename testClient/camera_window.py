import os
import queue
import threading

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QTimer, Qt, QCoreApplication
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox, QGraphicsScene
import cv2
import time
from socket import socket

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
    back_to_main_signal = QtCore.pyqtSignal()
    update_graphics_signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket,main_window):
        super().__init__()

        # these four lists r used to store the results from server
        self.xs = []
        self.ys = []
        self.ws = []
        self.hs = []
        self.probabilities = []
        self.emotions = []

        self.classes = ('Surprise', 'Fear', 'Disgust', 'Smile', 'Sadness', 'Anger', 'Neutral')

        # load ui
        uic.loadUi('cameraWindow/mainwindow.ui', self)
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
        self.actionback.triggered.connect(self.back_action)

        self.recordButton.setStyleSheet("border-image: url(:/res/pic/record.png);")
        self.recordButton.clicked.connect(self.switchforRecording)
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

        self.textEdit.setReadOnly(True) # the console only used to show messages

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
        # print("timer2 loading end")                          """cautious: this timer is already abandon"""

        self.update_graphics_signal.connect(self.updateGraphicsDraw)

        self.main_window = main_window
        self.back_to_main_signal.connect(main_window.show)

        self.client_socket.settimeout(3.0) #this is used to stop receive message, prevent disturp other windows

        threading.Thread(target=self.listeningMessages, daemon=True).start()  # aia


    # change background images for all scenes, 5 methods
    def applyStyleSheet(self, styleSheetPath):
        try:
            with open(styleSheetPath, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet: {e}")

    def changeStyleToStarrySky(self):
        global_settings.change_style_sheet("sky")  #apply the change for other window
        self.applyStyleSheet(r"cameraWindow/res/qss/style.qss")  # update this window

    def changeStyleToSea(self):
        global_settings.change_style_sheet("sea")
        self.applyStyleSheet(r"cameraWindow/res/qss/style1.qss")

    def changeStyleToDesert(self):
        global_settings.change_style_sheet("desert")
        self.applyStyleSheet(r"cameraWindow/res/qss/style2.qss")

    def changeStyleToGrassland(self):
        global_settings.change_style_sheet("grassland")
        self.applyStyleSheet(r"cameraWindow/res/qss/style3.qss")

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


    # take screenshot triggered by shotButton, this method will screenshot the whole widget
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
    def switchforRecording(self):
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


    # this method used to print some exception or message to the console in the main window
    def append_to_console(self, message):
        self.textEdit.append(message)


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
        # store the frame in queue(the queue is used to store the frames to be sent)
        if self.frame_queue.full():
            self.frame_queue.get()
        self.frame_queue.put(frame)

        # draw the frame and rectangles, and the results
        try:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            for i in range(len(self.emotions)):
                emotion_index = int(self.emotions[i])
                emotion_text = self.classes[emotion_index] # find the text using the number of the expression
                cv2.rectangle(frame, (self.xs[i], self.ys[i]), (self.xs[i] + self.ws[i], self.ys[i] + self.hs[i]),
                              (255, 0, 0), 2)
                cv2.putText(frame, f"{emotion_text}: {self.probabilities[i]}%", (self.xs[i] + 20, self.ys[i]),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

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


        # if is recording then also record
        if self.is_recording and self.video_writer is not None:
            self.video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))



    # Overload the close
    def closeEvent(self, event):
        self.cleanup_resources()
        self.client_socket.send("close".encode())
        event.accept()

    def cleanup_resources(self):
        print("Cleaning up resources")
        if self.is_recording:
            self.switchforRecording()  # if is recording, then stop and save
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

    def updateGraphicsDraw(self, message):
        print(message)
        self.xs.clear()
        self.ys.clear()
        self.ws.clear()
        self.hs.clear()
        self.probabilities.clear()
        self.emotions.clear()
        print("update: clean end")

        if not message:
            print("Received empty data after 'B:'")
            return

        # The example of message:       6, 6|'0.999', '0.999'|244, 145, 151, 150, 480, 24, 125, 125
        try:
            parts = message.split('|')

            emotions = parts[0].split(',')
            probabilities = parts[1].replace("'", "").split(',')
            boxFeatures = parts[2].split(',')

            print("split end")

            if len(emotions) == len(probabilities) and len(boxFeatures) % 4 == 0:
                self.emotions = emotions
                for probability in probabilities:
                    self.probabilities.append(float(probability))

                for i in range(0, len(boxFeatures), 4):
                    self.xs.append(int(boxFeatures[i]))
                    self.ys.append(int(boxFeatures[i + 1]))
                    self.ws.append(int(boxFeatures[i + 2]))
                    self.hs.append(int(boxFeatures[i + 3]))
                print("update: store end")

            else:
                print("the data received is in wrong format")

        except Exception as e:
            print('error happen in split the messsage: '+ e)


        # clean previous rectangle and emotion text before draw the next faces
        # self.scene.clear()

    # Method sending frames to server
    def sendingFrame(self):
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
    def listeningMessages(self):
        self.last_ok_received = time.time()
        self.checkWhetherTimeout()
        time.sleep(1)
        while self.is_running:
            try:
                time.sleep(0.2)
                self.sendingFrame()
                print("listening...")
                try:
                    server_message = self.client_socket.recv(1024).decode()
                except socket.timeout:
                    if not self.is_running:
                        break
                print(f"receive message: {server_message}")
                if server_message.startswith("B:"):
                    if server_message=="B:":
                        self.last_ok_received = time.time()
                        continue
                    clean_message = server_message[2:]
                    self.update_graphics_signal.emit(clean_message)
                    self.last_ok_received = time.time()
                elif server_message == "disconnect":
                    print("received disconnect from server")
                    QMessageBox.Warning(self,"Disconnect","Sorry, you are kicked by the admin",QMessageBox.Ok)
                    self.close()
                    break
                elif server_message == 'client':
                    self.main_window.handle_client()
                else:
                    print("other message...")
                    # self.last_ok_received = time.time()
                    self.append_to_console(server_message)
                    # print(server_message)
            except Exception as e:
                print("Error in receiving message from server: " + str(e))
                break

    # check and resend when the server can not handle frames and send messages back well
    def checkWhetherTimeout(self):
        if time.time() - self.last_ok_received > 5:  # try to resend if can not send after 10 secs
            print("sending error, retry")
            self.sendingFrame()
            # self.append_to_console("Error in sending images to server, try to resend")

        self.timeout_timer = threading.Timer(5, self.checkWhetherTimeout)  # continue checking after 10 secs
        self.timeout_timer.start()

    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()

    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()


    def back_action(self):
        print("back action")
        self.append_to_console("you are kicked")

        self.cleanup_resources()

        # QMessageBox.warning(self, "Back", "You are kicked or .")

        self.back_to_main_signal.emit()
        self.client_socket.send(b'close\n')
        self.close()

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