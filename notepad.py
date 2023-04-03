import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog
from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        #define a text_field
        self.text_field = QTextEdit()

        #define buttons
        self.clear_button = QPushButton("Clear")
        self.open_button = QPushButton("Open")
        self.save_button = QPushButton("Save")

        #define a horizontal box layout
        h_box = QHBoxLayout()

        #add widgets to the horizontal box layout
        h_box.addWidget(self.clear_button)
        h_box.addWidget(self.open_button)
        h_box.addWidget(self.save_button)

        #define a vertical box layout
        v_box = QVBoxLayout()

        #add widgets and the horizontal box layout to the vertical box layout
        v_box.addWidget(self.text_field)
        v_box.addLayout(h_box)

        #set the vertical box layout to the window
        self.setLayout(v_box)
        #set the window title
        self.setWindowTitle("Notepad")

        #connect buttons to relative functions
        self.clear_button.clicked.connect(self.clear)
        self.open_button.clicked.connect(self.open)
        self.save_button.clicked.connect(self.save)

    def clear(self):

        #clear text which in the text field
        self.text_field.clear()

    def open(self):

        #open a file and write it to the text_field
        file_name = QFileDialog.getOpenFileName(self, "Open File",os.getenv("HOME"))

        with open(file_name[0], "r", encoding="utf-8") as file:

            self.text_field.setText(file.read())

    def save(self):

        #save the writing in the text field to a file
        file_name = QFileDialog.getSaveFileName(self,"Save File", os.getenv("HOME"))

        with open(file_name[0], "w", encoding="utf-8") as file:

            file.write(self.text_field.toPlainText())

class Menu(QMainWindow):

    def __init__(self):

        super().__init__()

        self.notepad = Notepad()

        self.setCentralWidget(self.notepad)

        self.create_menu()

    def create_menu(self):

        #defina a menubar
        menubar = self.menuBar()

        #add a menu
        file = menubar.addMenu("File")

        #define the open file action and its shortcut
        open_file = QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")

        #define the save file action and its shortcut
        save_file = QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        #define the clear file action and its shortcut
        clear_file = QAction("Clear File",self)
        clear_file.setShortcut("Ctrl+D")

        #define the exit file action and its shortcut
        exit_file = QAction("Exit",self)
        exit_file.setShortcut("Ctrl+Q")

        #add actions to the file menu
        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(clear_file)
        file.addAction(exit_file)

        #connect the file menu to the relative function
        file.triggered.connect(self.response)

        #set the window title
        self.setWindowTitle("Notepad")

        self.show()

    def response(self,action):

        if action.text() == "Open File":

            self.notepad.open()

        elif action.text() == "Save File":

            self.notepad.save()

        elif action.text() == "CLear File":

            self.notepad.clear()

        elif action.text() == "Exit":

            qApp.quit()

app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())