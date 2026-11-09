
import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys

root = tk.Tk()
root.title("EcoGuard AI - Control Center")
root.geometry("1100x700")
root.configure(bg="#10251d")

folder = os.path.dirname(os.path.abspath(__file__))

def open_module(filename):
    path = os.path.join(folder, filename)

    if not os.path.exists(path):
        messagebox.showerror("Error", filename + " not found!")
        return

    pythonw = os.path.join(
        os.path.dirname(sys.executable), "pythonw.exe"
    )

    if not os.path.exists(pythonw):
        pythonw = sys.executable

    subprocess.Popen([pythonw, path])

header = tk.Frame(root, bg="#163d2b", height=100)
header.pack(fill="x")

tk.Label(
    header, text="🌿 EcoGuard AI",
    font=("Arial", 27, "bold"),
    bg="#163d2b", fg="white"
).pack(side="left", padx=30, pady=25)

tk.Label(
    header, text="SMART ENVIRONMENT CONTROL CENTER",
    font=("Arial", 11, "bold"),
    bg="#163d2b", fg="#9ee6b2"
).pack(side="right", padx=25)

tk.Label(
    root, text="Welcome to EcoGuard AI",
    font=("Arial", 24, "bold"),
    bg="#10251d", fg="white"
).pack(pady=30)

tk.Label(
    root, text="Select Your Module",
    font=("Arial", 15),
    bg="#10251d", fg="#9ee6b2"
).pack(pady=5)

modules = [
    ("🌍 Environmental Dashboard", None),
    ("🤖 AI Risk Predictor", "prediction.py"),
    ("📊 Environmental Analytics", "analytics.py"),
    ("📄 PDF Report Generator", "reports.py")
]

frame = tk.Frame(root, bg="#10251d")
frame.pack(pady=30)

for i, (name, filename) in enumerate(modules):
    if filename is None:
        continue

    tk.Button(
        frame,
        text=name,
        command=lambda f=filename: open_module(f),
        font=("Arial", 15, "bold"),
        bg="#28794b",
        fg="white",
        width=32,
        height=2,
        cursor="hand2"
    ).pack(pady=12)

tk.Label(
    root,
    text="AI + ML | Environment | Sustainability",
    font=("Arial", 12),
    bg="#10251d",
    fg="#9ee6b2"
).pack(side="bottom", pady=25)

root.mainloop()
