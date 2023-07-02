from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
    QListView,
    QFileDialog,
    QLineEdit,
    QProgressBar,
    QHBoxLayout,
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, Signal, QSize
from View.separator import Separator
from View.style import style_sheet
from info import NAME, VERSION
import os
import pathlib


class MainWindow(QMainWindow):
    add_folder_signal = Signal(str)
    remove_folder_signal = Signal(int)
    copy_images_signal = Signal((str, str))
    target_path_edit_signal = Signal(str)
    date_format_edit_signal = Signal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def init_ui(self):
        current_dir = pathlib.Path(__file__).absolute().parent.parent
        icon_path = os.path.join(current_dir, "Ressources", "icon.png")
        folder_path = os.path.join(current_dir, "Ressources", "folder.png")

        # ========================= Add Widgets =========================
        widget = QWidget(self)
        main_layout = QVBoxLayout()

        source_folder_label = QLabel("Source Folders")
        target_folder_label = QLabel("Target Folder")
        date_format_label = QLabel("Date Format")

        self.list_view = QListView()

        self.target_folder_edit = QLineEdit()
        self.date_format_edit = QLineEdit()

        add_folder_btn = QPushButton("Add Folder")
        remove_folder_btn = QPushButton("Remove Folder")
        browse_target_folder = QPushButton(QIcon(folder_path), "")

        browse_target_folder_widget = QWidget()
        browse_target_folder_layout = QHBoxLayout()
        button_widget = QWidget()
        button_layout = QHBoxLayout()

        self.images_found_label = QLabel("Images found: 0 - Synced: 0")

        copy_images_btn = QPushButton("Copy Images")

        self.progress_bar = QProgressBar()

        font = QFont()

        # ========================= Set Widget Properties =========================
        self.setFixedSize(400, 500)
        self.setWindowTitle(f"{NAME} - {VERSION}")
        self.setWindowIcon(QIcon(icon_path))
        self.setStyleSheet(style_sheet)

        widget.setFixedSize(400, 500)
        widget.setLayout(main_layout)

        button_widget.setLayout(button_layout)
        button_layout.setSpacing(70)
        add_folder_btn.setFixedWidth(100)
        remove_folder_btn.setFixedWidth(100)

        self.target_folder_edit.setFixedHeight(30)
        browse_target_folder.setIconSize(QSize(30, 30))
        browse_target_folder.setFixedSize(30, 30)
        browse_target_folder_widget.setLayout(browse_target_folder_layout)
        browse_target_folder_layout.setContentsMargins(0, 0, 0, 0)

        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        remove_folder_btn.clicked.connect(self.remove_folder)
        copy_images_btn.clicked.connect(self.copy_images)
        browse_target_folder.clicked.connect(self.browse_target_folder)

        self.target_folder_edit.textChanged.connect(self.target_folder_changed)
        self.date_format_edit.textChanged.connect(self.date_format_changed)

        # ========================= Add Widgets to Layout =========================
        button_layout.addWidget(add_folder_btn)
        button_layout.addWidget(remove_folder_btn)

        browse_target_folder_layout.addWidget(self.target_folder_edit)
        browse_target_folder_layout.addWidget(browse_target_folder)

        main_layout.addWidget(source_folder_label)
        main_layout.addWidget(button_widget)
        main_layout.addWidget(self.list_view)
        main_layout.addWidget(self.images_found_label)
        main_layout.addWidget(Separator())
        main_layout.addWidget(target_folder_label)
        main_layout.addWidget(browse_target_folder_widget)
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

    def remove_folder(self):
        row = self.list_view.selectedIndexes()
        if len(row) == 0:
            return
        row = row[0].row()
        self.remove_folder_signal.emit(row)

    def update_images_label(self, images, unsynced):
        self.images_found_label.setText(f"Images found: {images} - Synced: {unsynced}")

    def copy_images(self):
        self.copy_images_signal.emit(
            self.target_folder_edit.text(), self.date_format_edit.text()
        )

    def update_progress_label(self, update):
        self.progress_bar.setValue(int(update))

    def set_date_format(self, date_format):
        self.date_format_edit.setText(date_format)

    def date_format_changed(self):
        self.date_format_edit_signal.emit(self.date_format_edit.text())

    def set_target_folder(self, folder):
        self.target_folder_edit.setText(folder)

    def target_folder_changed(self):
        self.target_path_edit_signal.emit(self.target_folder_edit.text())

    def browse_target_folder(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.target_path_edit_signal.emit(folder)
