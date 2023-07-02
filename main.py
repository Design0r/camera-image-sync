import sys
from PySide6.QtWidgets import QApplication
from View.main_window import MainWindow
from Model.model import Model
from Controller.controller import Controller

VERSION = "1.0.1"
NAME = "Camera Image Sync"


if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = Model()
    view = MainWindow()
    controller = Controller(model, view)

    controller.show_ui()

    sys.exit(app.exec())
