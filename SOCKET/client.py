import socket
import sys 
import threading
import tkinter as tk
from tkinter import ttk

class ClientNode:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345)
        self.node.connect(port_and_ip)

    def send_sms(self, SMS):
        self.node.send(SMS.encode())

    def receive_sms(self):
        while True:       
            data = self.node.recv(1024).decode()
            if data =="quit: success":
                self.node.close()
                break
            print(data)

    def main(self):
        while True:
            message = input()
            if input == "5$$":
                self.node.close()
                sys.exit()
                break
            self.send_sms(message)

def create_login():
    global login
    login = tk.Tk()
    login.title("Login")
    login.geometry("400x400")
    login.resizable(False, False)
    login.configure(bg="#e6e6e6")
    # login.iconbitmap("icon.ico")

    ttk.Label(login, text="Login", font=("Arial", 20)).pack(pady=10)
    ttk.Label(login, text="Username: ").pack(pady=5)
    ttk.Entry(login, width=30).pack(pady=5)
    ttk.Label(login, text="Password: ").pack(pady=5)
    ttk.Entry(login, width=30).pack(pady=5)
    ttk.Button(login, text="Login", command=login.destroy).pack(pady=10)
    ttk.Button(login, text="Sign Up", command=login.destroy).pack(pady=10)


    login.mainloop()
# Client = ClientNode()
# always_receive = threading.Thread(target=Client.receive_sms)
# always_receive.daemon = True
# always_receive.start()
# Client.main()

create_login()