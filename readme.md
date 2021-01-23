### Install PyQt5

```bash
pip install pyqt5
pip install pyqt5-tools
```

### Convert .ui file to .py

```bash
pyuic5 -x demo.ui -o demo.py
```

### QLabel

lable=QLabel()

**Signals**
- linkActivated: If the label containing embedded hyperlink is clicked, the URL will open. setOpenExternalLinks feature must be set to true.
- linkHovered: Slot method associated with this signal will be called when the label having embedded hyperlinked is hovered by the mouse.


**Methods**
- setText()
- setAlignment() 
- setPixmap(QPixmap('image.png')) 
- setOpenExternalLinks(bool)
- setTextInteractionFlags(Qt.TextSelectableByMouse)

Example

```python
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
```

### QLineEdit

**Methods**
- setAlignment()
- clear()
- setEchoMode()
- setMaxLength()
- setReadOnly()
- setText()
- text()
- setValidator()
- setInputMask()
- setFont()

Alignment
----
    Qt.AlignLeft
    Qt.AlignRight
    Qt.AlignCenter
    Qt.AlignJustify

Echo Mode
----
    QLineEdit.Normal
    QLineEdit.NoEcho
    QLineEdit.Password
    QLineEdit.PasswordEchoOnEdit

Validation Rules
----
    QIntValidator − Restricts input to integer
    QDoubleValidator − Fraction part of number limited to specified decimals
    QRegexpValidator − Checks input against a Regex expression

**Signals**
- cursorPositionChanged()
- editingFinished()
- returnPressed()
- selectionChanged()
- textChanged()
- textEdited()


```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()
	
   e1 = QLineEdit()
   e1.setValidator(QIntValidator())
   e1.setMaxLength(4)
   e1.setAlignment(Qt.AlignRight)
   e1.setFont(QFont("Arial",20))
	
   e2 = QLineEdit()
   e2.setValidator(QDoubleValidator(0.99,99.99,2))
	
   flo = QFormLayout()
   flo.addRow("integer validator", e1)
   flo.addRow("Double validator",e2)
	
   e3 = QLineEdit()
   e3.setInputMask('+99_9999_999999')
   flo.addRow("Input Mask",e3)
	
   e4 = QLineEdit()
   e4.textChanged.connect(textchanged)
   flo.addRow("Text changed",e4)
	
   e5 = QLineEdit()
   e5.setEchoMode(QLineEdit.Password)
   flo.addRow("Password",e5)
	
   e6 = QLineEdit("Hello Python")
   e6.setReadOnly(True)
   flo.addRow("Read Only",e6)
	
   e5.editingFinished.connect(enterPress)
   win.setLayout(flo)
   win.setWindowTitle("PyQt")
   win.show()
	
   sys.exit(app.exec_())

def textchanged(text):
   print ("contents of text box: "+text)
	
def enterPress():
   print ("edited")

if __name__ == '__main__':
   window()
```

### QPushButton

**Methods**
- setCheckable()
- toggle()
- isChecked()
- setIcon()
- setText()
- setDefault()
- text()
- setEnabled()
- setFont()


**Signals**
- clicked

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
   def __init__(self, parent=None):
      super(Form, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.b1 = QPushButton("Button1")
      self.b1.setCheckable(True)
      self.b1.toggle()
      self.b1.clicked.connect(lambda:self.whichbtn(self.b1))
      self.b1.clicked.connect(self.btnstate)
      layout.addWidget(self.b1)
		
      self.b2 = QPushButton()
      self.b2.setIcon(QIcon(QPixmap("python.gif")))
      self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.b3 = QPushButton("Disabled")
      self.b3.setEnabled(False)
      layout.addWidget(self.b3)
		
      self.b4 = QPushButton("&Default")
      self.b4.setDefault(True)
      self.b4.clicked.connect(lambda:self.whichbtn(self.b4))
      layout.addWidget(self.b4)
      
      self.setWindowTitle("Button demo")

   def btnstate(self):
      if self.b1.isChecked():
         print ("button pressed")
      else:
         print ("button released")
			
   def whichbtn(self,b):
      print ("clicked button is "+b.text())

def main():
   app = QApplication(sys.argv)
   ex = Form()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

### QRadioButton

**Methods**
- setChecked()
- isChecked()
- setText()
- text()


**Signals**
- toggled

> Radio buttons can also be put in a QGroupBox or QButtonGroup to create more than one selectable fields on the parent window.

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Radiodemo(QWidget):
   def __init__(self, parent = None):
      super(Radiodemo, self).__init__(parent)
		
      layout = QHBoxLayout()
      self.b1 = QRadioButton("Button1")
      self.b1.setChecked(True)
      self.b1.toggled.connect(lambda:self.btnstate(self.b1))
      layout.addWidget(self.b1)
		
      self.b2 = QRadioButton("Button2")
      self.b2.toggled.connect(lambda:self.btnstate(self.b2))

      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.setWindowTitle("RadioButton demo")
		
   def btnstate(self,b):
      if b.text() == "Button1":
         if b.isChecked() == True:
            print (b.text()+" is selected")
         else:
            print (b.text()+" is deselected")
				
      if b.text() == "Button2":
         if b.isChecked() == True:
            print (b.text()+" is selected")
         else:
            print (b.text()+" is deselected")
				
def main():

   app = QApplication(sys.argv)
   ex = Radiodemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

### QCheckBox

**Methods**
- setChecked()
- isChecked()
- setText()
- text()
- setTriState() : Provides no change state to checkbox


**Signals**
- toggled
- stateChanged


```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class checkdemo(QWidget):
   def __init__(self, parent = None):
      super(checkdemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.b1 = QCheckBox("Button1")
      self.b1.setChecked(True)
      self.b1.stateChanged.connect(lambda:self.btnstate(self.b1))
      layout.addWidget(self.b1)
		
      self.b2 = QCheckBox("Button2")
      self.b2.toggled.connect(lambda:self.btnstate(self.b2))

      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.setWindowTitle("checkbox demo")

   def btnstate(self,b):
      if b.text() == "Button1":
         if b.isChecked() == True:
            print (b.text()+" is selected")
         else:
            print (b.text()+" is deselected")
				
      if b.text() == "Button2":
         if b.isChecked() == True:
            print (b.text()+" is selected")
         else:
            print (b.text()+" is deselected")
				
def main():

   app = QApplication(sys.argv)
   ex = checkdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```


### QComboBox

**Methods**
- addItem()
- addItems()
- clear()
- count()
- currentText()
- itemText()
- currentIndex()
- setItemText()


**Signals**
- activated() : When the user chooses an item
- currentIndexChanged()
- highlighted() : When an item in the list is highlighted


```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class combodemo(QWidget):
   def __init__(self, parent = None):
      super(combodemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.cb = QComboBox()
      self.cb.addItem("C")
      self.cb.addItem("C++")
      self.cb.addItems(["Java", "C#", "Python"])
      self.cb.currentIndexChanged.connect(self.selectionchange)
		
      layout.addWidget(self.cb)
      self.setLayout(layout)
      self.setWindowTitle("combo box demo")

   def selectionchange(self,i):
      print ("Items in the list are :")
		
      for count in range(self.cb.count()):
         print (self.cb.itemText(count))
      print ("Current index",i,"selection changed ",self.cb.currentText())
		
def main():
   app = QApplication(sys.argv)
   ex = combodemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
```

### QSpinBox

**Methods**
- setMinimum()
- setMaximum()
- setRange() : Sets the minimum, maximum and step value
- setValue()
- Value() : Returns the current value
- singleStep() : Sets the step value of counter


**Signals**
- valueChanged

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class spindemo(QWidget):
   def __init__(self, parent = None):
      super(spindemo, self).__init__(parent)
      
      layout = QVBoxLayout()
      self.l1 = QLabel("current value:")
      self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)
      self.sp = QSpinBox()
		
      layout.addWidget(self.sp)
      self.sp.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
      self.setWindowTitle("SpinBox demo")
		
   def valuechange(self):
      self.l1.setText("current value:"+str(self.sp.value()))

def main():
   app = QApplication(sys.argv)
   ex = spindemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

### QSlider

**Methods**
- setMinimum()
- setMaximum()
- setRange() : Sets the minimum, maximum and step value
- setValue()
- setTickInterval(): Puts the number of ticks on the groove
- Value() : Returns the current value
- setSingleStep() : Sets the step value of counter
- setTickPosition()

Tick positions
----
- QSlider.NoTicks 	No tick marks
- QSlider.TicksBothSides 	Tick marks on both sides
- QSlider.TicksAbove 	Tick marks above the slider
- QSlider.TicksBelow 	Tick marks below the slider
- QSlider.TicksLeft 	Tick marks to the left of the slider
- QSlider.TicksRight 	Tick marks to the right of the slider

**Signals**
- valueChanged
- sliderPressed
- sliderMoved
- sliderReleased


```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class sliderdemo(QWidget):
   def __init__(self, parent = None):
      super(sliderdemo, self).__init__(parent)

      layout = QVBoxLayout()
      self.l1 = QLabel("Hello")
      self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)
		
      self.sl = QSlider(Qt.Horizontal)
      self.sl.setMinimum(10)
      self.sl.setMaximum(30)
      self.sl.setValue(20)
      self.sl.setTickPosition(QSlider.TicksBelow)
      self.sl.setTickInterval(5)
		
      layout.addWidget(self.sl)
      self.sl.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
      self.setWindowTitle("SpinBox demo")

   def valuechange(self):
      size = self.sl.value()
      self.l1.setFont(QFont("Arial",size))
		
def main():
   app = QApplication(sys.argv)
   ex = sliderdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```


### QMenubar QMenu QAction

**Methods**
- menuBar(): Returns main window’s QMenuBar object
- addMenu()
- addAction()
- setEnabled()
- addSeparator()
- Clear()
- setShortcut(): Associates keyboard shortcut to action button
- setText()
- setTitle()
- text()
- title()
- 

**Signals**
- triggered()

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class menudemo(QMainWindow):
   def __init__(self, parent = None):
      super(menudemo, self).__init__(parent)
		
      layout = QHBoxLayout()
      bar = self.menuBar()
      file = bar.addMenu("File")
      file.addAction("New")
		
      save = QAction("Save",self)
      save.setShortcut("Ctrl+S")
      file.addAction(save)
		
      edit = file.addMenu("Edit")
      edit.addAction("copy")
      edit.addAction("paste")
		
      quit = QAction("Quit",self) 
      file.addAction(quit)
      file.triggered[QAction].connect(self.processtrigger)
      self.setLayout(layout)
      self.setWindowTitle("menu demo")
		
   def processtrigger(self,q):
      print (q.text()+" is triggered")
		
def main():
   app = QApplication(sys.argv)
   ex = menudemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```


### QToolBar

**Methods**
- addWidget()
- setMovable()
- addAction()
- addSeparator()
- setOrientation()
- addToolBar()

**Signals**
- actionTriggered


```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class tooldemo(QMainWindow):
   def __init__(self, parent = None):
      super(tooldemo, self).__init__(parent)
      layout = QVBoxLayout()
      tb = self.addToolBar("File")
		
      new = QAction(QIcon("new.bmp"),"new",self)
      tb.addAction(new)
		
      open = QAction(QIcon("open.bmp"),"open",self)
      tb.addAction(open)
      save = QAction(QIcon("save.bmp"),"save",self)
      tb.addAction(save)
      tb.actionTriggered[QAction].connect(self.toolbtnpressed)
      self.setLayout(layout)
      self.setWindowTitle("toolbar demo")
		
   def toolbtnpressed(self,a):
      print ("pressed tool button is",a.text())
		
def main():
   app = QApplication(sys.argv)
   
   ex = tooldemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

### QInputDialog

**Methods**
- getInt()
- getDouble()
- getText()
- getItem()


```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class inputdialogdemo(QWidget):
   def __init__(self, parent = None):
      super(inputdialogdemo, self).__init__(parent)
		
      layout = QFormLayout()
      self.btn = QPushButton("Choose from list")
      self.btn.clicked.connect(self.getItem)
		
      self.le = QLineEdit()
      layout.addRow(self.btn,self.le)
      self.btn1 = QPushButton("get name")
      self.btn1.clicked.connect(self.gettext)
		
      self.le1 = QLineEdit()
      layout.addRow(self.btn1,self.le1)
      self.btn2 = QPushButton("Enter an integer")
      self.btn2.clicked.connect(self.getint)
		
      self.le2 = QLineEdit()
      layout.addRow(self.btn2,self.le2)
      self.setLayout(layout)
      self.setWindowTitle("Input Dialog demo")
		
   def getItem(self):
      items = ("C", "C++", "Java", "Python")
		
      item, ok = QInputDialog.getItem(
         self, "select input dialog", "list of languages", items, 0, False
      )
			
      if ok and item:
         self.le.setText(item)
			
   def gettext(self):
      text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
		
      if ok:
         self.le1.setText(str(text))
			
   def getint(self):
      num,ok = QInputDialog.getInt(self,"integer input dualog","enter a number")
		
      if ok:
         self.le2.setText(str(num))
			
def main():
   app = QApplication(sys.argv)
   ex = inputdialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```


### QFontDialog

**Methods**
- getFont()

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class fontdialogdemo(QWidget):
   def __init__(self, parent = None):
      super(fontdialogdemo, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.btn = QPushButton("choose font")
      self.btn.clicked.connect(self.getfont)
		
      layout.addWidget(self.btn)
      self.le = QLabel("Hello")
		
      layout.addWidget(self.le)
      self.setLayout(layout)
      self.setWindowTitle("Font Dialog demo")
		
   def getfont(self):
      font, ok = QFontDialog.getFont()
		
      if ok:
         self.le.setFont(font)
			
def main():
   app = QApplication(sys.argv)
   ex = fontdialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

### QFileDialog

**Methods**
- getOpenFileName()
- getSaveFileName()
- setacceptMode()
- setFileMode()
- setFilter()

AcceptMode
----
QFileDialog.AcceptOpen
QFileDialog.AcceptSave

File Mode:
----
QFileDialog.AnyFile
QFileDialog.ExistingFile
QFileDialog.Directory
QFileDialog.ExistingFiles


```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class filedialogdemo(QWidget):
   def __init__(self, parent = None):
      super(filedialogdemo, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.btn = QPushButton("QFileDialog static method demo")
      self.btn.clicked.connect(self.getfile)
		
      layout.addWidget(self.btn)
      self.le = QLabel("Hello")
		
      layout.addWidget(self.le)
      self.btn1 = QPushButton("QFileDialog object")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)
		
      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.setLayout(layout)
      self.setWindowTitle("File Dialog demo")
		
   def getfile(self):
      fname,ba = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif)")
      self.le.setPixmap(QPixmap(fname))
		
   def getfiles(self):
      dlg = QFileDialog()
      dlg.setFileMode(QFileDialog.AnyFile)
    #   dlg.setFilter("Text files (*.txt)")
      filenames = QStringListModel()
		
      if dlg.exec_():
         filenames = dlg.selectedFiles()
         f = open(filenames[0], 'r')
			
         with f:
            data = f.read()
            self.contents.setText(data)
				
def main():
   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

Another Example

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class CustomDialog(QFileDialog):

   def __init__(self, *args, **kwargs):
      super(CustomDialog, self).__init__(*args, **kwargs)
      
      self.setWindowTitle("HELLO!")

      QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

      self.buttonBox = QDialogButtonBox(QBtn)
      self.buttonBox.accepted.connect(self.accept)
      self.buttonBox.rejected.connect(self.reject)

      self.layout = QVBoxLayout()
      self.layout.addWidget(self.buttonBox)
      self.setLayout(self.layout)

class filedialogdemo(QWidget):
   def __init__(self, parent = None):

      super(filedialogdemo, self).__init__(parent)

      layout = QVBoxLayout()

      self.btn1 = QPushButton("QFileDialog object")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.setLayout(layout)
      self.setWindowTitle("File Dialog demo")

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
        f = open(filenames[0], 'r')

        with f:
            data = f.read()
            self.contents.setText(data)
def main():

   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
```

### QTab

**Methods**
- addTab()
- insertTab()
- removeTab()
- setCurrentIndex()
- setCurrentWidget()
- setTabBar()
- setTabPosition()
- setTabText()

Tab Position:
----
- QTabWidget.North above the pages
- QTabWidget.South below the pages
- QTabWidget.West to the left of the pages
- QTabWidget.East to the right of the pages

**Signals**
- currentChanged()
- tabClosedRequested()

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class tabdemo(QTabWidget):
   def __init__(self, parent = None):
      super(tabdemo, self).__init__(parent)
      self.tab1 = QWidget()
      self.tab2 = QWidget()
      self.tab3 = QWidget()
		
      self.addTab(self.tab1,"Tab 1")
      self.addTab(self.tab2,"Tab 2")
      self.addTab(self.tab3,"Tab 3")
      self.tab1UI()
      self.tab2UI()
      self.tab3UI()
      self.setWindowTitle("tab demo")
		
   def tab1UI(self):
      layout = QFormLayout()
      layout.addRow("Name",QLineEdit())
      layout.addRow("Address",QLineEdit())
      self.setTabText(0,"Contact Details")
      self.tab1.setLayout(layout)
		
   def tab2UI(self):
      layout = QFormLayout()
      sex = QHBoxLayout()
      sex.addWidget(QRadioButton("Male"))
      sex.addWidget(QRadioButton("Female"))
      layout.addRow(QLabel("Sex"),sex)
      layout.addRow("Date of Birth",QLineEdit())
      self.setTabText(1,"Personal Details")
      self.tab2.setLayout(layout)
		
   def tab3UI(self):
      layout = QHBoxLayout()
      layout.addWidget(QLabel("subjects")) 
      layout.addWidget(QCheckBox("Physics"))
      layout.addWidget(QCheckBox("Maths"))
      self.setTabText(2,"Education Details")
      self.tab3.setLayout(layout)
		
def main():
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```


### QStackedWidget

**Methods**
- addWidget()

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class stackedExample(QWidget):
   def __init__(self):
        super(stackedExample, self).__init__()
        self.leftlist = QListWidget ()
        self.leftlist.insertItem (0, 'Contact' )
        self.leftlist.insertItem (1, 'Personal' )
        self.leftlist.insertItem (2, 'Educational' )

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.stack1)
        self.Stack.addWidget (self.stack2)
        self.Stack.addWidget (self.stack3)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10,10)
        self.setWindowTitle('StackedWidget demo')
        self.show()
		
   def stack1UI(self):
      layout = QFormLayout()
      layout.addRow("Name",QLineEdit())
      layout.addRow("Address",QLineEdit())
      #self.setTabText(0,"Contact Details")
      self.stack1.setLayout(layout)
		
   def stack2UI(self):
      layout = QFormLayout()
      sex = QHBoxLayout()
      sex.addWidget(QRadioButton("Male"))
      sex.addWidget(QRadioButton("Female"))
      layout.addRow(QLabel("Sex"),sex)
      layout.addRow("Date of Birth",QLineEdit())
		
      self.stack2.setLayout(layout)
		
   def stack3UI(self):
      layout = QHBoxLayout()
      layout.addWidget(QLabel("subjects"))
      layout.addWidget(QCheckBox("Physics"))
      layout.addWidget(QCheckBox("Maths"))
      self.stack3.setLayout(layout)
		
   def display(self,i):
      self.Stack.setCurrentIndex(i)
		
def main():
   app = QApplication(sys.argv)
   ex = stackedExample()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

### QSplitter

**Methods**
- addWidget()
- indexOf()
- insertWidget()
- setOrientation()
- setSizes()
- count()


```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QWidget):
   def __init__(self):
    super(Example, self).__init__()
    self.initUI()
	
   def initUI(self):
      hbox = QHBoxLayout(self)
		
      topleft = QFrame()
      topleft.setFrameShape(QFrame.StyledPanel)
      bottom = QFrame()
      bottom.setFrameShape(QFrame.StyledPanel)
		
      splitter1 = QSplitter(Qt.Horizontal)
      textedit = QTextEdit()
      splitter1.addWidget(topleft)
      splitter1.addWidget(textedit)
      splitter1.setSizes([100,200])
		
      splitter2 = QSplitter(Qt.Vertical)
      splitter2.addWidget(splitter1)
      splitter2.addWidget(bottom)
		
      hbox.addWidget(splitter2)
		
      self.setLayout(hbox)
      QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
		
      self.setGeometry(300, 300, 300, 200)
      self.setWindowTitle('QSplitter demo')
      self.show()
		
def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

### QDockWidget

**Methods**
- setWidget()
- setFloating()

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class dockdemo(QMainWindow):
   def __init__(self, parent = None):
      super(dockdemo, self).__init__(parent)
		
      layout = QHBoxLayout()
      bar = self.menuBar()
      file = bar.addMenu("File")
      file.addAction("New")
      file.addAction("save")
      file.addAction("quit")
		
      self.items = QDockWidget("Dockable", self)
      self.listWidget = QListWidget()
      self.listWidget.addItem("item1")
      self.listWidget.addItem("item2")
      self.listWidget.addItem("item3")
		
      self.items.setWidget(self.listWidget)
      self.items.setFloating(False)
      self.setCentralWidget(QTextEdit())
      self.addDockWidget(Qt.RightDockWidgetArea, self.items)
      self.setLayout(layout)
      self.setWindowTitle("Dock demo")
		
def main():
   app = QApplication(sys.argv)
   ex = dockdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

### QStatusBar

**Methods**
- addWidget()
- addPermanentWidget()
- showMessage()
- clearMessage()
- removeWidget()

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class statusdemo(QMainWindow):
   def __init__(self, parent = None):
      super(statusdemo, self).__init__(parent)
		
      bar = self.menuBar()
      file = bar.addMenu("File")
      file.addAction("show")
      file.addAction("add")
      file.addAction("remove")
      file.triggered[QAction].connect(self.processtrigger)
      self.setCentralWidget(QTextEdit())
		
      self.statusBar = QStatusBar()
      self.b = QPushButton("click here")
      self.setWindowTitle("QStatusBar Example")
      self.setStatusBar(self.statusBar)
		
   def processtrigger(self,q):
	
      if (q.text() == "show"):
         self.statusBar.showMessage(q.text()+" is clicked",2000)
			
      if q.text() == "add":
         self.statusBar.addWidget(self.b)
			
      if q.text() == "remove":
         self.statusBar.removeWidget(self.b)
         self.statusBar.show()
			
def main():
   app = QApplication(sys.argv)
   ex = statusdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

### QListWidget

**Methods**
- addItem()
- addItems()
- insertItem()
- clear()
- setCurrentItem()
- sortItems()

**Signals**
- currentItemChanged()
- itemClicked()

```python
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class myListWidget(QListWidget):
   def Clicked(self,item):
      QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())
		
def main():
   app = QApplication(sys.argv)
   listWidget = myListWidget()
	
   #Resize width and height
   listWidget.resize(300,120)
	
   listWidget.addItem("Item 1"); 
   listWidget.addItem("Item 2");
   listWidget.addItem("Item 3");
   listWidget.addItem("Item 4");
	
   listWidget.setWindowTitle('PyQT QListwidget Demo')
   listWidget.itemClicked.connect(listWidget.Clicked)
   
   listWidget.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```


### QScrollbar

Control
- slider
- Two Scroll arrows
- Page control
- Scroll Bar

**Methods**
- setMaximum()

**Signals**
- valueChanged()
- sliderMoved()

```python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QWidget):
   def __init__(self):
      super(Example, self).__init__()
      self.initUI()
		
   def initUI(self):
      vbox = QVBoxLayout(self)
    #   vbox.addLayout(self)
      self.setLayout(vbox)
      hbox = QHBoxLayout()
      self.l1 = QLabel("Drag scrollbar sliders to change color")
      self.l1.setFont(QFont("Arial",16))
		
      hbox.addWidget(self.l1)
      self.s1 = QScrollBar()
      self.s1.setMaximum(255)
		
      self.s1.sliderMoved.connect(self.sliderval)
      self.s2 = QScrollBar()
      self.s2.setMaximum(255)
      self.s2.sliderMoved.connect(self.sliderval)
		
      self.s3 = QScrollBar()
      self.s3.setMaximum(255)
      self.s3.sliderMoved.connect(self.sliderval)
		
      hbox.addWidget(self.s1)
      hbox.addWidget(self.s2)
      hbox.addWidget(self.s3)
		
      self.setGeometry(300, 300, 300, 200)
      self.setWindowTitle('QSplitter demo')
      self.show()
		
   def sliderval(self):
      print (self.s1.value(),self.s2.value(), self.s3.value())
      palette = QPalette()
      c = QColor(self.s1.value(),self.s2.value(), self.s3.value(),255)
      palette.setColor(QPalette.Foreground,c)
      self.l1.setPalette(palette)
		
def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

### Calendar

```python
import sys
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QWidget):
   def __init__(self):
      super(Example, self).__init__()
      self.initUI()
		
   def initUI(self):
      cal = QCalendarWidget(self)
      cal.setGridVisible(True)
      cal.move(20, 20)
      cal.clicked[QDate].connect(self.showDate)
		
      self.lbl = QLabel(self)
      date = cal.selectedDate()
      self.lbl.setText(date.toString())
      self.lbl.move(20, 200)
		
      self.setGeometry(100,100,300,300)
      self.setWindowTitle('Calendar')
      self.show()
		
   def showDate(self, date):
	
      self.lbl.setText(date.toString())
		
def main():

   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```