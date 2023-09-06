
import tkinter as tk
import sqlite3
import asyncio


def button_clicked():
    print("Button clicked!")

root = tk.Tk()
root.title("Python TKinter Script")
root.title("Всякое полезное.")
root.geometry("500x400")

# Создание текста
label = tk.Label(root, text="Привет, мир!")
label.pack(pady=10)

# Создание кнопки
button = tk.Button(root, text="Нажми меня", command=button_clicked)
button.pack(pady=10)







root.mainloop()