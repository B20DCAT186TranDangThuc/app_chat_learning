import tkinter as tk

class Login:
    def __init__(self, master, client):
        self.client = client
        self.master = master
        self.master.title("Login")
        self.master.geometry("440x440")

        self.frame = tk.Frame(self.master)
        self.frame_buttom = tk.Frame(self.master)
        self.username_entry = tk.Entry(self.frame)
        self.password_entry = tk.Entry(self.frame, show="*")

        self.button_login = tk.Button(self.frame_buttom, text="Login", command=self.login)
        # self.button_signup = tk.Button(frame_buttom, text="Sign Up", command=self.signup)

        self.username_entry.pack(pady=20)
        self.password_entry.pack(pady=20)
        self.button_login.pack(pady=20)
        self.frame.pack()
        self.frame_buttom.pack(pady=20)

    def login(self):
        # Lấy thông tin username và password từ entry
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Gọi phương thức login trong object client
        self.client.login(username, password)



class SignUp:
    def __init__(self, master, client):
        self.client = client

        self.master = master
        self.master.title("Sign Up")
        self.master.geometry("440x440")

        self.frame = tk.Frame(self.master)
        self.frame_buttom = tk.Frame(self.master)
        self.username_entry = tk.Entry(self.frame)
        self.password_entry = tk.Entry(self.frame, show="*")

        self.button_login = tk.Button(self.frame_buttom, text="Back", command=self.logout)
        self.button_signup = tk.Button(self.frame_buttom, text="Sign Up", command=self.signup)

        self.username_entry.pack(pady=20)
        self.password_entry.pack(pady=20)
        self.button_login.pack(pady=20)
        self.button_signup.pack(pady=20)
        self.frame.pack()
        self.frame_buttom.pack(pady=20)

    def logout(self):
        self.client.logout()

    def signup(self):
        # Lấy thông tin username và password từ entry
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Gọi phương thức signup trong object client
        self.client.signup(username, password)

class Client:
    def __init__(self, master):
        self.master = master
        self.login_object = Login(self.master, self)

    def login(self, username, password):
        self.master.destroy()
        self.master = tk.Tk()
        self.signup_object = SignUp(self.master, self)

    def signup(self, username, password):
        print(username, password)
        self.master.destroy()
        self.master = tk.Tk()
        self.login_object = Login(self.master, self)
        


    def logout(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.login_object = Login(self.master, self)
        
if __name__ == "__main__":
    root = tk.Tk()
    client = Client(root)
    root.mainloop()
