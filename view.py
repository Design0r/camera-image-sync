from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QListWidget, QFileDialog, QListWidgetItem, QLineEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from functools import partial


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        self.controller = None
        super().__init__(parent)

    def set_controller(self, controller):
        self.controller = controller

    def init_ui(self):
        self.setFixedSize(400, 500)
        self.setWindowTitle("Camera Image Sync")

        # Add Widgets
        widget = QWidget(self)
        main_layout = QVBoxLayout()

        source_folder_label = QLabel("Source Folders")
        target_folder_label = QLabel("Target Folder")

        list_view = QListWidget()

        target_folder_line = QLineEdit("D:\Daten\Bilder\Lumix G70")

        add_folder_btn = QPushButton("Add Folder")
        images_found_label = QLabel("Images Found: 0")
        unsynced_images_label = QLabel("Unsynced Images Found: 0")

        # Set Widget Properties
        font = QFont()

        images_found_label.setFont(font)

        font.setPointSize(16)

        widget.setFixedSize(400, 500)
        widget.setLayout(main_layout)

        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        source_folder_label.setFont(font)
        target_folder_label.setFont(font)
        source_folder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        target_folder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        images_found_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        unsynced_images_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        add_folder_btn.clicked.connect(partial(self.add_folder, list_view, images_found_label, unsynced_images_label))

        # Add Widgets to Layout
        main_layout.addWidget(source_folder_label)
        main_layout.addWidget(add_folder_btn)
        main_layout.addWidget(list_view)
        main_layout.addWidget(images_found_label)
        main_layout.addWidget(unsynced_images_label)
        main_layout.addWidget(target_folder_label)
        main_layout.addWidget(target_folder_line)
        self.show()

    def add_folder(self, list_view: QListWidget, images_found_label: QLabel, unsynced_images_label: QLabel):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        QListWidgetItem(folder, list_view)

        all_list_items = [list_view.item(index).text() for index in range(list_view.count())]
        image_count, unsynced_count = self.controller.get_image_count(all_list_items)
        images_found_label.setText(f"Images Found: {image_count}")
        unsynced_images_label.setText(f"Unsynced Images Found: {unsynced_count}")
