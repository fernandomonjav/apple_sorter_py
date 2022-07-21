from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QComboBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class HomeView(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout()
        self.grid_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.grid_layout)

        self.info_box = QGroupBox("Información")
        self.info_layout = QFormLayout()
        self.info_box.setLayout(self.info_layout)

        self.train_label = QLabel("Dataset de entramiento:")
        self.train_text = QLabel("No encontrado")
        self.info_layout.addRow(self.train_label, self.train_text)

        self.test_label = QLabel("Dataset de prueba:")
        self.test_text = QLabel("No encontrado")
        self.info_layout.addRow(self.test_label, self.test_text)

        self.validation_label = QLabel("Dataset de validación:")
        self.validation_text = QLabel("No encontrado")
        self.info_layout.addRow(self.validation_label, self.validation_text)

        self.grid_layout.addWidget(self.info_box, 0, 0)

        self.classifier_box = QGroupBox("Clasifador")
        self.classifier_layout = QGridLayout()
        self.classifier_box.setLayout(self.classifier_layout)

        self.classifier_combobox = QComboBox()
        self.classifier_layout.addWidget(self.classifier_combobox, 0, 0, 1, 3)

        self.apply_classifier_combobox = QPushButton("Aplicar")
        self.classifier_layout.addWidget(self.apply_classifier_combobox, 0, 3, 1, 1)

        self.grid_layout.addWidget(self.classifier_box, 0, 1)
