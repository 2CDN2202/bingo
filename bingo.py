import tkinter as tk
import random

num = list(range(1,76))
yet = []

root = tk.Tk()
root.title("ビンゴシステム")
root.geometry("800x600")

def button_click():
    a = random.choice(num)
    num.remove(a)
    yet.append(a)
    label1 = tk.Label(root, text = a, font = ("Arial", 100), bg = "yellow", fg = "blue")
    label1.pack(pady=20)
    label1 = tk.Label(root, text = yet, font = ("Arial", 100))
    label1.pack(pady=20)

btn = tk.Button(root, command=button_click, text="抽選ボタン")
btn.place(relx=0.5, rely=0.5, width=100, height=80, anchor=tk.CENTER)


root.mainloop()