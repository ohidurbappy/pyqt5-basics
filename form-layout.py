import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


app=QApplication(sys.argv)


window=QWidget()

form=QFormLayout()

lblName=QLabel("Name")
editName=QLineEdit()

form.addRow(lblName,editName)

lblAddress=QLabel("Address")
editAddress=QLineEdit()
editAddress2=QLineEdit()

vLayoutAddressContainer=QVBoxLayout()
vLayoutAddressContainer.addWidget(editAddress)
vLayoutAddressContainer.addWidget(editAddress2)

form.addRow(lblAddress,vLayoutAddressContainer)


hboxGender=QHBoxLayout()

lblGender=QLabel("Sex")
radioMale=QRadioButton("Male")
radioFemale=QRadioButton("Female")

hboxGender.addWidget(radioMale)
hboxGender.addWidget(radioFemale)
hboxGender.addStretch()

form.addRow(lblGender,hboxGender)

form.addRow(QPushButton("OK"),QPushButton("Cancel"))


window.setLayout(form)
window.setWindowTitle("Form Layout")
# window.setGeometry(100,100,400,400)
window.show()
sys.exit(app.exec())