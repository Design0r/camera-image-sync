import sys
from PySide6.QtWidgets import QApplication
from view import MainWindow
from model import Model
from controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainWindow()
    model = Model()
    controller = Controller(model, view)

    controller.show_ui()

    sys.exit(app.exec())
