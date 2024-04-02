import unittest
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication
from testClient.admin_window import AdminWindow


class AdminWindowTests(unittest.TestCase):
    def setUp(self):
        # Create a mock client socket
        self.client_socket = MagicMock()
        # Create a QApplication instance (required for testing PyQt5)
        self.app = QApplication([])

    def test_start_receiving(self):
        admin_window = AdminWindow(self.client_socket)
        # Ensure that the client socket's 'send' method is called
        self.client_socket.send.assert_called_with("message from admin".encode())

    def test_receive_client_list(self):
        admin_window = AdminWindow(self.client_socket)
        # Set up a mock client list
        client_list = "client1\nclient2\nclient3"
        # Simulate receiving the client list from the server
        self.client_socket.recv.return_value = client_list.encode()
        # Call the 'receive_client_list' method
        admin_window.receive_client_list()
        # Verify that the client list is updated in the GUI
        self.assertEqual(admin_window.clientListWidget.count(), 3)

    def test_update_client_list(self):
        admin_window = AdminWindow(self.client_socket)
        # Set up a mock client list
        client_list = ["client1", "client2", "client3"]
        # Call the 'update_client_list' method
        admin_window.update_client_list(client_list)
        # Verify that the client list is updated in the GUI
        self.assertEqual(admin_window.clientListWidget.count(), 3)

    def test_add_client(self):
        admin_window = AdminWindow(self.client_socket)
        # Add a client to the GUI
        admin_window.add_client("client1")
        # Verify that the client is added to the list
        self.assertEqual(admin_window.clientListWidget.count(), 1)
        self.assertEqual(admin_window.clientListWidget.item(0).text(), "client1")

    def test_kickClient(self):
        admin_window = AdminWindow(self.client_socket)
        # Add a client to the GUI
        admin_window.add_client("client1")
        # Select the client in the GUI
        admin_window.clientListWidget.setCurrentRow(0)
        # Call the 'kickClient' method
        admin_window.kickClient()
        # Verify that the client socket's 'send' method is called with the correct message
        self.client_socket.send.assert_called_with("kick:client1".encode())

    def test_sendMessage(self):
        admin_window = AdminWindow(self.client_socket)
        # Add a client to the GUI
        admin_window.add_client("client1")
        # Select the client in the GUI
        admin_window.clientListWidget.setCurrentRow(0)
        # Set up a message in the console text edit
        admin_window.consoleTextEdit.setPlainText("Test message")
        # Call the 'sendMessage' method
        admin_window.sendMessage()
        # Verify that the client socket's 'send' method is called with the correct message
        self.client_socket.send.assert_called_with("sendmessage|client1|Test message".encode())

if __name__ == "__main__":
    unittest.main()