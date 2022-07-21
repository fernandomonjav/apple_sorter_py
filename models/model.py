from models.dataframe import DataFrame


class Model:
    def __init__(self):
        self.raw_df = None
        self.train_df = None
        self.test_df = None
        self.validation_df = None

    def get_raw_df(self):
        return self.raw_df

    def set_raw_df(self, raw_df: DataFrame):
        self.raw_df = raw_df

    def get_train_df(self):
        return self.train_df

    def set_train_df(self, train_df: DataFrame):
        self.train_df = train_df

    def get_test_df(self):
        return self.test_df

    def set_test_df(self, test_df: DataFrame):
        self.test_df = test_df

    def get_validation_df(self):
        return self.validation_df

    def set_validation_df(self, validation_df: DataFrame):
        self.validation_df = validation_df
