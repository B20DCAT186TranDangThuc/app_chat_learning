import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def create_winchat(root, item):
    del_winget(root)
    # get history message

    # NODE.send(f"6$${item[0]}".encode())

    frame_header = tk.Frame(root, bg="#3e82f1", height=50)
    frame_header.pack(fill=tk.X)
    back_button = tk.Button(frame_header, text="Back", bg="#f58d4e", fg="#FFFFFF", font=(
        "Arial", 16), height=1, command=lambda: create_find_friend(root))
    back_button.pack(side=tk.LEFT, padx=10, pady=10)
    frame = tk.LabelFrame(bg='#ffffff', width=400,
                          height=300, text=f"{item[1]}", font=("Arial", 16))
    frame.pack_propagate(0)
    frame.pack(pady=20, padx=20)

    # create a scrollbar and attach it to the message frame
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # create a canvas and attach it to the message frame
    global canvas
    canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # attach the scrollbar to the canvas
    scrollbar.config(command=canvas.yview)

    # create a frame inside the canvas to contain messages
    global message_canvas
    message_canvas = tk.Frame(canvas)
    canvas.create_window((0, 0), window=message_canvas, anchor=tk.NW)

    frame2 = tk.Frame(bg='#3e82f1', width=400, height=100)
    global message_entry
    message_entry = tk.Entry(
        frame2, font=("Arial", 25), width=15, bd=0, highlightthickness=0)
    send_button = tk.Button(
        frame2, text="Send", bg="#f58d4e", fg="#FFFFFF", font=("Arial", 16), height=1, command=lambda: send_message(item[0]))

    message_entry.grid(row=0, column=0)
    send_button.grid(row=0, column=1, padx=(20, 0))
    frame2.pack()

    # focus vào entry đầu tiên
    message_entry.focus()

    # Enter để gửi message
    root.bind("<Return>", lambda x: send_message(item[0]))

    # render message from history
    # if list_history_message is not None:
    #     for message in list_history_message:
    #         if message[1] != item[1]:
    #             render_message(item[1], message[2], "#cccccc")
    #         else:
    #             render_message("Bạn", message[2], "#FF3399")


def del_winget(root):
    for widget in root.winfo_children():
        widget.destroy()


def search_user(username, request_frame):
    for widget in request_frame.winfo_children():
        widget.destroy()

    tk.Button(request_frame, text=f"{username}",  font=(
        "Tahoma", 15), width=20, height=2, bg="#f58d4e", fg="#fff", ).pack(padx=20, pady=10)


def creat_login(root):
    pass

def create_find_friend(root):
    pass

def send_message(username):
    pass

root = tk.Tk()
root.title("App Chat")
root.configure(background="#3e82f1")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (540/2)
y = (screen_height/2) - (540/2)
root.geometry("%dx%d+%d+%d" % (500, 540, x, y))

item = ("username", "name")
create_winchat(root, item)

root.mainloop()
