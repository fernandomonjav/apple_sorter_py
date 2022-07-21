import numpy as np
import pandas as pd


class DataFrame(pd.DataFrame):
    def __init__(self, data: np.ndarray, class_index: int = None):
        super().__init__(data)

        self.class_index = class_index

    def set_class_index(self, class_index: int):
        self.class_index = class_index

    def get_X(self):
        if self.class_index:
            return np.array(self.iloc[:, 0 : self.class_index])
        return np.array(self)

    def get_y(self):
        if not self.class_index:
            return np.array([])
        return np.array(self.iloc[:, self.class_index])
