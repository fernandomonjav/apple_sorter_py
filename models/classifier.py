from models.dataframe import DataFrame


class Classifier:
    def __init__(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def build_classifier(self, train_df: DataFrame):
        X = train_df.get_X()
        y = train_df.get_y()

        self.model.fit(X, y)
