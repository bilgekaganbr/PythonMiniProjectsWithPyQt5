import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        #the function that will be called by init function
        self.init_ui()

    def init_ui(self):

        #define a label
        self.text_field = QtWidgets.QLabel("Not clicked on me yet...")
        #define a button
        self.button = QtWidgets.QPushButton("Click me...")
        #initialize the count from 0
        self.count = 0

        #define a vertical box layout
        v_box = QtWidgets.QVBoxLayout()

        #add the button and the label to the vertical box layout and then add stretch so that all the components stay
        #at top
        v_box.addWidget(self.button)
        v_box.addWidget(self.text_field)
        v_box.addStretch()

        #define a horizontal box layout
        h_box = QtWidgets.QHBoxLayout()

        #add a stretch to the left and the right side then add the vertical box layout to the middle
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        #set the horizontal box layout to the window object
        self.setLayout(h_box)

        #connect the button to the function
        self.button.clicked.connect(self.click)

        self.show()

    def click(self):

        #when the button is clicked, increase the count by 1
        self.count += 1
        #update the text in the label
        self.text_field.setText("Clicked on me " + str(self.count) + " times...")

#create an application
app = QtWidgets.QApplication(sys.argv)

window = Window()

#loop the application
sys.exit(app.exec_())

