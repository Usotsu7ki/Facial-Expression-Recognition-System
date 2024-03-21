from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from contactus import ContactUsDialog
from help import HelpDialog


class RegisterWindow(QtWidgets.QWidget):
    def __init__(self, client_socket):
        super(RegisterWindow, self).__init__()

        uic.loadUi('register/widget.ui', self)  # load ui

        self.client_socket = client_socket
        # print(self.client_socket)

        self.btn_submit.clicked.connect(self.onSubmit)

        self.btn_forget_2.clicked.connect(self.contactActionTriggered)
        self.btn_forget_3.clicked.connect(self.helpActionTriggered)

        self.btn_1.clicked.connect(self.changeStyleToStarrySky)
        self.btn_2.clicked.connect(self.changeStyleToSea)
        self.btn_3.clicked.connect(self.changeStyleToDesert)
        self.btn_4.clicked.connect(self.changeStyleToGrassland)

        self.label_pwd.setScaledContents(True)
        self.label_pwd_2.setScaledContents(True)
        self.label_pwd_3.setScaledContents(True)
        self.label_pwd_4.setScaledContents(True)
        self.label_pwd_5.setScaledContents(True)

        self.lineE_username.setPlaceholderText("User name")
        self.lineE_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineE_security_question.setPlaceholderText("Security")
        self.lineE_security_ans.setPlaceholderText("Security answer")
        self.lineE_admin_number.setPlaceholderText("Admin code(if you have)")

        # load qss
        try:
            with open("register/res/qss/style-1.qss", "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet for register window: {e}")

        print("加载完毕")

    # 5 methods about changing stylesheet
    def applyStyleSheet(self, styleSheetPath):
        try:
            with open(styleSheetPath, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet: {e}")

    def changeStyleToStarrySky(self):
        self.applyStyleSheet(r"register\res\qss\style-1.qss")

    def changeStyleToSea(self):
        self.applyStyleSheet(r"register\res\qss\style-2.qss")

    def changeStyleToDesert(self):
        self.applyStyleSheet(r"register\res\qss\style-3.qss")

    def changeStyleToGrassland(self):
        self.applyStyleSheet(r"register\res\qss\style-4.qss")


    # Submit the username, pwd, security ques and ans to server, if have admin code, also send(optional)
    # Judge whether register successfully depend on server response
    def onSubmit(self):
        username = self.lineE_username.text()
        password = self.lineE_pwd.text()
        security_question = self.lineE_security_question.text()
        security_answer = self.lineE_security_ans.text()
        admin_number = self.lineE_admin_number.text()  # admin number可以为空

        # username pwd security ques and security ans compulsory
        if not all([username, password, security_question, security_answer]):
            QMessageBox.warning(self, "Incomplete Information", "Please fill in all required fields.")
            return
        print(f"to be send: {username},{password},{security_question},{security_answer},{admin_number}")

        self.sendRegistrationInfo(username, password, security_question, security_answer, admin_number)

        response = self.client_socket.recv(1024).decode()  # get response and judge
        if response == "register success":
            QMessageBox.information(self, "Success", "Registration successful!")
            self.close()  # register success
        elif response == "fail_admin":
            QMessageBox.warning(self, "Registration Failed", "Incorrect admin number.")
        elif response == "fail_username_same":
            QMessageBox.warning(self, "Registration Failed", "Username already exists.")
        elif response == "fail_database":
            QMessageBox.warning(self, "Registration Failed", "Database error occurred.")
        else:
            QMessageBox.warning(self, "Registration Failed", "An unknown error occurred.")


    def sendRegistrationInfo(self, username, password, security_question, security_answer, admin_number):
        # info format
        # 注意： server should split in same format
        info = f"register:{username}|{password}|{security_question}|{security_answer}|{admin_number}"

        try:
            self.client_socket.send(info.encode())
            print("send end")
        except Exception as e:
            print(f"sned fail: {e}")
            QMessageBox.warning(self, "Connection Error", "Failed to send registration info to the server.")
            return



    #help and contact us

    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()

    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()
