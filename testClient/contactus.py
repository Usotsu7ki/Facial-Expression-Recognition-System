from PyQt5 import QtWidgets, uic

class ContactUsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ContactUsDialog, self).__init__(parent)
        uic.loadUi('contactus\dialog.ui', self)

        try:
            with open(r"contactus\qss\style.qss", "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Error loading stylesheet in ContactUsDialog: {e}")

        self.pushButton.clicked.connect(self.close)
