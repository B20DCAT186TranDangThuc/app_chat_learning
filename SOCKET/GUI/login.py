import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox


class Login:
    def __init__(self, master, client):

        self.client = client
        self.master = master
        master.title("Login")
        # master.geometry("440x440")
        master.configure(bg='#333333')

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width/2) - (440/2)
        y = (screen_height/2) - (540/2)

        master.geometry("%dx%d+%d+%d" % (440, 540, x, y))

        frame = tk.Frame(bg='#333333')
        frame_buttom = tk.Frame(bg='#333333')
        # Creating widgets
        bg_ing = tk.PhotoImage(file="nen4.png")
        login_label = tk.Label(
            frame, bg="#333333", image=bg_ing, font=("Arial", 40), compound=tk.CENTER)
        username_label = tk.Label(
            frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))

        self.username_entry = tk.Entry(frame, font=("Arial", 20), )
        self.password_entry = tk.Entry(frame, show="*", font=("Arial", 20),)

        password_label = tk.Label(
            frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.login_button = tk.Button(
            frame_buttom, text="Login", bg="#1b0b54", fg="#FFFFFF", font=("Arial", 16), width=10, height=2, command=self.login)
        self.signup_button = tk.Button(
            frame_buttom, text="Sign Up", bg="#1b0b54", fg="#FFFFFF", font=("Arial", 16), width=10, height=2, command=self.open_sign_up)

        # Placing widgets on the screen
        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
        username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20, padx=(10, 0))
        password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20, padx=(10, 0))

        self.login_button.grid(row=3, column=0, padx=10)
        self.signup_button.grid(row=3, column=1, padx=10)

        frame.pack()
        frame_buttom.pack(pady=20)
        self.logged_in = False
        self.label_image = bg_ing

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "" or password == "":
            messagebox.showerror("Lỗi", "Username or password is empty")
        else:
            self.client.login(username, password)
            
    def open_sign_up(self):
        self.client.open_signup()

    def close_login(self):
        self.client.close_login()


    def on_closing(self):
        self.master.destroy()

    def show_error(self, message):
        messagebox.showerror("Lỗi", message)

        

# if __name__ == "__main__":
#     root = tk.Tk()
#     login_interface = Login(root)
#     root.mainloop()
