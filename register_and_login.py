import sys
import sqlite3
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        #function that provides database connection
        self.connect()
        #function that determines the structure of the window
        self.init_ui()

    def connect(self):

        #define the database
        self.connection = sqlite3.connect("user.db")

        #define the cursor
        self.cursor = self.connection.cursor()
        #create a table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

        #commit changes
        self.connection.commit()

    def init_ui(self):

        #determine the window title
        self.setWindowTitle("Register/Login")

        #define an username label
        self.username_field = QtWidgets.QLabel("Username")
        #define a line for username
        self.username = QtWidgets.QLineEdit()

        #define a password label
        self.password_field = QtWidgets.QLabel("Password")
        #define a line for password
        self.password = QtWidgets.QLineEdit()
        #hide the password
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        #define a login button
        self.login_button = QtWidgets.QPushButton("Login")
        #define a register button
        self.register_button = QtWidgets.QPushButton("Register")

        #define an information label
        self.info_field = QtWidgets.QLabel()

        #define a vertical box layout
        v_box = QtWidgets.QVBoxLayout()

        #add components to the vertical box layout as username, password, and labels be in the middle and buttons
        #be at the bottom
        v_box.addStretch()
        v_box.addWidget(self.username_field)
        v_box.addWidget(self.username)
        v_box.addWidget(self.password_field)
        v_box.addWidget(self.password)
        v_box.addWidget(self.info_field)
        v_box.addStretch()
        v_box.addWidget(self.login_button)
        v_box.addWidget(self.register_button)

        #define a horizontal box layout
        h_box = QtWidgets.QHBoxLayout()

        #add vertical box layout to the horizontal box layout as all components be in the middle
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        #set the horizontal box layout to the window object
        self.setLayout(h_box)

        #connect both buttons to their functions
        self.register_button.clicked.connect(self.register)
        self.login_button.clicked.connect(self.login)

        self.show()

    def register(self):

        #take username and password texts
        usern = self.username.text()
        passw = self.password.text()

        #determine all usernames in the database that are equal to usern(there must be 1 or 0 username)
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (usern,))

        #assign found usernames to the list(the list must have 1 element or no elements)
        data = self.cursor.fetchall()

        if len(data) != 0:

            #if the list contains an element then warn the user that user already exists
            self.info_field.setText("User already exists...\nYou can login...")

        else:

            #else, add the new username and password to the database
            self.cursor.execute("INSERT INTO users VALUES(?,?)",(usern, passw))
            #commit changes
            self.connection.commit()

            self.info_field.setText("Registration successful...\nYou can login...")

    def login(self):

        #take username and password texts
        usern = self.username.text()
        passw = self.password.text()

        #determine all usernames and passwords in the database that are equal to
        #usern and passw(there must be 1 or 0 username-password pair) respectively
        self.cursor.execute("SELECT * FROM users WHERE username = ? and password = ?",(usern, passw))

        #assign found usernames and passwords to the list(the list must have 1 element or no elements)
        data = self.cursor.fetchall()

        if len(data) == 0:

            #if the list contains no element then warn the user that user not found
            self.info_field.setText("User not found...\nPlease try again...")

        else:

            self.info_field.setText("Welcome " + usern)

#deifne and application
app = QtWidgets.QApplication(sys.argv)

window = Window()

#loop the application
sys.exit(app.exec_())
