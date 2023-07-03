from PySide6.QtCore import QAbstractListModel, Qt, Signal


class ListModel(QAbstractListModel):
    images_changed = Signal((int, int))
    date_format_changed = Signal(str)
    target_path_changed = Signal(str)

    def __init__(self) -> None:
        self.folders = []
        self._date_format = ""
        self._target_path = ""
        self._images = []
        self._unsynced_images = []
        super().__init__()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            text = self.folders[index.row()]
            # Return the todo text only.
            return text

    def rowCount(self, index):
        return len(self.folders)

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        self._images = value
        self.images_changed.emit(len(self._images), len(self._unsynced_images))

    @property
    def unsynced_images(self):
        return self._unsynced_images

    @unsynced_images.setter
    def unsynced_images(self, value):
        self._unsynced_images = value
        self.images_changed.emit(len(self._images), len(self._unsynced_images))

    @property
    def date_format(self):
        return self._date_format

    @date_format.setter
    def date_format(self, value):
        self._date_format = value
        self.date_format_changed.emit(value)

    @property
    def target_path(self):
        return self._target_path

    @target_path.setter
    def target_path(self, value):
        self._target_path = value
        self.target_path_changed.emit(value)
