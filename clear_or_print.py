import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        #the function that will be called by init function
        self.init_ui()

    def init_ui(self):

        #define a line for text
        self.text_field = QtWidgets.QLineEdit()
        #define a 'clear' button
        self.clear = QtWidgets.QPushButton("Clear")
        #define a 'print' button
        self.print = QtWidgets.QPushButton("Print")

        #define a vertical box layout
        v_box = QtWidgets.QVBoxLayout()

        #add the label and two buttons to the vertical box layout then add a stretch so that all the components stay at top
        v_box.addWidget(self.text_field)
        v_box.addWidget(self.clear)
        v_box.addWidget(self.print)
        v_box.addStretch()

        #set the vertical box layout to the window object
        self.setLayout(v_box)

        #connect both buttons to the function
        self.clear.clicked.connect(self.click)
        self.print.clicked.connect(self.click)

        self.show()

    def click(self):

        #define a sender so that object can understand which button is clicked
        sender = self.sender()

        if sender.text() == "Clear":

            #if the clear button is clicked then erase the text in the label
            self.text_field.clear()

        else:

            #else print the text in the label
            print(self.text_field.text())

#create an application
app = QtWidgets.QApplication(sys.argv)

window = Window()

#loop the application
sys.exit(app.exec_())
