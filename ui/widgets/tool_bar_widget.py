from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QActionGroup,
    QMenu,
    QToolBar,
    QToolButton,
)


class ToolBarWidget(QToolBar):
    def __init__(self):
        super().__init__()

        self.setMovable(False)

        self.home_action = QAction(QIcon.fromTheme("go-home"), "Inicio")
        self.home_action.setProperty("id", "home")
        self.home_action.setCheckable(True)

        self.preprocess_action = QAction(QIcon.fromTheme("adjustlevels"), "Preprocesar")
        self.preprocess_action.setProperty("id", "preprocess")
        self.preprocess_action.setCheckable(True)

        self.classify_action = QAction(QIcon.fromTheme("view-group"), "Clasificar")
        self.classify_action.setProperty("id", "classify")
        self.classify_action.setCheckable(True)

        self.visualize_action = QAction(QIcon.fromTheme("viewimage"), "Visualizar")
        self.visualize_action.setProperty("id", "visualize")
        self.visualize_action.setCheckable(True)

        self.tab_actions = QActionGroup(self)
        self.tab_actions.addAction(self.home_action)
        self.tab_actions.addAction(self.preprocess_action)
        self.tab_actions.addAction(self.classify_action)
        self.tab_actions.addAction(self.visualize_action)

        self.addAction(self.home_action)
        self.addAction(self.preprocess_action)
        self.addAction(self.classify_action)
        self.addAction(self.visualize_action)

        self.addSeparator()

        self.__create_import_menu()
        self.__create_save_menu()

        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

    def __create_import_menu(self):
        self.import_tool_button = QToolButton()
        self.import_tool_button.setPopupMode(QToolButton.InstantPopup)
        self.import_tool_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.import_tool_button.setIcon(QIcon.fromTheme("document-import"))
        self.import_tool_button.setText("Importar")

        self.import_menu = QMenu(self.import_tool_button)

        self.raw_import_action = self.import_menu.addAction(
            QIcon.fromTheme("document-import"), "Dataset sin procesar"
        )
        self.train_import_action = self.import_menu.addAction(
            QIcon.fromTheme("document-import"), "Dataset de entrenamiento"
        )
        self.test_import_action = self.import_menu.addAction(
            QIcon.fromTheme("document-import"), "Dataset de prueba"
        )
        self.validation_import_action = self.import_menu.addAction(
            QIcon.fromTheme("document-import"), "Dataset de validación"
        )

        self.import_tool_button.setMenu(self.import_menu)

        self.addWidget(self.import_tool_button)

    def __create_save_menu(self):
        self.save_tool_button = QToolButton()
        self.save_tool_button.setPopupMode(QToolButton.InstantPopup)
        self.save_tool_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.save_tool_button.setIcon(QIcon.fromTheme("document-save"))
        self.save_tool_button.setText("Guardar")

        self.save_menu = QMenu(self.save_tool_button)

        self.raw_save_action = self.save_menu.addAction(
            QIcon.fromTheme("document-save"), "Dataset sin procesar"
        )
        self.train_save_action = self.save_menu.addAction(
            QIcon.fromTheme("document-save"), "Dataset de entrenamiento"
        )
        self.test_save_action = self.save_menu.addAction(
            QIcon.fromTheme("document-save"), "Dataset de prueba"
        )
        self.validation_save_action = self.save_menu.addAction(
            QIcon.fromTheme("document-save"), "Dataset de validación"
        )

        self.save_tool_button.setMenu(self.save_menu)

        self.addWidget(self.save_tool_button)
