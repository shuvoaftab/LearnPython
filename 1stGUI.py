import tkinter as tk

from tkinter import filedialog, Text
import os


root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=400, bg="#263d42")
canvas.pack()

frame = tk.Frame(root, bg="#3e646c")
frame.place(relwidth=0.9, relheight=0.9, rely=0.1, relx=0.1)


root.mainloop()
