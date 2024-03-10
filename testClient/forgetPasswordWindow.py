from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from contactus import ContactUsDialog
from help import HelpDialog


class ForgetPasswordWindow(QtWidgets.QDialog):
    def __init__(self, client_socket):
        super(ForgetPasswordWindow, self).__init__()
        uic.loadUi('forget/widget.ui', self)

        self.client_socket = client_socket

        # 加载样式表
        try:
            with open("forget/res/qss/style-1.qss", "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet for forget password window: {e}")

        self.username = self.findChild(QtWidgets.QLineEdit, 'username')
        self.security_answer = self.findChild(QtWidgets.QLineEdit, 'security_answer')
        self.new_password = self.findChild(QtWidgets.QLineEdit, 'new_password')
        self.security_label = self.findChild(QtWidgets.QLabel, 'security_label')

        self.btn_submit = self.findChild(QtWidgets.QPushButton, 'btn_forget')
        self.btn_submit.clicked.connect(self.onSubmit)

        self.btn_forget_2.clicked.connect(self.contactActionTriggered)
        self.btn_forget_3.clicked.connect(self.helpActionTriggered)

        self.btn_getSecurity = self.findChild(QtWidgets.QPushButton, 'btn_getSecurity')
        self.btn_getSecurity.clicked.connect(self.getSecurity)

        print("forget password界面导入完成")

    def getSecurity(self):
        username = self.username.text()
        if not username:
            QMessageBox.warning(self, "Incomplete Information", "Please fill in username.")
            self.security_label.clear()
            return
        info = f"forget:{username}"
        try:
            self.client_socket.send(info.encode())

            response = self.client_socket.recv(1024).decode()
            if response == "username_notexist":
                QMessageBox.warning(self, "Username not exist")
                print("username not exist ")
                self.security_label.clear()
                return
            else:
                self.security_label.setText(response)
                print(response)
        except Exception as e:
            print(f"发送失败: {e}")
            QMessageBox.warning(self, "Connection Error", "Failed to send change password to server.")
            self.security_label.clear()


    def onSubmit(self):
        # 获取用户输入
        username = self.username.text()
        security_answer = self.security_answer.text()
        new_password = self.new_password.text()

        # 检查输入是否完整
        if not all([username, security_answer, new_password]):
            QMessageBox.warning(self, "Incomplete Information", "Please fill in all required fields.")
            print("info lack")
            return

        info = f"change:{username}:{security_answer}:{new_password}"
        print(f"try send to server change password:{info}")
        try:
            self.client_socket.send(info.encode())
            print("发送完毕")

            response = self.client_socket.recv(1024).decode()
            if response == "success":
                QMessageBox.information(self, "Success", "Password change successful.")
                self.close()
            elif response == "fail_database":
                QMessageBox.warning(self, "Change Failed", "There was a database error. Please try again later.")
            else:
                QMessageBox.warning(self, "Security answer incorrect or other error. Please try again.")

        except Exception as e:
            print(f"发送失败: {e}")
            QMessageBox.warning(self, "Connection Error", "Failed to send registration info to the server.")
            return





    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()

    # help按钮的事件处理函数
    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()