import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")[1]
    if color_code:
        color_entry.delete(0, tk.END)
        color_entry.insert(0, color_code)
        text_area.config(bg=color_code)

def update_color(event):
    color_code = color_entry.get()
    text_area.config(bg=color_code)

root = tk.Tk()
root.title("Color Picker")

frame = tk.Frame(root)
frame.pack(pady=20)

color_button = tk.Button(frame, text="Choose Color", command=choose_color)
color_button.pack(side=tk.LEFT, padx=10)

color_entry = tk.Entry(frame, width=20)
color_entry.pack(side=tk.LEFT, padx=10)
color_entry.bind("<Return>", update_color)

text_area = tk.Text(root, height=10, width=40)
text_area.pack(pady=20)

root.mainloop()
