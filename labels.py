import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def l2_clicked():
    print("L2 Clicked")

def l2_hover():
    print("L2 Hover")


app=QApplication(sys.argv)


window=QWidget()

vLayout=QVBoxLayout()

# QLabel

l1=QLabel()
l1.setText("This is a label")
l1.setAlignment(Qt.AlignCenter)

l2=QLabel()
l2.setText("https://www.ohidur.com")
l2.setOpenExternalLinks(True)
l2.linkHovered.connect(l2_hover)
l2.linkActivated.connect(l2_clicked)



l3=QLabel()
l3.setPixmap(QPixmap('vs.png'))

l4=QLabel()
l4.setText("This text is selectable")
l4.setAlignment(Qt.AlignRight)
l4.setTextInteractionFlags(Qt.TextSelectableByMouse)


vLayout.addWidget(l1)
vLayout.addWidget(l2)
vLayout.addWidget(l3)
vLayout.addWidget(l4)


window.setLayout(vLayout)
window.show()
sys.exit(app.exec())