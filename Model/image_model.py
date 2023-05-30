from PySide6.QtCore import Signal, QObject


class ImageModel(QObject):
    images_changed = Signal((int, int))

    def __init__(self):
        super().__init__()
        self._images = []
        self._unsynced_images = []

    @property
    def images(self):
        return self._images, self._unsynced_images

    @images.setter
    def images(self, value):
        self._images, self._unsynced_images = value
        self.images_changed.emit(len(self._images), len(self._unsynced_images))
