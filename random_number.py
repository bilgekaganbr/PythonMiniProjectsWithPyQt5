import sys
from PyQt5 import QtWidgets
import random

class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        #set the window title
        self.setWindowTitle("Random Number Generator")

        #define the options label
        self.options = QtWidgets.QLabel("Select a number range...")

        #define radiobuttons
        self.one_ten = QtWidgets.QRadioButton("1-10")
        self.one_hundred = QtWidgets.QRadioButton("1-100")
        self.one_thousand = QtWidgets.QRadioButton("1-1000")

        #define the answer field
        self.answer_field = QtWidgets.QLabel("")

        #define the generate button
        self.generate_button = QtWidgets.QPushButton("Generate")

        #define a vertical box layout
        v_box = QtWidgets.QVBoxLayout()

        #add widgets to the vertical box layout
        v_box.addWidget(self.options)
        v_box.addWidget(self.one_ten)
        v_box.addWidget(self.one_hundred)
        v_box.addWidget(self.one_thousand)
        v_box.addStretch()
        v_box.addWidget(self.answer_field)
        v_box.addStretch()
        v_box.addWidget(self.generate_button)

        #define a horizontal box layout
        h_box = QtWidgets.QHBoxLayout()

        #add the vertical box layout to the horizontal box layout
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        #set the horizontal box layout to the window
        self.setLayout(h_box)

        #connect the generate button to the relative function
        self.generate_button.clicked.connect(lambda : self.generate(self.one_ten.isChecked(), self.one_hundred.isChecked(),
                                                                    self.one_thousand.isChecked(), self.answer_field))

        self.show()

    #generate a random number based on which radiobutton is selected and set it to the answer field
    def generate(self, one_ten, one_hundred, one_thousand, answer_field):

        if one_ten:

            random_number = random.randint(1, 10)
            answer_field.setText(str(random_number))

        if one_hundred:

            random_number = random.randint(1, 100)
            answer_field.setText(str(random_number))

        if one_thousand:

            random_number = random.randint(1, 1000)
            answer_field.setText(str(random_number))

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
