from PySide6.QtCore import QAbstractListModel, Qt


class FolderModel(QAbstractListModel):
    def __init__(self) -> None:
        self.folders = []
        super().__init__()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            text = self.folders[index.row()]
            # Return the todo text only.
            return text

    def rowCount(self, index):
        return len(self.folders)
