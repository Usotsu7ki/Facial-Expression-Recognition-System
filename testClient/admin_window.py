import socket
import threading

# import cv2
# import numpy as np
from PyQt5 import QtWidgets, uic, QtCore
# import sys

from PyQt5.QtWidgets import QMessageBox

HOST = ''
PORT = 8080
ADDRESS = (HOST, PORT)


class AdminWindow(QtWidgets.QMainWindow):

    update_client_list_signal = QtCore.pyqtSignal(list) #更新客户端列表信号

    def __init__(self, client_socket):
        super().__init__()
        uic.loadUi('admin.ui', self)
        self.client_socket = client_socket

        self.clientListWidget = self.findChild(QtWidgets.QListWidget, 'listWidget')
        self.consoleTextEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.sendButton = self.findChild(QtWidgets.QPushButton, 'sendButton')

        self.helpAction = self.findChild(QtWidgets.QAction, 'actionhelp')
        self.helpAction.triggered.connect(self.helpActionTriggered)
        self.contactAction = self.findChild(QtWidgets.QAction, 'actioncontact_us')
        self.contactAction.triggered.connect(self.contactActionTriggered)

        self.sendButton.clicked.connect(self.sendMessage) # send button
        self.clientListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) # list right click menu
        self.clientListWidget.customContextMenuRequested.connect(self.showContextMenu) #showing menu

        self.update_client_list_signal.connect(self.update_client_list)
        self.start_receiving()

    def start_receiving(self):
        print("start receiving")
        self.client_socket.send("message from admin".encode())
        threading.Thread(target=self.receive_client_list, daemon=True).start()

    def receive_client_list(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                client_list_str = data.decode()
                client_list = client_list_str.split("\n")  # 分割字符串获取客户端列表
                print("receive client lists")
                self.update_client_list_signal.emit(client_list)  # 发射信号
            except Exception as e:
                print(f"Error receiving client list: {e}")
                break

    def update_client_list(self, client_list):
        # 清除当前列表
        self.clientListWidget.clear()
        # 添加新的客户端列表
        for client_address in client_list:
            if client_address:  # 确保地址不是空字符串
                self.add_client(client_address)

    def add_client(self, client_address):
        # 添加新客户端到列表
        self.clientListWidget.addItem(client_address)

    def display_message(self, message):
        # 在控制台显示消息
        self.consoleTextEdit.append(message)


    def showContextMenu(self, position):
        # 显示右键菜单
        menu = QtWidgets.QMenu()
        disconnectAction = menu.addAction("kick this client")
        sendMessageAction = menu.addAction("send messages")
        action = menu.exec_(self.clientListWidget.mapToGlobal(position))
        if action == disconnectAction:
            self.kickClient()
        elif action == sendMessageAction:
            self.consoleTextEdit.setFocus()

    def kickClient(self):
        # 给服务端发送消息踢对应的客户端
        print("kick it")
        selected_item = self.clientListWidget.currentItem()
        if selected_item:
            client_address = selected_item.text()
            self.client_socket.send(("kick:" + client_address).encode())

    def sendMessage(self):
        print("begin send message")
        selected_item = self.clientListWidget.currentItem()
        if selected_item:
            client_address = selected_item.text()
            message = self.consoleTextEdit.toPlainText().split('\n')[-1]  # 获取最后一行文本
            full_message = "sendmessage|" + client_address + "|" + message
            #这里有很难办的文字处理问题
            self.client_socket.send(full_message.encode())

    def closeEvent(self, event):
        # 在窗口关闭时执行的操作
        if self.client_socket:
            self.client_socket.send("closeme".encode())
            self.client_socket.close()  # 关闭socket
        event.accept()





    def helpActionTriggered(self):
        QMessageBox.information(self, 'help', 'this is help context')

    def contactActionTriggered(self):
        QMessageBox.information(self, 'contact us', 'this is contact us text')