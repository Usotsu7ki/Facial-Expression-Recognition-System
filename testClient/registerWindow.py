from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from contactus import ContactUsDialog
from help import HelpDialog


class RegisterWindow(QtWidgets.QWidget):
    def __init__(self, client_socket):
        super(RegisterWindow, self).__init__()

        uic.loadUi('register/widget.ui', self)  # 加载注册窗口的UI文件

        self.client_socket = client_socket
        print(self.client_socket)

        self.btn_submit.clicked.connect(self.onSubmit)

        self.btn_forget_2.clicked.connect(self.contactActionTriggered)
        self.btn_forget_3.clicked.connect(self.helpActionTriggered)

        self.label_pwd_2.setScaledContents(True)
        self.label_pwd_3.setScaledContents(True)
        self.label_pwd_4.setScaledContents(True)
        self.label_pwd_5.setScaledContents(True)

        self.lineE_username.setPlaceholderText("User name")
        self.lineE_pwd.setPlaceholderText("Password")
        self.lineE_security_question.setPlaceholderText("Security")
        self.lineE_security_ans.setPlaceholderText("Security answer")
        self.lineE_admin_number.setPlaceholderText("Admin code(if you have)")

        # 加载样式表
        try:
            with open("register/res/qss/style-1.qss", "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet for register window: {e}")

        print("加载完毕")



    def onSubmit(self):
        username = self.lineE_username.text()
        password = self.lineE_pwd.text()
        security_question = self.lineE_security_question.text()
        security_answer = self.lineE_security_ans.text()
        admin_number = self.lineE_admin_number.text()  # admin number可以为空

        # 前四项必填
        if not all([username, password, security_question, security_answer]):
            QMessageBox.warning(self, "Incomplete Information", "Please fill in all required fields.")
            return
        print(f"即将发送注册内容:{username},{password},{security_question},{security_answer},{admin_number}")
        # 发给服务器
        self.sendRegistrationInfo(username, password, security_question, security_answer, admin_number)

        response = self.client_socket.recv(1024).decode()  # 接收服务器响应
        if response == "register success":
            QMessageBox.information(self, "Success", "Registration successful!")
            self.close()  # 注册成功，关闭注册窗口
        elif response == "fail_admin":
            QMessageBox.warning(self, "Registration Failed", "Incorrect admin number.")
        elif response == "fail_username_same":
            QMessageBox.warning(self, "Registration Failed", "Username already exists.")
        elif response == "fail_database":
            QMessageBox.warning(self, "Registration Failed", "Database error occurred.")
        else:
            QMessageBox.warning(self, "Registration Failed", "An unknown error occurred.")

    def sendRegistrationInfo(self, username, password, security_question, security_answer, admin_number):
        info = f"register:{username}|{password}|{security_question}|{security_answer}|{admin_number}"
        try:
            self.client_socket.send(info.encode())
            print("发送完毕")
        except Exception as e:
            print(f"发送失败: {e}")
            QMessageBox.warning(self, "Connection Error", "Failed to send registration info to the server.")
            return
        # 发给服务器的格式，服务器对应接收并处理




    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()

    # help按钮的事件处理函数
    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()
