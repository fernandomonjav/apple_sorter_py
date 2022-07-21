from PyQt5.QtWidgets import QMessageBox
from models.classifier import Classifier
from models.dataframe import DataFrame
from models.classifier_table_model import ClassifierTableModel
import time
from models.evaluation import Evaluation
from models.model import Model
from ui.views.classify.classify_view import ClassifyView
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


class ClassifyController:
    def __init__(self, view: ClassifyView, model: Model):
        self.view = view
        self.model = model

        self.load_table_models()
        self.load_classifier_options()

        self.view.classifier_combobox.currentIndexChanged.connect(
            self.change_table_header
        )
        self.view.run_button.clicked.connect(self.run_classifier)

        self.change_table_header(0)

    def load_table_models(self):
        general_cols = [
            "Uso de CPU",
            "Tiempo de ejecución",
            "Exactitud",
            "Precisión",
            "Recall",
            "F-Measure",
            "AUC",
        ]
        logistic_regression_cols = ["Algoritmo", *general_cols]
        neural_network_cols = [
            "Algoritmo",
            "Tasa de aprendizaje",
            "Función",
            "Tamaño",
            *general_cols,
        ]
        svm_cols = ["Algoritmo", "Kernel", *general_cols]
        bayesian_cols = ["Algoritmo", "Descripción", *general_cols]
        decision_tree_cols = ["Algoritmo", "Descripción", *general_cols]

        self.table_models = [
            ClassifierTableModel(logistic_regression_cols),
            ClassifierTableModel(neural_network_cols),
            ClassifierTableModel(svm_cols),
            ClassifierTableModel(bayesian_cols),
            ClassifierTableModel(decision_tree_cols),
        ]

    def load_classifier_options(self):
        options = [
            "Regresión logística",
            "Red neuronal",
            "SVM",
            "Bayesiano",
            "Árbol de decisión",
        ]
        classifier_combobox = self.view.classifier_combobox
        classifier_combobox.addItems(options)

    def change_table_header(self, index: int):
        table_model = self.table_models[index]
        self.view.classifier_table.setModel(table_model)

    def evaluation_results(self, model, train_df: DataFrame, test_df: DataFrame):
        start_time = time.time()
        classifier = Classifier(model)
        classifier.build_classifier(train_df)
        evaluation = Evaluation()
        evaluation.evaluate_model(classifier.get_model(), test_df)
        end_time = time.time()
        result = (
            "",
            str(end_time - start_time),
            str(evaluation.accuracy_score),
            str(evaluation.precision_score),
            str(evaluation.recall_score),
            str(evaluation.f1_score),
            str(evaluation.auc_score),
        )
        return result

    def run_classifier(self):
        classifier_index = self.view.classifier_combobox.currentIndex()

        train_df = self.model.get_train_df()
        test_df = self.model.get_test_df()

        if train_df is None:
            message_box = QMessageBox()
            message_box.setText("Dataset de entramiento no importado")
            message_box.setInformativeText(
                "Debes importar el dataset de entramiento para realizar esta acción."
            )
            message_box.exec()
            return

        if test_df is None:
            message_box = QMessageBox()
            message_box.setText("Dataset de prueba no importado")
            message_box.setInformativeText(
                "Debes importar el dataset de prueba para realizar esta acción."
            )
            message_box.exec()
            return

        table_model = self.table_models[classifier_index]

        if classifier_index == 0:

            model = LogisticRegression(solver="liblinear", max_iter=1000, penalty="l2")
            results = self.evaluation_results(model, train_df, test_df)
            table_model.insert_row(["Regresión logística", *results])

        elif classifier_index == 2:
            model = SVC(kernel="linear", probability=True)
            results = self.evaluation_results(model, train_df, test_df)
            table_model.insert_row(["SVM", "linear", *results])

            model = SVC(kernel="rbf", probability=True)
            results = self.evaluation_results(model, train_df, test_df)
            table_model.insert_row(["SVM", "rbf", *results])

        elif classifier_index == 4:

            model = RandomForestClassifier(
                n_estimators=100, random_state=2016, min_samples_leaf=8
            )
            results = self.evaluation_results(model, train_df, test_df)
            table_model.insert_row(["RandomForest", "This random forest", *results])

        print(table_model.rows)
