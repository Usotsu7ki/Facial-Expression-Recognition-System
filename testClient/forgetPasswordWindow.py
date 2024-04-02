from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

import global_settings
from contactus import ContactUsDialog
from help import HelpDialog


class ForgetPasswordWindow(QtWidgets.QDialog):
    def __init__(self, client_socket):
        super(ForgetPasswordWindow, self).__init__()
        uic.loadUi('forget/widget.ui', self)

        self.client_socket = client_socket

        try:
            with open(global_settings.forget_style_path, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet for register window: {e}")

        self.label_pwd_2.setScaledContents(True)
        self.label_pwd_3.setScaledContents(True)
        self.label_pwd_4.setScaledContents(True)
        self.label_pwd_5.setScaledContents(True)
        self.label_pwd_6.setScaledContents(True)
        # print("5 label loading complete")


        self.username.setPlaceholderText("User name")
        self.security_label = self.findChild(QtWidgets.QLabel, 'security_label')
        self.security_answer.setPlaceholderText("Security answer")
        self.new_password.setPlaceholderText("New password")
        self.check_password.setPlaceholderText("Confirm password")
        # print("5 lineE loading complete")


        # self.btn_1.clicked.connect(self.changeStyleToStarrySky)
        # self.btn_2.clicked.connect(self.changeStyleToSea)
        # self.btn_3.clicked.connect(self.changeStyleToDesert)
        # self.btn_4.clicked.connect(self.changeStyleToGrassland)
        # # print("4个风格按钮加载完成")

        self.btn_submit.clicked.connect(self.onSubmit)

        self.btn_forget_2.clicked.connect(self.contactActionTriggered)
        self.btn_forget_3.clicked.connect(self.helpActionTriggered)
        # print("3个按钮加载完成")

        self.btn_getSecurity.clicked.connect(self.getSecurity)
        # print("forget password window loading end")

    def getSecurity(self):
        # get the security question from server using username submitted
        username = self.username.text()
        if not username:
            QMessageBox.warning(self, "Incomplete Information", "Please fill in username.")
            self.security_label.clear()
            return
        info = f"forget:{username}"
        try:
            self.client_socket.send(info.encode())

            response = self.client_socket.recv(1024).decode() # get security ques
            if response == "username_notexist":
                QMessageBox.warning(self, "Username not exist")
                print("username not exist ")
                self.security_label.clear()
                return
            else:
                self.security_label.setText(response) # show the ques in label
                print(response)
        except Exception as e:
            print(f"Send fail: {e}")
            QMessageBox.warning(self, "Connection Error", "Failed to send change password to server.")
            self.security_label.clear()

    # 5 methods about style change
    def applyStyleSheet(self, styleSheetPath):
        try:
            with open(styleSheetPath, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet: {e}")


    # Press submit button, submit all messages inputted
    def onSubmit(self):
        # 获取用户输入
        username = self.username.text()
        security_answer = self.security_answer.text()
        new_password = self.new_password.text()
        check_password = self.check_password.text()

        if not all([username, security_answer, new_password]): # ensure all lineE inputted
            QMessageBox.warning(self, "Incomplete Information", "Please fill in all required fields.")
            print("info lack")
            return

        if new_password != check_password: # confirm password
            return

        info = f"change:{username}:{security_answer}:{new_password}"
        print(f"try send to server change password:{info}")
        try:
            self.client_socket.send(info.encode())
            print("send end")

            response = self.client_socket.recv(1024).decode()
            if response == "success": # change success
                QMessageBox.information(self, ":D", "Reset password successfully.")
                self.close()
            elif response == "fail_database": # something wrong happens in database
                QMessageBox.warning(self, "Change Failed", "There was a database error. Please try again later.")
            else:
                QMessageBox.warning(self, "Security answer incorrect or other error. Please try again.")

        except Exception as e:
            print(f"sending fail: {e}")
            QMessageBox.warning(self, "Connection Error", "Failed to send registration info to the server.")
            return



    # help and contact us

    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()

    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()