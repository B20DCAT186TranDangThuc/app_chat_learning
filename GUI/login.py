import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

class Login:
    def __init__(self, master):
        
        self.master = master
        master.title("Login")
        master.geometry("440x440")
        master.configure(bg='#333333')

        frame = tk.Frame(bg='#333333')
        # Creating widgets
        login_label = tk.Label(
            frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
        username_label = tk.Label(
            frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.username_entry = tk.Entry(frame, font=("Arial", 16))
        self.password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
        password_label = tk.Label(
            frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.login_button = tk.Button(
            frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.login)
        self.signup_button = tk.Button(
            frame, text="Sign Up", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.sign_up)
        
        # Placing widgets on the screen
        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        self.login_button.grid(row=3, column=0, columnspan=1, pady=20)
        self.signup_button.grid(row=3, column=1, columnspan=1, pady=20)

        frame.pack()
        self.logged_in = False

    def login(self):
        pass
    def sign_up(self):
        pass

    def open_chat_window(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    login_interface = Login(root)
    root.mainloop()
