from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from contactus import ContactUsDialog
from help import HelpDialog


class RegisterWindow(QtWidgets.QDialog):
    def __init__(self, client_socket):
        super(RegisterWindow, self).__init__()
        uic.loadUi('register/widget.ui', self)  # 加载注册窗口的UI文件

        self.client_socket = client_socket

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



    def onSubmit(self):
        username = self.lineE_username.text()
        password = self.lineE_pwd.text()
        security_question = self.lineE_security_question.text()
        security_answer = self.lineE_security_ans.text()
        admin_number = self.lineE_admin_number.text()  # 可以为空

        # 前四项必填
        if not all([username, password, security_question, security_answer]):
            QMessageBox.warning(self, "Incomplete Information", "Please fill in all required fields.")
            return

        # 发给服务器
        self.sendRegistrationInfo(username, password, security_question, security_answer, admin_number)

    def sendRegistrationInfo(self, username, password, security_question, security_answer, admin_number):
        info = f"register:{username}|{password}|{security_question}|{security_answer}|{admin_number}"
        self.client_socket.send(info.encode())




    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()

    # help按钮的事件处理函数
    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()
