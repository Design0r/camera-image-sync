import os
import pathlib


class Model:
    def __init__(self) -> None:
        self.image_types = [".jpg", ".jpeg", ".png", ".rw2"]
        self.images = None

    def get_image_count(self, folders):
        all_images = []

        for folder in folders:
            if not os.path.exists(folder):
                return

            images = [file for path, _, files in os.walk(folder) for file in files if pathlib.Path(os.path.join(path, file)).suffix in self.image_types]
            all_images += images

        self.images = set(all_images)
        return len(set(all_images)), 0
