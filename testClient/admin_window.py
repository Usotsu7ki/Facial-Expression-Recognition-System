import socket
import threading
from PyQt5 import QtWidgets, uic, QtCore
# import sys

from contactus import ContactUsDialog
from help import HelpDialog

HOST = '127.0.0.1'
PORT = 8080
ADDRESS = (HOST, PORT)
#这里之后要改成读取本地ip


class AdminWindow(QtWidgets.QMainWindow):

    update_client_list_signal = QtCore.pyqtSignal(list) #signal to update client list

    def __init__(self, client_socket):
        super().__init__()
        uic.loadUi('admin\mainwindow.ui', self)
        print("load ui finish")

        try:
            with open(r"admin\res\qss\style.qss", "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Error loading stylesheet in AdminWindow: {e}")

        self.client_socket = client_socket

        self.btn_1.clicked.connect(self.changeStyleToStarrySky)
        self.btn_2.clicked.connect(self.changeStyleToSea)
        self.btn_3.clicked.connect(self.changeStyleToDesert)
        self.btn_4.clicked.connect(self.changeStyleToGrassland)

        self.clientListWidget = self.findChild(QtWidgets.QListWidget, 'listWidget_2')
        self.consoleTextEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.sendButton = self.findChild(QtWidgets.QPushButton, 'sendButton')

        self.helpAction = self.findChild(QtWidgets.QAction, 'actionhelp')
        self.helpAction.triggered.connect(self.helpActionTriggered)
        self.contactAction = self.findChild(QtWidgets.QAction, 'actionContact_us')
        self.contactAction.triggered.connect(self.contactActionTriggered)

        self.sendButton.clicked.connect(self.sendMessage) # send button
        self.clientListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) # list right click menu
        self.clientListWidget.customContextMenuRequested.connect(self.showContextMenu) #showing menu

        self.update_client_list_signal.connect(self.update_client_list)
        self.start_receiving()
        print("init admin end")

    def applyStyleSheet(self, styleSheetPath):
        try:
            with open(styleSheetPath, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet: {e}")

    def changeStyleToStarrySky(self):
        self.applyStyleSheet(r"admin\res\qss\style.qss")

    def changeStyleToSea(self):
        self.applyStyleSheet(r"admin\res\qss\style1.qss")

    def changeStyleToDesert(self):
        self.applyStyleSheet(r"admin\res\qss\style2.qss")

    def changeStyleToGrassland(self):
        self.applyStyleSheet(r"admin\res\qss\style3.qss")

    def start_receiving(self):
        print("start receiving")
        self.client_socket.send("message from admin".encode())
        threading.Thread(target=self.receive_client_list, daemon=True).start()

    def receive_client_list(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                client_list_str = data.decode()
                client_list = client_list_str.split("\n")  # divide strings of different client sockets and added in lists
                print("receive client lists")
                self.update_client_list_signal.emit(client_list)  # update the current list and refresh
            except Exception as e:
                print(f"Error receiving client list: {e}")
                break

    def update_client_list(self, client_list):
        # clear the current list
        self.clientListWidget.clear()
        # using new list
        for client_address in client_list:
            if client_address and client_address != "disconnect" and not(HOST in client_address):  # Ensure the address not null, not admin itself
                self.add_client(client_address)

    def add_client(self, client_address):
        # add new client to list
        self.clientListWidget.addItem(client_address)

    def display_message(self, message):
        # append messages to testE
        self.consoleTextEdit.append(message)


    def showContextMenu(self, position):
        # Show mouse button menu and actions
        menu = QtWidgets.QMenu()
        disconnectAction = menu.addAction("kick this client")
        sendMessageAction = menu.addAction("send messages")
        action = menu.exec_(self.clientListWidget.mapToGlobal(position))
        if action == disconnectAction:
            self.kickClient()
        elif action == sendMessageAction:
            self.consoleTextEdit.setFocus()

    def kickClient(self):
        # send messages to server, kick the client chosen
        print("kick it")
        selected_item = self.clientListWidget.currentItem()
        if selected_item:
            client_address = selected_item.text()
            self.client_socket.send(("kick:" + client_address).encode())

    def sendMessage(self):
        print("begin sending message")
        selected_item = self.clientListWidget.currentItem()
        if selected_item:
            client_address = selected_item.text()
            message = self.consoleTextEdit.toPlainText().split('\n')[-1]  # send the last line
            full_message = "sendmessage|" + client_address + "|" + message
            self.client_socket.send(full_message.encode())

    def closeEvent(self, event):
        # overload the close
        if self.client_socket:
            self.client_socket.send("closeme".encode())
            self.client_socket.close()   ############ may be this should be added in camera window after cancel of return
        event.accept()



    def helpActionTriggered(self):
        print("open help dialog")
        dialog = HelpDialog(self)
        dialog.exec_()

    def contactActionTriggered(self):
        print("open contact us dialog")
        dialog = ContactUsDialog(self)
        dialog.exec_()