from models.dataframe import DataFrame
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from models.model import Model
import numpy as np
import pandas as pd
import csv
from ui.views.preprocess.preprocess_view import PreprocessView
from sklearn.preprocessing import MinMaxScaler
import cv2
import mahotas
from PIL import Image, ImageStat
from concurrent.futures import ThreadPoolExecutor

labels = [
    "Apple Braeburn",
    "Apple Golden 3",
    "Apple Granny Smith",
    "Apple Pink Lady",
    "Apple Red Delicious",
]

headers = [
    "hue",
    "saturation",
    "value",
    "brightness",
    "SRE",
    "LRE",
    "GNL",
    "RLNU",
    "RP",
    "LGRE",
    "HGRE",
    "SRLGE",
    "SRHGE",
    "LRLGE",
    "LRHGE",
    "GLV",
    "RLV",
    "label",
]


class PreprocessController:
    def __init__(self, view: PreprocessView, model: Model):
        self.view = view
        self.model = model

        self.filenames = []
        self.rows = []

        for i in range(len(labels)):
            self.filenames.append([])
            self.rows.append([])

        self.view.label_combobox.addItems(labels)

        self.view.examine_button.clicked.connect(self.choose_clicked)
        self.view.extract_button.clicked.connect(self.extract_features_thread)
        self.view.apply_filters_button.clicked.connect(self.apply_extraction)
        self.view.save_button.clicked.connect(self.save_clicked)

        self.view.split_button.clicked.connect(self.split_dataframe)

        # Caja de filtros
        self.view.apply_filters_button.clicked.connect(self.apply_filters)

    def train_validation_test_split(
        self, df: DataFrame, train_percent=0.6, validate_percent=0.2, seed=None
    ):
        np.random.seed(seed)
        perm = np.random.permutation(df.index)
        m = len(df.index)
        train_end = int(train_percent * m)
        validate_end = int(validate_percent * m) + train_end
        train = df.iloc[perm[:train_end]]
        validate = df.iloc[perm[train_end:validate_end]]
        test = df.iloc[perm[validate_end:]]
        return DataFrame(train), DataFrame(validate), DataFrame(test)

    # Dividir dataframe en train, test, validation
    def split_dataframe(self):
        raw_df = self.model.get_raw_df()

        # Si datataframe no existe
        if raw_df is None:
            message_box = QMessageBox()
            message_box.setText("No se ha encontrado un dataset")
            message_box.setInformativeText(
                "Debes importar un dataset para realizar esta acción."
            )
            message_box.exec()
            return

        train_df, validation_df, test_df = self.train_validation_test_split(raw_df)

        train_df.set_class_index(len(train_df.columns) - 1)
        test_df.set_class_index(len(test_df.columns) - 1)

        self.model.set_train_df(train_df)
        self.model.set_test_df(test_df)
        self.model.set_validation_df(validation_df)

    def save_dataframe(self, df: DataFrame):
        filename, filter = QFileDialog.getSaveFileName(filter="csv(*.csv)")

        if filter != "csv(*.csv)":
            return

        writer = csv.writer(
            open(
                filename,
                mode="w",
            )
        )

        writer.writerow(df.columns)

        for x in df.values.tolist():
            for y in x:
                writer.writerow(y)

    def get_values_hsv(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        avg_color_per_row = np.average(hsv, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        return [avg_color[0], avg_color[1], avg_color[2]]

    # Extraer texturas
    def extract_textures(self, img):
        return mahotas.features.haralick(img).mean(axis=0)

    # Extraer brillo
    def extract_brightness(self, image):
        image = Image.fromarray(image)
        image.convert("L")
        stat = ImageStat.Stat(image)
        return stat.rms[0]

    def create_dataset(self, ar):
        writer = csv.writer(
            open(
                "hello.csv",
                mode="w",
            )
        )
        writer.writerow(headers)
        writer.writerow(ar)

    # Normalizar dataframe
    def normalize(self, x):
        scaler = MinMaxScaler(feature_range=(0, 1))
        return scaler.fit_transform(x)

    def choose_clicked(self):
        filenames, filter = QFileDialog.getOpenFileNames(
            filter="Image files (*.jpg *.png)"
        )

        if filter != "Image files (*.jpg *.png)":
            return

        index = self.view.label_combobox.currentIndex()

        self.filenames[index] = filenames

    # Aplicar extracción
    def apply_extraction(self):
        df = pd.DataFrame(self.rows, columns=headers)
        self.model.set_raw_df(DataFrame(df))

    # Guardar extracción de características en  csv
    def save_clicked(self):
        filename, filter = QFileDialog.getSaveFileName(filter="csv(*.csv)")

        if filter != "csv(*.csv)":
            return

        writer = csv.writer(
            open(
                filename,
                mode="w",
            )
        )
        writer.writerow(headers)

        for x in self.rows:
            for y in x:
                writer.writerow(y)

    # Extraer caracteristicas de imagen
    def extract_image_features(self, filename, label):
        image = cv2.imread(filename)
        hsv = self.get_values_hsv(image)
        brightness = self.extract_brightness(image)
        textures = self.extract_textures(image)
        return list(hsv) + [brightness] + list(textures) + [label]

    # Extraer caracteristicas
    def extract_features(self, i):
        for filename in self.filenames[i]:
            row = self.extract_image_features(filename, i)
            self.rows[i].append(row)

    # Extraer caracteristicas  con hilos
    def extract_features_thread(self):

        with ThreadPoolExecutor(max_workers=3) as executer:
            for i in range(len(self.filenames)):
                executer.submit(self.extract_features, i)

    # Aplicar filtros a dataframe
    def apply_filters(self):
        isNormalize = self.view.normalize_checkbox.isChecked()

        raw_df = self.model.get_raw_df()

        # Si datataframe no existe
        if raw_df is None:
            message_box = QMessageBox()
            message_box.setText("No se ha encontrado un dataset")
            message_box.setInformativeText(
                "Debes importar un dataset para realizar esta acción."
            )
            message_box.exec()
            return

        if isNormalize:
            self.normalize(raw_df)
