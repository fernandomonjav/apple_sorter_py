import typing
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant, Qt


class ClassifierTableModel(QAbstractTableModel):
    def __init__(self, cols: list = [], rows: list = []):
        super().__init__()
        self.cols = []

        for col in cols:
            self.insert_columns(col)

        self.rows = []

        for row in rows:
            self.insert_columns(row)

    def rowCount(self, parent: QModelIndex) -> int:
        return len(self.rows)

    def columnCount(self, parent: QModelIndex) -> int:
        return len(self.cols)

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: int
    ) -> typing.Any:
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return self.cols[section]

    def data(self, index: QModelIndex, role: int) -> typing.Any:
        if role != Qt.DisplayRole:
            return QVariant()
        return self.rows[index.row()][index.column()]

    def insert_columns(self, data):
        col_count = len(self.cols)
        self.beginInsertColumns(QModelIndex(), col_count, col_count)
        new_column = data
        self.cols.append(new_column)
        col_count += 1
        self.endInsertColumns()
        return True

    def insert_row(self, data_row):
        row_count = len(self.rows)
        self.beginInsertRows(QModelIndex(), row_count, row_count)
        new_row = data_row
        self.rows.append(new_row)
        row_count += 1
        self.endInsertRows()
        return True
