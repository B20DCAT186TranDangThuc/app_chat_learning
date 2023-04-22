from tkinter import *
import socket, threading

class ChatWindow:
    def __init__(self, master, client):
        
        self.client = client
        self.master = master
        master.title("Chat")
        master.geometry("440x440")
        master.configure(bg='#333333')

        self.frame = LabelFrame(bg='#ffffff', width=400, height=300, text="Đỗ Sơn", font=("Arial", 16))
        self.frame.pack_propagate(0)
        self.frame.pack(pady=20, padx=20)

        # create a scrollbar and attach it to the message frame
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # create a canvas and attach it to the message frame
        self.canvas = Canvas(self.frame, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=TOP, fill=BOTH, expand=True)
        
        # attach the scrollbar to the canvas
        self.scrollbar.config(command=self.canvas.yview)

        # create a frame inside the canvas to contain messages
        self.message_canvas = Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.message_canvas, anchor=NW)

        frame2 = Frame(bg='#333333', width=400, height=100)
        self.message_entry = Entry(
            frame2, font=("Arial", 25), width=15, bd=0, highlightthickness=0)
        self.send_button = Button(
            frame2, text="Send", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),height=1 ,command=self.send_message)

        self.message_entry.grid(row=0, column=0)
        self.send_button.grid(row=0, column=1, padx=(20,0))
        frame2.pack()
        
        # focus vào entry đầu tiên
        self.message_entry.focus()

        # Enter để gửi message
        self.master.bind("<Return>", lambda x: self.send_message())

        receive_thread = threading.Thread(target=self.receive_message, daemon=True)
        receive_thread.start()

        
    def send_message(self):
        pass

    def receive_message(self):
        pass

    def send_sms(self, SMS):
        pass

    def update_canvas(self, event=None):
        pass

# if __name__ == "__main__":
#     root = Tk()
#     my_gui = ChatWindow(root)
#     root.mainloop()