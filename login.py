
import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys

root = tk.Tk()
root.title("EcoGuard AI - Admin Login")
root.geometry("550x500")
root.configure(bg="#10251d")

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "eco123":
        messagebox.showinfo("Success", "Welcome Admin!")
        root.destroy()
        open_admin()
    else:
        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password"
        )

def open_admin():
    admin = tk.Tk()
    admin.title("EcoGuard AI - Admin Panel")
    admin.geometry("750x550")
    admin.configure(bg="#10251d")

    tk.Label(
        admin, text="ECOGUARD AI ADMIN PANEL",
        font=("Arial", 23, "bold"),
        bg="#10251d", fg="white"
    ).pack(pady=35)

    folder = os.path.dirname(os.path.abspath(__file__))

    def open_module(filename):
        path = os.path.join(folder, filename)
        if os.path.exists(path):
            subprocess.Popen([sys.executable, path])
        else:
            messagebox.showerror("Error", filename + " not found")

    modules = [
        ("AI Risk Predictor", "prediction.py"),
        ("Analytics", "analytics.py"),
        ("PDF Reports", "reports.py"),
        ("Machine Learning", "ml_model.py"),
        ("Water Quality ML", "water_ml.py")
    ]

    for name, filename in modules:
        tk.Button(
            admin, text=name,
            command=lambda f=filename: open_module(f),
            bg="#28794b", fg="white",
            font=("Arial", 12, "bold"),
            width=28, pady=7
        ).pack(pady=5)

    tk.Button(
        admin, text="Logout",
        command=admin.destroy,
        bg="#a83b3b", fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=20)

    admin.mainloop()

tk.Label(
    root, text="🌿 ECOGUARD AI",
    font=("Arial", 25, "bold"),
    bg="#10251d", fg="#9ee6b2"
).pack(pady=40)

tk.Label(
    root, text="ADMIN LOGIN",
    font=("Arial", 18, "bold"),
    bg="#10251d", fg="white"
).pack(pady=15)

tk.Label(root, text="Username",
         bg="#10251d", fg="white").pack()

user_entry = tk.Entry(root, font=("Arial", 13))
user_entry.pack(pady=8)

tk.Label(root, text="Password",
         bg="#10251d", fg="white").pack()

pass_entry = tk.Entry(root, show="*", font=("Arial", 13))
pass_entry.pack(pady=8)

tk.Button(
    root, text="LOGIN",
    command=login,
    bg="#35a66a", fg="white",
    font=("Arial", 13, "bold"),
    padx=35, pady=10
).pack(pady=25)

root.mainloop()
