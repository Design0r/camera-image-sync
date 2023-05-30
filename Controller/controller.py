import os
import pathlib
import datetime
import shutil
from time import ctime


class Controller:

    image_types = [".jpg", ".jpeg", ".png", ".rw2"]

    def __init__(self, folder_model, image_model, view) -> None:
        self.folder_model = folder_model
        self.image_model = image_model
        self.view = view

    def show_ui(self):
        self.view.init_ui()

        self.view.list_view.setModel(self.folder_model)
        self.view.add_folder_signal.connect(self.add_folder)
        self.view.copy_images_signal.connect(self.copy_images)
        self.image_model.images_changed.connect(self.view.update_images_label)

    def add_folder(self, folder: str) -> None:
        if not folder:
            return

        self.folder_model.folders.append(folder)
        self.folder_model.layoutChanged.emit()
        self.get_image_count()

    def get_image_count(self):
        all_files = []

        for folder in self.folder_model.folders:
            if not os.path.exists(folder):
                return

            files = [os.path.join(path, file) for path, _, files in os.walk(folder) for file in files if pathlib.Path(os.path.join(path, file)).suffix in self.image_types]
            all_files += files

        self.image_model.images = all_files, []

    def copy_images(self, target_path, date_format):
        for idx, image in enumerate(self.image_model.images[0]):

            c_time = os.path.getctime(image)
            c_time = datetime.datetime.fromtimestamp(c_time)
            c_time = self.format_date(date_format, c_time)

            existing_folder = self.check_date(c_time, target_path)

            print(existing_folder)

            if existing_folder:
                if os.path.exists(existing_folder):
                    shutil.copy2(image, existing_folder)
                    print("copying", image, "to", existing_folder)
            else:
                target_folder = os.path.join(target_path, c_time)
                os.mkdir(target_folder)
                print("creating folder", c_time)
                shutil.copy2(image, target_folder)
                print("copying", image, "to", target_folder)

            self.view.update_progress_label(int(((idx + 1) / len(self.image_model.images[0])) * 100))

    def check_date(self, date, target_path):
        for folder in os.listdir(target_path):
            if date in folder:
                return os.path.join(target_path, folder)

    def format_date(self, input_format, date):

        spacing = "_"
        if "-" in input_format:
            spacing = "-"
        elif "_" in input_format:
            spacing = "_"

        split_format = input_format.split(spacing)
        for i in split_format:
            if "Y" in i.upper():
                year_format = i
            else:
                year_format = "YY"

        if year_format.upper() == "YYYY":
            year_replace = "%Y"
        elif year_format.upper() == "YY":
            year_replace = "%y"

        formatted_date = date.strftime(input_format.replace(year_format, year_replace).replace("MM", "%m").replace("DD", "%d"))
        return formatted_date
