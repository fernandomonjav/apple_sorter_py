from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QGridLayout,
    QGroupBox,
    QHeaderView,
    QLabel,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class VisualizeView(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.explore_box = QGroupBox()
        self.explore_layout = QGridLayout()
        self.explore_box.setLayout(self.explore_layout)

        self.image_table = QTableView()
        self.image_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.explore_layout.addWidget(self.image_table, 0, 0, 1, 4)

        self.open_button = QPushButton("Examinar")
        self.explore_layout.addWidget(self.open_button, 1, 0, 1, 4)

        self.preview_box = QGroupBox("Vista previa")
        self.preview_layout = QGridLayout()
        self.preview_box.setLayout(self.preview_layout)

        self.image_preview = QLabel()
        self.image_preview.setFixedSize(
            self.preview_box.width() / 2, self.preview_box.width() / 2
        )
        self.preview_layout.addWidget(self.image_preview, 0, 0, 4, 4, Qt.AlignCenter)

        self.predict_button = QPushButton("Predecir")
        self.preview_layout.addWidget(self.predict_button, 4, 0, 1, 4)

        self.grid_layout.addWidget(self.explore_box, 0, 0, 1, 6)
        self.grid_layout.addWidget(self.preview_box, 0, 6, 1, 2)
