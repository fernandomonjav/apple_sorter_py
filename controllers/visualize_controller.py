from PyQt5.QtWidgets import QFileDialog
from models.classifier_table_model import ClassifierTableModel
from PyQt5.QtCore import QItemSelection, Qt
from PyQt5.QtGui import QPixmap
from models.model import Model
from ui.views.visualize.visualize_view import VisualizeView


class VisualizeController:
    def __init__(self, view: VisualizeView, model: Model):
        self.view = view
        self.model = model

        self.images_table_model = ClassifierTableModel(["Ruta de archivo"])

        self.view.image_table.setModel(self.images_table_model)
        self.view.image_table.selectionModel().selectionChanged.connect(self.hello)

        self.view.open_button.clicked.connect(self.open_images_clicked)
        self.view.predict_button.clicked.connect(self.open_images_clicked)

    def open_images_clicked(self):
        filenames, filter = QFileDialog.getOpenFileNames(
            filter="Image files (*.jpg *.png)"
        )

        if filter != "Image files (*.jpg *.png)":
            return

        rows = []

        for filename in filenames:
            rows.append([filename])

        for row in rows:
            self.images_table_model.insert_row(row)

    def hello(self, selected: QItemSelection, deselected: QItemSelection):
        table_view = self.view.image_table
        index = table_view.selectionModel().currentIndex()
        row = index.row()
        name = table_view.model().data(table_view.model().index(row, 0), 0)

        pix_map = QPixmap(name)
        size = self.view.image_preview.size()
        self.view.image_preview.setPixmap(
            pix_map.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
