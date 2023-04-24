import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import socket
# GUI
NODE = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_and_ip = ('127.0.0.1', 12345)

request_frame = None


def creat_login(root):
    del_winget(root)

    intro_frame = tk.Frame(root)

    intro_label = tk.Label(intro_frame, text="Login",
                           font=("Arial", 20), fg="blue")
    intro_label.pack(pady=20)

    infomation_frame = tk.Frame(root)
    button_frame = tk.Frame(root)
    user_label = tk.Label(infomation_frame, text="Username")
    pass_label = tk.Label(infomation_frame, text="Password")

    user_entry = tk.Entry(infomation_frame)
    pass_entry = tk.Entry(infomation_frame, show="*")

    button_login = tk.Button(
        button_frame, text="Login", command=lambda: login(root, user_entry, pass_entry))
    button_signup = tk.Button(button_frame, text="Sign Up",
                              command=lambda: create_signup(root))

    user_label.grid(row=0, column=0, padx=10, pady=10)
    pass_label.grid(row=1, column=0, padx=10, pady=10)
    user_entry.grid(row=0, column=1, padx=10, pady=10)
    pass_entry.grid(row=1, column=1, padx=10, pady=10)
    button_login.grid(row=0, column=0, padx=10, pady=10)
    button_signup.grid(row=0, column=1, padx=10, pady=10)

    intro_frame.pack(pady=20)
    infomation_frame.pack(pady=20)
    button_frame.pack(pady=20)


def create_signup(root):
    del_winget(root)
    infomation_frame = tk.Frame(root)
    button_frame = tk.Frame(root)

    user_label = tk.Label(infomation_frame, text="Tên đăng nhập")
    pass_label = tk.Label(infomation_frame, text="Mật khẩu")
    fullname_label = tk.Label(infomation_frame, text="Tên đầy đủ")

    user_entry = tk.Entry(infomation_frame)
    pass_entry = tk.Entry(infomation_frame, show="*")
    fullname_entry = tk.Entry(infomation_frame)

    button_login = tk.Button(button_frame, text="Back",
                             command=lambda: creat_login(root))
    button_signup = tk.Button(
        button_frame, text="Sign Up", command=lambda: signup(user_entry, pass_entry, fullname_entry))

    user_label.grid(row=0, column=0, padx=10, pady=10)
    pass_label.grid(row=1, column=0, padx=10, pady=10)
    fullname_label.grid(row=2, column=0, padx=10, pady=10)
    user_entry.grid(row=0, column=1, padx=10, pady=10)
    pass_entry.grid(row=1, column=1, padx=10, pady=10)
    fullname_entry.grid(row=2, column=1, padx=10, pady=10)
    button_login.grid(row=0, column=0, padx=10, pady=10)
    button_signup.grid(row=0, column=1, padx=10, pady=10)

    infomation_frame.pack(pady=20)
    button_frame.pack(pady=20)


def create_winchat(root, item):
    del_winget(root)
    print(item)
    frame_header = tk.Frame(root, bg="#FF3399", height=50)
    frame_header.pack(fill=tk.X)
    back_button = tk.Button(frame_header, text="Back", bg="#FF3399", fg="#FFFFFF", font=(
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
    canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # attach the scrollbar to the canvas
    scrollbar.config(command=canvas.yview)

    # create a frame inside the canvas to contain messages
    message_canvas = tk.Frame(canvas)
    canvas.create_window((0, 0), window=message_canvas, anchor=tk.NW)

    frame2 = tk.Frame(bg='#333333', width=400, height=100)
    message_entry = tk.Entry(
        frame2, font=("Arial", 25), width=15, bd=0, highlightthickness=0)
    send_button = tk.Button(
        frame2, text="Send", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), height=1, command=lambda: send_message())

    message_entry.grid(row=0, column=0)
    send_button.grid(row=0, column=1, padx=(20, 0))
    frame2.pack()

    # focus vào entry đầu tiên
    message_entry.focus()

    # Enter để gửi message
    root.bind("<Return>", lambda x: send_message())


def create_find_friend(root):
    del_winget(root)

    searching_frame = tk.LabelFrame(
        bg='#ffffff', text="Tìm kiếm bạn bè", font=("Arial", 10))
    searching_frame.pack(pady=20)

    search_input = tk.Entry(searching_frame, font=("Arial", 14))
    search_button = tk.Button(searching_frame, text="🔍", width=3, height=1, font=(
        "Arial", 16), bg="#FF3399", fg="#FFFFFF", command=lambda: search_user(search_input.get(), request_frame))

    logout_button = tk.Button(
        searching_frame, text="Đăng xuất", width=10, height=2, font=("Arial", 10), command=lambda: creat_login(root))

    search_input.grid(row=0, column=0, padx=(20, 0))
    search_button.grid(row=0, column=1, padx=20, pady=10)
    logout_button.grid(row=0, column=2, padx=(0, 20), pady=10)

    global request_frame
    request_frame = tk.Frame(width=400, height=300)
    request_frame.pack(pady=20)

    # friend_button = tk.Button(request_frame, text="Đỗ Sơn", width=20, height=2, font=(
    #     "Arial", 16), command=lambda: create_winchat(root, "Đỗ Sơn Thucc"), anchor="w", justify="left", padx=20)
    # friend_button.grid(row=0, column=0, padx=20, pady=10)
# handle event


def search_user(name, request_frame):
    del_winget(request_frame)
    # gửi tên người dùng cần tìm 
    if name:
        NODE.send(f"8$${name}".encode('utf-8'))


def login(root, user_entry, pass_entry):
    username = user_entry.get()
    password = pass_entry.get()
    NODE.send(f"2$${username}__{password}".encode('utf-8'))


def del_winget(root):
    for widget in root.winfo_children():
        widget.destroy()


def signup(user_entry, pass_entry, fullname_entry):
    username = user_entry.get()
    password = pass_entry.get()
    fullname = fullname_entry.get()
    if username and password and fullname:
        NODE.send(f"1$${username}__{password}__{fullname}".encode('utf-8'))
    else:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")


def render_member(list_str):
    result = eval(list_str)
    if len(result) == 0:
        label = tk.Label(request_frame, text="Không tìm thấy kết quả", font=("Arial", 16))
        label.pack(pady=20)
    for i, item in enumerate(result):
        friend_button = tk.Button(request_frame, text=item[1], width=20, height=2, font=(
            "Arial", 10), command=lambda x_item=item: create_winchat(root,x_item), anchor="w", justify="left", padx=20)
        friend_button.pack(padx=20, pady=10)

def receive_message(node):
    while True:
        try:
            data = node.recv(1024).decode('utf-8')
            print(data)
            list_request = data.split(": ")
            if list_request[0] == "login":
                if list_request[1] == "success":
                    create_find_friend(root)
                else:
                    messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không đúng")
            if list_request[0] == "register":
                if list_request[1] == "success":
                    messagebox.showinfo("Thông báo", "Đăng ký thành công")
                else:
                    messagebox.showerror("Lỗi", "Tài khoản đã tồn tại")
            if list_request[0] == "find_member":
                render_member(list_request[1])
        except Exception as e:
            print(e)
            break


def quit_app(receive_thread):
    NODE.close()
    root.quit()
    root.destroy()
    receive_thread.join()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("App Chat")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (540/2)
    y = (screen_height/2) - (540/2)
    root.geometry("%dx%d+%d+%d" % (500, 540, x, y))

    # connect server
    NODE.connect(port_and_ip)

    # thread receive message
    receive_thread = threading.Thread(target=receive_message, args=(NODE,))
    receive_thread.start()

    creat_login(root)
    root.protocol("WM_DELETE_WINDOW", lambda: quit_app(receive_thread))
    root.mainloop()
