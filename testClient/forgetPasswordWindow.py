from PyQt5 import QtWidgets, uic

class ForgetPasswordWindow(QtWidgets.QDialog):
    def __init__(self, client_socket):
        super(ForgetPasswordWindow, self).__init__()
        uic.loadUi('forget/widget.ui', self)  # 加载忘记密码窗口的UI文件

        # 加载样式表
        try:
            with open("forget/res/qss/style-1.qss", "r", encoding="utf-8") as file:
                self.setStyleSheet(file.read())
        except Exception as e:
            print(f"Error loading stylesheet for forget password window: {e}")
