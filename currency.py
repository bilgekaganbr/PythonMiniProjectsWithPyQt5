import sys
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets

#pull data from web site
def data(currency):

    url = "https://kur.doviz.com/serbest-piyasa/"

    response = requests.get(url + currency)

    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    values = soup.find_all("div", {"class": "text-xl font-semibold text-white"})

    for value in values:

        value = value.text
        value = value.replace(",", ".")

        return value

class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        #set the window title
        self.setWindowTitle("Currency Converter")

        #define a label
        self.line_title = QtWidgets.QLabel("Currency")

        #define the currency field
        self.currency_field = QtWidgets.QLineEdit()

        #define the answer label
        self.answer = QtWidgets.QLabel("")

        #define buttons
        self.convert_button = QtWidgets.QPushButton("Convert")
        self.clear_button = QtWidgets.QPushButton("Clear")

        #define a vertical box layout
        v_box = QtWidgets.QVBoxLayout()

        #add widgets to the vertical box layout
        v_box.addStretch()
        v_box.addWidget(self.line_title)
        v_box.addWidget(self.currency_field)
        v_box.addStretch()
        v_box.addWidget(self.answer)
        v_box.addStretch()
        v_box.addWidget(self.convert_button)
        v_box.addWidget(self.clear_button)

        #define a horizontal box layout
        h_box = QtWidgets.QHBoxLayout()

        #add the vertical box layout to the horizontal box layout
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        #set the horizontal box layout to the window
        self.setLayout(h_box)

        #connect buttons to relative functions
        self.convert_button.clicked.connect(self.convert)
        self.clear_button.clicked.connect(self.clear)

        self.show()

    def convert(self):

        self.answer.setText("1 " + self.currency_field.text() + " is " + data(self.currency_field.text()) + "TL")

    def clear(self):

        self.currency_field.clear()

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())