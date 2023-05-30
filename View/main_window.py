from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QListView, QFileDialog, QLineEdit, QProgressBar
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Signal
from View.separator import Separator
from View.style import style_sheet


class MainWindow(QMainWindow):

    add_folder_signal = Signal(str)
    copy_images_signal = Signal((str, str))

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
        date_format_label = QLabel("Date Format")

        self.list_view = QListView()

        self.target_folder_edit = QLineEdit(r"D:\Daten\Bilder\Lumix G70")
        self.date_format_edit = QLineEdit("YY_MM_DD")

        add_folder_btn = QPushButton("Add Folder")
        self.images_found_label = QLabel("Images found: 0 - Unsynced: 0")

        copy_images_btn = QPushButton("Copy Images")

        self.progress_bar = QProgressBar()

        font = QFont()

        # ========================= Set Widget Properties =========================
        widget.setFixedSize(400, 500)
        widget.setLayout(main_layout)
        self.setStyleSheet(style_sheet)

        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        source_folder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        target_folder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.images_found_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        date_format_label.setAlignment(Qt.AlignCenter)

        font.setPointSize(13)
        source_folder_label.setFont(font)
        target_folder_label.setFont(font)
        date_format_label.setFont(font)

        # ========================= Connect Button Events =========================
        add_folder_btn.clicked.connect(self.add_folder)
        copy_images_btn.clicked.connect(self.copy_images)

        # ========================= Add Widgets to Layout =========================
        main_layout.addWidget(source_folder_label)
        main_layout.addWidget(add_folder_btn)
        main_layout.addWidget(self.list_view)
        main_layout.addWidget(self.images_found_label)
        main_layout.addWidget(Separator())
        main_layout.addWidget(target_folder_label)
        main_layout.addWidget(self.target_folder_edit)
        main_layout.addWidget(Separator())
        main_layout.addWidget(date_format_label)
        main_layout.addWidget(self.date_format_edit)
        main_layout.addWidget(Separator())
        main_layout.addWidget(copy_images_btn)
        main_layout.addWidget(self.progress_bar)

        self.show()

    def add_folder(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.add_folder_signal.emit(folder)

    def update_images_label(self, images, unsynced):
        self.images_found_label.setText(f"Images found: {images} - Unsynced: {unsynced}")

    def copy_images(self):
        self.copy_images_signal.emit(self.target_folder_edit.text(), self.date_format_edit.text())

    def update_progress_label(self, update):
        self.progress_bar.setValue(int(update))
