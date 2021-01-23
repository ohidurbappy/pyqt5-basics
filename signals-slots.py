import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def btn1_clicked():
    lbl1.setText("Hi, What's up?")

app=QApplication(sys.argv)


window=QWidget()
window.resize(400,400)
window.setWindowTitle("Signal and Slots")

btn1=QPushButton(window)
btn1.setText("Click Me")
btn1.move(50,20)

lbl1=QLabel(window)
lbl1.setText("Hi there")
lbl1.move(50,50)

btn1.clicked.connect(btn1_clicked)


window.show()

app.exec()