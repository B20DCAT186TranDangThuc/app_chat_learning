import tkinter as tk
import tkinter.messagebox as tkMessageBox


class SignUp:
    def __init__(self, root):

        self.root = root
        root.title("Sign Up")
        root.geometry("440x440")
        root.configure(bg='#333333')

        frame = tk.Frame(bg='#333333')
        login_label = tk.Label(
            frame, text="Sign Up", bg='#333333', fg="#FF3399", font=("Arial", 30))
        
        username_label = tk.Label(
            frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.username_entry = tk.Entry(frame, font=("Arial", 16))

        password_label = tk.Label(
            frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.password_entry = tk.Entry(frame, show="*", font=("Arial", 16))

        full_name_label = tk.Label(
            frame, text="Full Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.full_name_entry = tk.Entry(frame, font=("Arial", 16))

        # button
        self.sign_up_button = tk.Button(
            frame, text="Sign Up", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.sign_up)
        
        
        # Placing widgets on the screen
        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
        username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        full_name_label.grid(row=3, column=0)
        self.full_name_entry.grid(row=3, column=1, pady=20)
        self.sign_up_button.grid(row=4, column=0, columnspan=2, pady=20)

        frame.pack(pady=40)

        # bấm enter để sign up
        self.root.bind("<Return>", self.sign_up)

        # focus vào entry đầu tiên
        self.username_entry.focus()

        # bấm xuống để focus vào entry dưới
        def focus_next_entry(event):
            event.widget.tk_focusNext().focus()
            return("break")
        # bấm lên để focus vào entry trên
        def focus_previous_entry(event):
            event.widget.tk_focusPrev().focus()
            return("break")
        self.username_entry.bind("<Up>", focus_previous_entry)
        self.username_entry.bind("<Down>", focus_next_entry)
        self.password_entry.bind("<Up>", focus_previous_entry)
        self.password_entry.bind("<Down>", focus_next_entry)
        self.full_name_entry.bind("<Up>", focus_previous_entry)
        self.full_name_entry.bind("<Down>", focus_next_entry)

        # này là để fix bug do chưa thể tách button ra khỏi frame
        self.sign_up_button.bind("<Up>", focus_previous_entry)
        self.sign_up_button.bind("<Down>", focus_next_entry)
            
    def sign_up(self, event=None):
        pass

    
    

if __name__ == "__main__":
    root = tk.Tk()
    chat_interface = SignUp(root)
    root.mainloop()