import tkinter as tk
from tkinter import ttk


class FindMember():
    def __init__(self, master, client):

        self.client = client
        self.master = master
        self.master.title("Find Member")
        self.master.geometry("460x440")
        self.master.config(bg="#333333")

        self.find_member = tk.Frame(self.master)
        self.request = tk.Frame(self.master)
        # icon search
        self.icon_search = tk.PhotoImage(file="search_icon.png")
        self.input_search = tk.Entry(
            self.find_member, width=16, font=("Arial", 20))

        self.button_search = tk.Button(self.find_member, fg="#FFFFFF", text="Search",
                                       bg="#1b0b54", image=self.icon_search, command=self.search, width=50, height=35)
        self.button_logout = tk.Button(
            self.find_member, fg="#FFFFFF", text="Logout", bg="#1b0b54", command=self.logout, width=10, height=2)

        self.input_search.grid(row=0, column=0, padx=10, pady=10)
        self.button_search.grid(row=0, column=1, padx=10, pady=10)
        self.button_logout.grid(row=0, column=3, padx=10, pady=10)
        self.find_member.grid(row=0, column=0, padx=10, pady=10)

        self.request.grid(row=1, column=0, pady=10)
        self.request.config(height=300, width=420, bg="#343541")
        self.request.grid_propagate(0)

    def search(self):
        # delete all button
        for widget in self.request.winfo_children():
            widget.destroy()

        list_name_member = ["thuc", "thuc1234", "son", "sonocho", "thucdang"]
        dem = 0
        text = self.input_search.get()
        for i in list_name_member:
            if i.find(text) != -1 and text != "":
                dem += 1

                self.button = tk.Button(self.request, text=i, fg="#FFFFFF", font=(
                    "Arial", 16), bg="#1b0b54",width=30, height=2, anchor="w", command=self.open_chat)
                self.button.grid(row=dem, column=1, padx=10, pady=10)
                
        if dem == 0:
            self.lable = tk.Label(self.request, text="Not Found", fg="#FFFFFF", font=(
                "Arial", 16), bg="#1b0b54", width=30, height=2)
            self.lable.grid(row=1, column=0, padx=10, pady=10)
    
    def logout(self):
        self.client.show_login()

    def open_chat(self):
        self.client.open_chat_window()
# if __name__ == '__main__':
#     root = tk.Tk()
#     FindMember(root)
#     root.mainloop()
