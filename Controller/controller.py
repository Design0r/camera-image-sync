import datetime
import json
import os
import pathlib
import shutil

from Model.model import ListModel
from View.main_window import MainWindow


class MainController:
    image_types = [".jpg", ".jpeg", ".png", ".rw2"]
    DEFAULT_DATE_FORMAT = "YY_MM_DD"
    DEFAULT_PATH = "Path/To/PhotoLibrary"

    def __init__(self, model: ListModel, view: MainWindow) -> None:
        self.model = model
        self.view = view

    def show_ui(self):
        self.view.init_ui()

        self.view.list_view.setModel(self.model)
        self.view.add_folder_signal.connect(self.add_folder)
        self.view.remove_folder_signal.connect(self.remove_folder)
        self.view.copy_images_signal.connect(self.copy_images)
        self.view.target_path_edit_signal.connect(self.set_target_path)
        self.view.date_format_edit_signal.connect(self.set_date_format)

        self.model.images_changed.connect(self.view.update_images_label)
        self.model.target_path_changed.connect(self.view.set_target_folder)
        self.model.date_format_changed.connect(self.view.set_date_format)

        self.load_config()

    def add_folder(self, folder: str) -> None:
        if not folder:
            return

        self.model.folders.append(folder)
        self.model.layoutChanged.emit()
        self.get_image_count()
        self.save_config()

    def remove_folder(self, index: int) -> None:
        if not index:
            return
        self.model.folders.pop(index)
        self.model.layoutChanged.emit()
        self.get_image_count()
        self.save_config()

    def get_image_count(self):
        all_files: list[str] = []

        for folder in self.model.folders:
            if not os.path.exists(folder):
                return

            files = [
                os.path.join(path, file)
                for path, _, files in os.walk(folder)
                for file in files
                if pathlib.Path(path, file).suffix.lower() in self.image_types
            ]
            all_files += files

        self.model.images = all_files
        self.check_unsynced()

    def check_unsynced(self):
        unsynced_images: list[str] = []
        for image in self.model.images:
            c_time = self.get_creation_time(image)
            existing_folder = self.check_date(c_time, self.model.target_path)
            if not existing_folder:
                return

            folder_content = os.listdir(existing_folder)

            for file in folder_content:
                if os.path.basename(image) == file:
                    unsynced_images.append(file)

        self.model.unsynced_images = unsynced_images

    def copy_images(self):
        for idx, image in enumerate(self.model.images):
            c_time = self.get_creation_time(image)
            existing_folder = self.check_date(c_time, self.model.target_path)

            if existing_folder:
                if os.path.exists(existing_folder):
                    shutil.copy2(image, existing_folder)
                    print("copying", image, "to", existing_folder)
            else:
                target_folder = os.path.join(self.model.target_path, c_time)
                os.mkdir(target_folder)
                print("creating folder", c_time)
                shutil.copy2(image, target_folder)
                print("copying", image, "to", target_folder)

            self.view.update_progress_label(
                int(((idx + 1) / len(self.model.images)) * 100)
            )
        self.get_image_count()

    def get_creation_time(self, image: str):
        c_time = os.path.getctime(image)
        c_time = datetime.datetime.fromtimestamp(c_time)
        c_time = self.format_date(self.model.date_format, c_time)
        return c_time

    def check_date(self, date: str, target_path: str):
        if not os.path.exists(target_path):
            return
        for folder in os.listdir(target_path):
            if date in folder:
                return os.path.join(target_path, folder)

    def format_date(self, input_format: str, date: datetime.datetime):
        spacing = "_"
        if "-" in input_format:
            spacing = "-"
        elif "_" in input_format:
            spacing = "_"

        year_format = "YY"

        split_format = input_format.split(spacing)
        for i in split_format:
            if "Y" in i.upper():
                year_format = i
                break

            year_format = "YY"

        year_replace = "%y"
        if year_format.upper() == "YYYY":
            year_replace = "%Y"
        elif year_format.upper() == "YY":
            year_replace = "%y"

        formatted_date = date.strftime(
            input_format.replace(year_format, year_replace)
            .replace("MM", "%m")
            .replace("DD", "%d")
        )
        return formatted_date

    def set_target_path(self, path: str):
        if not os.path.exists(path):
            return
        self.model.target_path = path
        self.get_image_count()
        self.save_config()

    def set_date_format(self, date_format: str):
        self.model.date_format = date_format
        try:
            self.get_image_count()
            self.save_config()
        except Exception:
            pass

    def load_config(self):
        try:
            with open("config.json", "r", encoding="utf-8") as file:
                config_data = json.load(file)
                self.image_types = (
                    config_data["image_types"]
                    if config_data["image_types"] != ""
                    else self.image_types
                )
                self.model.folders = config_data["source_folders"]
                self.model.date_format = (
                    config_data["date_format"]
                    if config_data["date_format"] != ""
                    else self.DEFAULT_DATE_FORMAT
                )
                self.model.target_path = (
                    config_data["target_path"]
                    if config_data["target_path"] != ""
                    else self.DEFAULT_PATH
                )

                self.get_image_count()
                print("Config Loaded")
        except Exception as error:
            print(f"Error Loading Config: {error}")
            print("Trying to create new Config...")
            try:
                self.save_config()
                self.load_config()
            except Exception as error2:
                print(f"Error creating Config: {error2}")

    def save_config(self):
        with open("config.json", "w", encoding="utf-8") as file:
            data = {
                "source_folders": self.model.folders,
                "date_format": self.model.date_format,
                "target_path": self.model.target_path
                if self.model.target_path
                else self.DEFAULT_PATH,
                "image_types": self.image_types,
            }
            json.dump(data, file, indent=4)
        print("Config Saved")
