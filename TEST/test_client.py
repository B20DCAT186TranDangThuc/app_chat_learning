import tkinter as tk
from login_test import Login
from signup_test import Signup
from chatwindow import ChatWindow

class Client:
    def __init__(self, master):
        self.master = master
        self.login = Login(self.master, self.show_signup, self.show_chatwindow)
        self.signup = None
        self.chatwindow = None

    def show_signup(self):
        self.login.destroy()
        self.signup = Signup(self.master, self.show_login)

    def show_login(self):
        self.signup.destroy()
        self.login = Login(self.master, self.show_signup, self.show_chatwindow)

    def show_chatwindow(self, username):
        self.login.destroy()
        if self.signup:
            self.signup.destroy()
        self.chatwindow = ChatWindow(self.master, username)

# Create the main window
root = tk.Tk()

# Create the client
client = Client(root)

# Start the event loop
root.mainloop()
