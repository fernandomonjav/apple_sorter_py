from models.dataframe import DataFrame
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


class Evaluation:
    def __init__(self):
        pass

    def evaluate_model(self, model, test_df: DataFrame):
        self.X_test = test_df.get_X()
        self.y_test = test_df.get_y()
        self.y_pred = model.predict(self.X_test)
        self.y_score = model.predict_proba(self.X_test)

        # Precisión del modelo: ¿con qué frecuencia es correcto el clasificador?
        self.accuracy_score = accuracy_score(self.y_test, self.y_pred)

        # Precisión del modelo: ¿qué porcentaje de tuplas positivas se etiquetan como tales?
        self.precision_score = precision_score(
            self.y_test, self.y_pred, average="micro"
        )

        # Model Recall: ¿qué porcentaje de tuplas positivas se etiquetan como tales?
        self.recall_score = recall_score(self.y_test, self.y_pred, average="micro")

        # F-Score o F-Measure
        self.f1_score = f1_score(self.y_test, self.y_pred, average="micro")

        self.auc_score = roc_auc_score(self.y_test, self.y_score, multi_class="ovr")
