import sqlite3
import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.func()

    def func(self):
        db = sqlite3.connect("coffe.sqlite")
        con = db.cursor()
        result = con.execute("""SELECT sort, degree, grains, review, price, weigth FROM coffe""").fetchall()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Сорт", "Обжарка", "молотый/в зернах", 'Описание',
                                                    'Цена(RUB)', 'Вес(граммы)'])
        self.tableWidget.setRowCount(len(result))

        for i in range(len(result)):
            for z in range(len(result[i])):
                if type(result[i][z]) is str:
                    self.tableWidget.setItem(i, z, QTableWidgetItem((result[i][z])))
                else:
                    if z == 2 and result[i][z] == 1:
                        self.tableWidget.setItem(i, z, QTableWidgetItem(("В зернах")))
                    elif z != 2:
                        self.tableWidget.setItem(i, z, QTableWidgetItem((str(result[i][z]))))
                    else:
                        self.tableWidget.setItem(i, z, QTableWidgetItem(("Молотый")))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())