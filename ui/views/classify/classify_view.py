from PyQt5.QtWidgets import (
    QComboBox,
    QGridLayout,
    QGroupBox,
    QHeaderView,
    QPushButton,
    QTableView,
    QTableWidget,
    QWidget,
)


class ClassifyView(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.classifier_combobox = QComboBox()
        self.grid_layout.addWidget(self.classifier_combobox, 0, 0, 1, 4)

        self.run_button = QPushButton("Ejecutar")
        self.grid_layout.addWidget(self.run_button, 0, 4)

        self.option_box = QGroupBox("Opciones")
        self.option_layout = QGridLayout()
        self.option_box.setLayout(self.option_layout)

        self.classifier_table = QTableView()
        self.classifier_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.grid_layout.addWidget(self.classifier_table, 1, 0, 1, 5)
