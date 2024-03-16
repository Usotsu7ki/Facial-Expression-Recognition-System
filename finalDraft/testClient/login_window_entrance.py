# login_window_entrance.py

from PyQt5.QtCore import Qt

import resources_rc
import sys
import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QApplication, QProgressDialog
import socket
from camera_window import CameraWindow
from admin_window import AdminWindow
from contactus import ContactUsDialog
from help import HelpDialog


def read_server_address():
    with open("address.txt", "r") as file:
        lines = file.readlines()
        host = lines[0].strip()
        port = int(lines[1].strip())
    return host, port

def show_loading_dialog():
    # 创建一个QProgressDialog实例
    progressDialog = QProgressDialog("Loading...", None, 0, 100)
    progressDialog.setWindowTitle("Launching, Please Wait")
    progressDialog.setCancelButton(None)  # 禁用取消按钮
    progressDialog.setWindowModality(Qt.ApplicationModal)
    progressDialog.show()

    # 更新进度条来模拟加载过程
    for i in range(1, 101):
        progressDialog.setValue(i)
        QApplication.processEvents()  # 处理事件，保持界面响应
        time.sleep(0.01)

    progressDialog.close()

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('login\widget.ui', self)  # 加载UI文件

        self.btn_login.clicked.connect(self.submitPassword)  # 绑定提交按钮的点击事件
        self.btn_forget.clicked.connect(self.skipLogin)  # 绑定跳过按钮的点击事件

        '''
        self.helpAction = self.findChild(QtWidgets.QAction, 'actionhelp')
        self.helpAction.triggered.connect(self.helpActionTriggered)
        self.contactAction = self.findChild(QtWidgets.QAction, 'actioncontact_us')
        self.contactAction.triggered.connect(self.contactActionTriggered)
        '''

        self.lineE_pwd.setEchoMode(QtWidgets.QLineEdit.Password)

        self.btn_forget_2.clicked.connect(self.contactActionTriggered)
        self.btn_forget_3.clicked.connect(self.helpActionTriggered)

        print("Window initialized")

        self.host, self.port = read_server_address()

        self.client_socket = self.connect_to_server()  # 建立到服务器的连接



    def connect_to_server(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((self.host, self.port))
            return client_socket
        except Exception as e:
            print(f"error in connect the server, please check the server or the internet:{e}")
            #reply = QMessageBox.show(self,"connet fail")

    def submitPassword(self):
        password = self.lineE_pwd.text()
        self.client_socket.send(("password:"+password).encode())  # 向服务器发送密码
        response = self.client_socket.recv(1024).decode()  # 接收服务器响应
        if response == "admin":
            self.admin_window = AdminWindow(self.client_socket)  # 创建管理员界面
            self.admin_window.show()
            self.close()
            print("admin stage open")
        else:
            print("wrong password")
            #self.lineEdit.setText("wrong password")  # 显示密码错误信息

    """
    跳过登录，给其相应问题框：如果同意给摄像头权限就打开摄像头，关闭登录窗口
            不同意就不操作
    """
    def skipLogin(self):
        reply = QMessageBox.question(self, 'webcam permission', 'Please give us permission to open camera？',
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

    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()

    # help按钮的事件处理函数
    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    show_loading_dialog()
    try:
        with open(r"login\res\qss\style-1.qss", "r", encoding="utf-8") as file:
            stylesheet = file.read()
            app.setStyleSheet(stylesheet)
    except Exception as e:
        print(f"Error loading stylesheet: {e}")

    mainWin = MainWindow()
    mainWin.setWindowTitle("Log in")  # 设置窗口标题
    mainWin.show()

    sys.exit(app.exec_())
