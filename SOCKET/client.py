import sys
import tkinter as tk
from tkinter import ttk
import socket
import GUI.login as login
import GUI.win_chat as chat
import GUI.sign_up as sign_up
import GUI.find_chatmember as find_member

import threading
class ClientNode:
    def __init__(self, master):
        # connect to server
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345)
        self.node.connect(port_and_ip)

        # create thread to receive message
        self.thread = threading.Thread(target=self.receive_message)
        self.thread.start()

        self.master = master
        # render login page
        self.login_page = login.Login(self.master, self)
        self.master.mainloop()




    def receive_message(self):
        while True:
            try:
                data = self.node.recv(1024).decode('utf-8')
                print(data)
                if data == "login: success":
                    self.show_find_member()
                elif data == "login: fail":
                    self.login_page.show_error("Login fail")
            except:
                self.close()
                break

    def send_message(self, message):
        self.node.send(message.encode('utf-8'))



    # function to render gui (login, signup, chat, find member)
    def open_signup(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.signup_page = sign_up.SignUp(self.master, self)

    def show_find_member(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.find_member_page = find_member.FindMember(self.master, self)

    def open_chat_window(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.chat_window = chat.ChatWindow(self.master, self)

    def show_login(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.login_page = login.Login(self.master, self)
    
    def show_error(self, message):
        self.login_page.show_error(message)
    
    def sign_up(self, username, password, fullname):
        self.send_message(f"1$${username}__{password}__{fullname}")

    def login(self, username, password):
        self.send_message(f"2$${username}__{password}")

    def find_member(self, username):
        self.send_message(f"3$${username}")

    def close(self):
        self.node.close()
        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    client = ClientNode(root)
