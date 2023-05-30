import os
import pathlib


class Controller:

    image_types = [".jpg", ".jpeg", ".png", ".rw2"]

    def __init__(self, folder_model, image_model, view) -> None:
        self.folder_model = folder_model
        self.image_model = image_model
        self.view = view

        self.view.add_folder_signal.connect(self.add_folder)
        self.image_model.images_changed.connect(self.view.update_images_label)
        self.image_model.unsynced_images_changed.connect(self.view.update_unsynced_images_label)

    def show_ui(self):
        self.view.init_ui()
        self.view.list_view.setModel(self.folder_model)

    def add_folder(self, folder: str) -> None:
        if not folder:
            return

        self.folder_model.folders.append(folder)
        self.folder_model.layoutChanged.emit()
        print(self.folder_model.folders)
        self.get_image_count()

    def get_image_count(self):
        all_files = []

        for folder in self.folder_model.folders:
            if not os.path.exists(folder):
                return

            files = [file for path, _, files in os.walk(folder) for file in files if pathlib.Path(os.path.join(path, file)).suffix in self.image_types]
            all_files += files

        self.image_model.images = all_files
        # self.image_model.unsynced_images = set(all_files)
