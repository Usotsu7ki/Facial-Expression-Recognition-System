# login_window_entrance.py

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import global_settings
import resources_rc
import sys
import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QApplication, QProgressDialog
import socket

from ProgressBarDialog import ProgressBarDialog
from camera_window import CameraWindow
from admin_window import AdminWindow
from contactus import ContactUsDialog
from forgetPasswordWindow import ForgetPasswordWindow
from help import HelpDialog
from registerWindow import RegisterWindow


def read_server_address():
    with open("address.txt", "r") as file:
        lines = file.readlines()
        host = lines[0].strip()
        port = int(lines[1].strip())
    return host, port

# Add a loading bar(only for beauty)
def show_loading_dialog():
    progressDialog = ProgressBarDialog()
    progressDialog.setWindowTitle("Launching, Please Wait")
    progressDialog.setWindowModality(Qt.ApplicationModal)
    progressDialog.show()

    # update the progress bar
    for i in range(1, 71):
        progressDialog.updateProgress(i)
        time.sleep(0.01)

    progressDialog.close()

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('login/widget.ui', self)  # load ui

        self.label_pwd_2.setPixmap(QPixmap(":/res/pic/user_name.png"))


        self.btn_login.clicked.connect(self.submitPassword)  # bind submit username and password to the button
        #self.btn_forget.clicked.connect(self.skipLogin)

        self.lineE_username.setPlaceholderText("Enter username")

        self.lineE_pwd.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton_register.clicked.connect(self.openRegisterWindow) #register function
        self.pushButton_fgtpwd.clicked.connect(self.openForgetPasswordWindow) #forget password function

        self.btn_help.clicked.connect(self.contactActionTriggered)
        self.btn_contact.clicked.connect(self.helpActionTriggered)

        print("Window initialized")

        self.host, self.port = read_server_address()
        self.is_socket_connection = True
        self.client_socket = self.connect_to_server()  # connect to server


    # Change UI style 5 methods
    def applyStyleSheet(self, styleSheetPath):
        try:
            with open(styleSheetPath, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet: {e}")


    # Open camera window
    def handle_client(self):
        reply = QMessageBox.question(self, "Webcam Permission", "Please give us permission to open the camera.",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("open camera window")
            self.client_socket.send("request_ok".encode())
            if self.client_socket.recv(1024).decode() == "ok":
                print("receive respnce ok from server, open the webcam and send imgs")
                self.camera_window = CameraWindow(self.client_socket,self)
                self.camera_window.show()
                self.hide()
            else:
                print(self.client_socket.recv(1024).decode())
        else:
            self.client_socket.send(b'back')
            print("camera permission not granted")


    def openRegisterWindow(self):
        print("open stage open")
        self.register_window = RegisterWindow(self.client_socket)
        self.register_window.show()

    def openForgetPasswordWindow(self):
        print("forget password open")
        self.forget_password_window = ForgetPasswordWindow(self.client_socket)
        self.forget_password_window.show()


    def connect_to_server(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((self.host, self.port))
            return client_socket
        except Exception as e:
            print(f"error in connect the server, please check the server or the internet:{e}")
            QMessageBox.warning(self, "Error in connect the server", "Please check the server or the internet.")
            self.is_socket_connection = False


    # Submit username and password form lineE then send to server for checking
    # After receiving server messages, open different windows based on judgements
    def submitPassword(self):
        username = self.lineE_username.text()
        password = self.lineE_pwd.text()
        if not self.is_socket_connection:
            QMessageBox.warning(self,"No connection to server.","Please check the server and the internet")
            return

        if username and password:
            try:
                login_info = f"login:{username}:{password}"
                self.client_socket.send(login_info.encode())
                print("username password send complete")
                response = self.client_socket.recv(1024).decode()
                print("Received:", response)
                if response == "admin":
                    print("receive admin message，init and open admin window")
                    self.admin_window = AdminWindow(self.client_socket)
                    self.admin_window.show()
                    self.close()
                    print("admin stage open")
                elif response == "client": # open client window
                    self.handle_client()
                    return
                elif response == "fail": # login fail
                    QMessageBox.warning(self, "login Failed", "No such user found or incorrect password.", QMessageBox.Ok)
                else:
                    QMessageBox.warning(self, "Error", "An error occurred during login.", QMessageBox.Ok)
                    print("wrong username or password")
            except Exception as e:
                print(f"Execption in sending login or receive response: {e}")
                self.handle_client()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter both username and password.", QMessageBox.Ok)


    """
    skip login(abadon)
    跳过登录，给其相应问题框：如果同意给摄像头权限就打开摄像头，关闭登录窗口
            不同意就不操作
    """
    #skipLogin方法已经废弃
    #this method was abadoned because of Addition od register and accounts
    def skipLogin(self):
        reply = QMessageBox.question(self, "webcam permission", "Please give us permission to open camera？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("jump to camera window")
            self.client_socket.send("client".encode())
            if(self.client_socket.recv(1024).decode()=="ok"):
                print("receive respnce ok from server, open the webcam and send imgs")
            else:
                print(self.client_socket.recv(1024).decode())
            self.camera_window = CameraWindow(self.client_socket,self)
            self.camera_window.show()
            self.hide()

    # help and contact us action
    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()


    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()

    def showEvent(self, event):
        super().showEvent(event)
        self.applyStyleSheet(global_settings.login_style_path)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    show_loading_dialog()
    try:
        with open(r"login/res/qss/style-1.qss", "r", encoding="utf-8") as file:
            stylesheet = file.read()
            app.setStyleSheet(stylesheet)
    except Exception as e:
        print(f"Error loading stylesheet: {e}")

    mainWin = MainWindow()
    mainWin.setWindowTitle("Log in")
    mainWin.show()

    sys.exit(app.exec_())
