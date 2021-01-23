import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


app=QApplication(sys.argv)

window=QWidget()

# Vertical box layout
vBox=QVBoxLayout()

btn1=QPushButton("Button 1")
btn2=QPushButton("Button 2")

vBox.addWidget(btn1)
vBox.addStretch()
vBox.addWidget(btn2)


hBox=QHBoxLayout()
btn3=QPushButton("Button 3")
btn4=QPushButton("Button 4")
hBox.addWidget(btn3)
hBox.addStretch()
hBox.addWidget(btn4)


vBox.addStretch()
vBox.addLayout(hBox)

window.setLayout(vBox)

window.setWindowTitle("Hello PyQt5")
window.show()
app.exec()