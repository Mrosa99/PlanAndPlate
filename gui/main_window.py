import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.login_window import Ui_login_window


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login_window()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
