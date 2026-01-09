import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Bağımsız Program")
root.geometry("300x150")

def selam_ver():
    messagebox.showinfo("Mesaj", "Merhaba! Bu program tarayıcıdan bağımsız çalışıyor.")

btn = tk.Button(root, text="Tıkla", command=selam_ver)
btn.pack(expand=True)

root.mainloop()
