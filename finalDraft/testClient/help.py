from PyQt5 import QtWidgets, uic

class HelpDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(HelpDialog, self).__init__(parent)
        uic.loadUi('help\dialog.ui', self)

        try:
            with open(r"help\qss\style.qss", "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Error loading stylesheet in HelpDialog: {e}")

        self.pushButton.clicked.connect(self.close)
