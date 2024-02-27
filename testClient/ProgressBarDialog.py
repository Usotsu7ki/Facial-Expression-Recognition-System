from PyQt5 import QtWidgets, uic

class ProgressBarDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ProgressBarDialog, self).__init__(parent)
        uic.loadUi('testProgress\dialog.ui', self)  # 确保路径正确
        self.progressBar.setValue(0)  # 初始化进度条为0%

    def update_progress(self, value):
        self.progressBar.setValue(value)
        QtWidgets.QApplication.processEvents()  # 更新界面以及进度条