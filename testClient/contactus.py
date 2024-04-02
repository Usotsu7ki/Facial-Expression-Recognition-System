from PyQt5 import QtWidgets, uic

import global_settings


class ContactUsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ContactUsDialog, self).__init__(parent)
        uic.loadUi('contactUs/dialog.ui', self)

        try:
            with open(global_settings.contactus_style_path, "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Error loading stylesheet in ContactUsDialog: {e}")

        self.pushButton.clicked.connect(self.close)

        # self.btn_1.clicked.connect(self.changeStyleToStarrySky)
        # self.btn_2.clicked.connect(self.changeStyleToSea)
        # self.btn_3.clicked.connect(self.changeStyleToDesert)
        # self.btn_4.clicked.connect(self.changeStyleToGrassland)


    def applyStyleSheet(self, styleSheetPath):
        try:
            with open(styleSheetPath, "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet: {e}")


