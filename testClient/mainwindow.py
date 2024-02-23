# mainwindow.py
import resources_rc
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import socket
from camera_window import CameraWindow
from admin_window import AdminWindow

# 服务端ip地址
HOST = '127.0.0.1'
# 服务端端口号
PORT = 8080
ADDRESS = (HOST, PORT)

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('login\widget.ui', self)  # 加载UI文件

        self.btn_login.clicked.connect(self.submitPassword)  # 绑定提交按钮的点击事件
        self.btn_forget.clicked.connect(self.skipLogin)  # 绑定跳过按钮的点击事件

        self.lineE_pwd.setEchoMode(QtWidgets.QLineEdit.Password)

        self.btn_forget_2.clicked.connect(self.contactUs)
        self.btn_forget_3.clicked.connect(self.help)

        print("Window initialized")

        self.client_socket = self.connect_to_server()  # 建立到服务器的连接


    def connect_to_server(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect(ADDRESS)
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

    def contactUs(self):
        QMessageBox.information(self, 'Contact Us', 'Contact information: [Your Contact Info]')

    # help按钮的事件处理函数
    def help(self):
        QMessageBox.information(self, 'Help', 'Help information: [Your Help Info]')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
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
