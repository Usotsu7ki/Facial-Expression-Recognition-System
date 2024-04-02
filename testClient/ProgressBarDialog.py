from PyQt5 import QtWidgets, uic

class ProgressBarDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ProgressBarDialog, self).__init__(parent)
        uic.loadUi('testProgress\dialog.ui', self)
        self.progressBar.setValue(0)  # init the bar value 0(leftest)

    def updateProgress(self, value):
        self.progressBar.setValue(value)
        QtWidgets.QApplication.processEvents()  # update the bar