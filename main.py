import sys
from PySide6.QtWidgets import QApplication
from View import MainWindow
from Model import ListModel
from Controller import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = ListModel()
    view = MainWindow()
    controller = MainController(model, view)

    controller.show_ui()

    sys.exit(app.exec())
