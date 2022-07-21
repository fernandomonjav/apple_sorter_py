from PyQt5.QtWidgets import (
    QCheckBox,
    QComboBox,
    QGridLayout,
    QGroupBox,
    QPushButton,
    QWidget,
)


class PreprocessView(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.create_features_box()
        self.create_dataset_box()
        self.create_filters_box()

    def create_features_box(self):
        # Caja de características
        self.features_box = QGroupBox("Características")
        self.features_layout = QGridLayout()
        self.features_box.setLayout(self.features_layout)

        # Combobox de tipos de manzanas
        self.label_combobox = QComboBox()
        self.features_layout.addWidget(self.label_combobox, 0, 0, 1, 3)

        # Botón para examinar manzanas
        self.examine_button = QPushButton("Examinar")
        self.features_layout.addWidget(self.examine_button, 0, 3)

        # Botón para extraer características de manzanas
        self.extract_button = QPushButton("Extraer")
        self.features_layout.addWidget(self.extract_button, 1, 0, 1, 2)

        # Botón para extraer características de manzanas
        self.save_button = QPushButton("Guardar")
        self.features_layout.addWidget(self.save_button, 1, 2, 1, 2)

        self.grid_layout.addWidget(self.features_box)

    def create_dataset_box(self):
        # Caja de dataset
        self.dataset_box = QGroupBox("Dataset")
        self.dataset_layout = QGridLayout()
        self.dataset_box.setLayout(self.dataset_layout)

        self.split_button = QPushButton("Dividir")
        self.dataset_layout.addWidget(self.split_button, 0, 0, 1, 3)

        self.grid_layout.addWidget(self.dataset_box)

    def create_filters_box(self):
        # Caja de filtros
        self.filters_box = QGroupBox("Filtros")
        self.filters_layout = QGridLayout()
        self.filters_box.setLayout(self.filters_layout)

        self.normalize_checkbox = QCheckBox("Normalizar")
        self.filters_layout.addWidget(self.normalize_checkbox, 0, 0, 1, 3)

        # Botón para aplicar filtros
        self.apply_filters_button = QPushButton("Aplicar")
        self.filters_layout.addWidget(self.apply_filters_button, 1, 0, 1, 3)

        self.grid_layout.addWidget(self.filters_box)
