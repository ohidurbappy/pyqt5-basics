import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


app=QApplication(sys.argv)

window=QWidget()

gLayout=QGridLayout()

for row in range(1,5):
    for column in range(1,5):
        gLayout.addWidget(QPushButton("Btn "+str(row)+str(column)),row,column)


window.setLayout(gLayout)
window.setGeometry(100,100,400,400)
window.setWindowTitle("Grid Layout")
window.show()


sys.exit(app.exec())

