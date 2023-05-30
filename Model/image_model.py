from PySide6.QtCore import Signal, QObject


class ImageModel(QObject):
    images_changed = Signal(str)
    unsynced_images_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self._images = []
        self._unsynced_images = []

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        self._images = value
        self.images_changed.emit(len(self.images))

    @property
    def unsynced_images(self):
        return self._unsynced_images

    @unsynced_images.setter
    def unsynced_images(self, value):
        self._unsynced_images = value
        self.unsynced_images_changed.emit(len(self.unsynced_images))
