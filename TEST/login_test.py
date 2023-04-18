import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self, master, signup_callback, login_callback):
        self.master = master
        self.signup_callback = signup_callback
        self.login_callback = login_callback
        
        # Create widgets
        self.username_label = tk.Label(master, text="Username:")
        self.username_entry = tk.Entry(master)
        self.password_label = tk.Label(master, text="Password:")
        self.password_entry = tk.Entry(master, show="*")
        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.signup_button = tk.Button(master, text="Signup", command=self.show_signup)
        
        # Layout widgets
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
        self.signup_button.pack()

    def login(self):
        # Get username and password from input fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Validate username and password (optional)
        if not self.validate(username, password):
            return
        
        # Check credentials against database or API
        # If successful, call login_callback with username as argument
        if self.check_credentials(username, password):
            self.login_callback(username)

    def show_signup(self):
        # Destroy login interface and call signup_callback to show signup interface
        self.destroy()
        self.signup_callback()

    def destroy(self):
        # Destroy all widgets in the login interface and clean up resources
        self.username_label.destroy()
        self.username_entry.destroy()
        self.password_label.destroy()
        self.password_entry.destroy()
        self.login_button.destroy()
        self.signup_button.destroy()

    def validate(self, username, password):
        # Validate username and password input (optional)
        if not username:
            messagebox.showerror("Error", "Please enter a username")
            return False
        elif not password:
            messagebox.showerror("Error", "Please enter a password")
            return False
        else:
            return True

    def check_credentials(self, username, password):
        # Check username and password against database or API
        # Return True if credentials are valid, False otherwise
        # You will need to implement this method based on your authentication system
        return True
