import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# app=QApplication(sys.argv)
# window=QWidget()
# window.setWindowTitle("First app")
# window.setGeometry(100,100,640,400)
# b=QLabel(window)
# b.setText("Hello World")
# window.show()
# app.exec()

# oop style

# List of common widgets
# QLabel	
# QLineEdit	
# QTextEdit
# QPushButton
# QRadioButton
# QCheckBox
# QSpinBox
# QScrollBar
# QSlider
# QComboBox
# QMenuBar
# QStatusBar
# QToolBar
# QListView
# QPixmap
# QDialog

class Window(QWidget):

    def __init__(self,parent=None):
        super(Window,self).__init__(parent)
        self.resize(400,400)
        self.setWindowTitle("Learning PyQt5")
        lbl1=QLabel(self)
        lbl1.setText("Hello World")
        font=QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        lbl1.setFont(font)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Window()
    w.show()
    app.exec()
        