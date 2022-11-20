import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('espresso db.db')
        res = self.con.cursor().execute('SELECT * FROM coffee').fetchall()
        self.table.setColumnCount(len(res[0]))
        self.table.setRowCount(len(res))
        self.table.setHorizontalHeaderLabels(['ИД', 'Название сорта', 'Степень обжарки', 'Молотый/В зернах',
                                              'Описание вкуса', 'Цена', 'Объем упаковки'])
        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                if j == 2:
                    roast = self.con.cursor().execute(f'SELECT name FROM roasts WHERE id = {elem}').fetchone()[0]
                    self.table.setItem(i, j, QTableWidgetItem(roast))
                elif j == 3:
                    if elem == 1:
                        self.table.setItem(i, j, QTableWidgetItem('Молотый'))
                    elif elem == 2:
                        self.table.setItem(i, j, QTableWidgetItem('В зернах'))
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(elem)))
        self.table.resizeColumnsToContents()


app = QApplication(sys.argv)
ex = Espresso()
ex.show()
sys.exit(app.exec())
