import csv
from controllers.visualize_controller import VisualizeController
from ui.views.visualize.visualize_view import VisualizeView
from controllers.preprocess_controller import PreprocessController
from ui.views.preprocess.preprocess_view import PreprocessView
from models.dataframe import DataFrame
from models.model import Model
from PyQt5.QtWidgets import QAction, QFileDialog, QMainWindow, QStackedWidget
import pandas as pd
from ui.widgets.tool_bar_widget import ToolBarWidget
from ui.widgets.menu_bar_widget import MenuBarWidget
from ui.views.classify.classify_view import ClassifyView
from controllers.classify_controller import ClassifyController
from controllers.home_controller import HomeController
from ui.views.home.home_view import HomeView


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.app = app

        self.model = Model()

        self.menu_bar = MenuBarWidget()
        self.setMenuBar(self.menu_bar)

        self.tool_bar = ToolBarWidget()
        self.addToolBar(self.tool_bar)

        self.stacked = QStackedWidget()

        self.home_view = HomeView()
        self.home_controller = HomeController(self.home_view)
        self.stacked.addWidget(self.home_view)

        self.preprocess_view = PreprocessView()
        self.preprocess_controller = PreprocessController(
            self.preprocess_view, self.model
        )
        self.stacked.addWidget(self.preprocess_view)

        self.classify_view = ClassifyView()
        self.classify_controller = ClassifyController(self.classify_view, self.model)
        self.stacked.addWidget(self.classify_view)

        self.visualize_view = VisualizeView()
        self.visualize_controller = VisualizeController(self.visualize_view, self.model)
        self.stacked.addWidget(self.visualize_view)

        self.menu_bar.raw_import_action.triggered.connect(self.import_raw_df_by_csv)
        self.menu_bar.train_import_action.triggered.connect(self.import_train_df_by_csv)
        self.menu_bar.test_import_action.triggered.connect(self.import_test_df_by_csv)
        self.menu_bar.validation_import_action.triggered.connect(
            self.import_validation_df_by_csv
        )
        self.menu_bar.exit_action.triggered.connect(self.exit_action_triggered)

        self.tool_bar.raw_import_action.triggered.connect(self.import_raw_df_by_csv)
        self.tool_bar.train_import_action.triggered.connect(self.import_train_df_by_csv)
        self.tool_bar.test_import_action.triggered.connect(self.import_test_df_by_csv)
        self.tool_bar.validation_import_action.triggered.connect(
            self.import_validation_df_by_csv
        )
        self.tool_bar.raw_save_action.triggered.connect(self.save_raw_clicked)
        self.tool_bar.train_save_action.triggered.connect(self.save_test_clicked)
        self.tool_bar.test_save_action.triggered.connect(self.save_validation_clicked)
        self.tool_bar.validation_save_action.triggered.connect(
            self.import_validation_df_by_csv
        )

        self.tool_bar.tab_actions.triggered.connect(self.tab_actions_triggered)

        self.setCentralWidget(self.stacked)
        self.setMinimumSize(1080, 480)

    # Import dataframe by csv
    # Importar dataframe por csv
    def import_df_by_csv(self):
        filename, filter = QFileDialog.getOpenFileName(filter="csv(*.csv)")
        if filter != "csv(*.csv)":
            return None
        return DataFrame(pd.read_csv(filename))

    # Import train dataframe by csv
    # Importar dataframe de entrenamiento por csv
    def import_raw_df_by_csv(self):
        df = self.import_df_by_csv()
        df.set_class_index(len(df.columns) - 1)
        self.model.set_raw_df(df)

    # Import train dataframe by csv
    # Importar dataframe de entrenamiento por csv
    def import_train_df_by_csv(self):
        df = self.import_df_by_csv()
        df.set_class_index(len(df.columns) - 1)
        self.model.set_train_df(df)

    # Import test dataframe by csv
    # Importar dataframe de prueba por csv
    def import_test_df_by_csv(self):
        df = self.import_df_by_csv()
        df.set_class_index(len(df.columns) - 1)
        self.model.set_test_df(df)

    # Import validation dataframe by csv
    # Importar dataframe de validación por csv
    def import_validation_df_by_csv(self):
        df = self.import_df_by_csv()
        self.model.set_validation_df(df)

    # Guardar extracción de características en  csv
    def save_raw_clicked(self):
        filename, filter = QFileDialog.getSaveFileName(filter="csv(*.csv)")

        if filter != "csv(*.csv)":
            return

        writer = csv.writer(
            open(
                filename,
                mode="w",
            )
        )

        raw_df = self.model.get_raw_df()

        writer.writerow(raw_df.columns.tolist())

        for x in raw_df.values.tolist():
            for y in x:
                writer.writerow(y)

    # Guardar extracción de características en  csv
    def save_test_clicked(self):
        filename, filter = QFileDialog.getSaveFileName(filter="csv(*.csv)")

        if filter != "csv(*.csv)":
            return

        writer = csv.writer(
            open(
                filename,
                mode="w",
            )
        )

        test_df = self.model.get_test_df()

        writer.writerow(test_df.columns.tolist())

        for x in test_df.values.tolist():
            for y in x:
                writer.writerow(y)

    # Guardar extracción de características en  csv
    def save_validation_clicked(self):
        filename, filter = QFileDialog.getSaveFileName(filter="csv(*.csv)")

        if filter != "csv(*.csv)":
            return

        writer = csv.writer(
            open(
                filename,
                mode="w",
            )
        )

        validation_df = self.model.get_validation_df()

        writer.writerow(validation_df.columns.tolist())

        for x in validation_df.values.tolist():
            for y in x:
                writer.writerow(y)

    def exit_action_triggered(self):
        self.app.quit()

    def tab_actions_triggered(self, action: QAction):
        id = action.property("id")

        if id == "home":
            view = self.home_view
        elif id == "preprocess":
            view = self.preprocess_view
        elif id == "classify":
            view = self.classify_view
        elif id == "visualize":
            view = self.visualize_view
        else:
            view = self.home_view

        self.stacked.setCurrentWidget(view)

        action.setCheckable(True)
