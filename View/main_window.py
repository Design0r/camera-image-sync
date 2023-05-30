from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QListView, QFileDialog, QLineEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Signal


class MainWindow(QMainWindow):

    add_folder_signal = Signal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def init_ui(self):
        self.setFixedSize(400, 500)
        self.setWindowTitle("Camera Image Sync")

        # ========================= Add Widgets =========================
        widget = QWidget(self)
        main_layout = QVBoxLayout()

        source_folder_label = QLabel("Source Folders")
        target_folder_label = QLabel("Target Folder")

        self.list_view = QListView()

        target_folder_line = QLineEdit("D:\Daten\Bilder\Lumix G70")

        add_folder_btn = QPushButton("Add Folder")
        self.images_found_label = QLabel("Images Found: 0")
        self.unsynced_images_label = QLabel("Unsynced Images Found: 0")

        font = QFont()

        # ========================= Set Widget Properties =========================
        widget.setFixedSize(400, 500)
        widget.setLayout(main_layout)

        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        source_folder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        target_folder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.images_found_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.unsynced_images_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font.setPointSize(16)
        self.images_found_label.setFont(font)
        source_folder_label.setFont(font)
        target_folder_label.setFont(font)

        # ========================= Connect Button Events =========================
        add_folder_btn.clicked.connect(self.add_folder)

        # ========================= Add Widgets to Layout =========================
        main_layout.addWidget(source_folder_label)
        main_layout.addWidget(add_folder_btn)
        main_layout.addWidget(self.list_view)
        main_layout.addWidget(self.images_found_label)
        main_layout.addWidget(self.unsynced_images_label)
        main_layout.addWidget(target_folder_label)
        main_layout.addWidget(target_folder_line)

        self.show()

    def add_folder(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.add_folder_signal.emit(folder)

    def update_images_label(self, new_data):
        self.images_found_label.setText(f"Images found: {new_data}")

    def update_unsynced_images_label(self, new_data):
        self.unsynced_images_label.setText(f"Images found: {new_data}")
