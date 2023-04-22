import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Test")
root.geometry("400x400")
frame = tk.Frame(root, bg="#9b59b6")

frame.pack(fill=tk.BOTH, expand=True)
root.mainloop()