import sys
import tkinter as tk
from tkinter import ttk
import socket
import threading
import time
# func connect to server
def connect():
    node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_and_ip = ("127.0.0.1", 12345)
    node.connect(port_and_ip)
    return node

# func send message to server
def send_message(node, message):
    node.send(message.encode("utf-8"))

# func receive message from server
def receive_message(node):
    while True:
        try:
            data = node.recv(1024).decode("utf-8")
            print(data)
            spit_message(data)
        except:
            close(node)
            break

# func close connection
def close(node):
    node.close()

# func split message from server
def spit_message(message):
    pass


if __name__ == "__main__":
    node = connect()
    thread = threading.Thread(target=receive_message, args=(node,))
    thread.start()

    while True:
        message = input("Enter message: ")
        send_message(node, message)
        time.sleep(1)