from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenuBar


class MenuBarWidget(QMenuBar):
    def __init__(self):
        super().__init__()

        self.__create_file_menu()
        self.__create_help_menu()

    def __create_file_menu(self):
        self.file_menu = self.addMenu("Archivo")
        self.import_menu = self.file_menu.addMenu(
            QIcon.fromTheme("document-import"), "Importar"
        )
        self.raw_import_action = self.import_menu.addAction(
            QIcon.fromTheme("document-import"), "Dataset"
        )
        self.train_import_action = self.import_menu.addAction(
            QIcon.fromTheme("document-import"), "Dataset de entramiento"
        )
        self.test_import_action = self.import_menu.addAction(
            QIcon.fromTheme("document-import"), "Dataset de prueba"
        )
        self.validation_import_action = self.import_menu.addAction(
            QIcon.fromTheme("document-import"), "Dataset de validación"
        )

        self.exit_action = self.file_menu.addAction(
            QIcon.fromTheme("window-close"), "Salir"
        )

    def __create_help_menu(self):
        self.help_menu = self.addMenu("Ayuda")
        self.about_action = self.help_menu.addAction("Acerca")
