

class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def show_ui(self):
        self.view.init_ui()

    def get_image_count(self, folders):
        count = self.model.get_image_count(folders)
        return count
