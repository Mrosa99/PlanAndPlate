from PySide6.QtWidgets import QMainWindow, QApplication
from ui.login_window import Ui_PlanAndPlate


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PlanAndPlate()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
