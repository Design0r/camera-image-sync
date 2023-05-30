import sys
from PySide6.QtWidgets import QApplication
from View.main_window import MainWindow
from Model.folder_model import FolderModel
from Model.image_model import ImageModel
from Controller.controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)

    folder_model = FolderModel()
    image_model = ImageModel()
    view = MainWindow()
    controller = Controller(folder_model, image_model, view)

    controller.show_ui()

    sys.exit(app.exec())
