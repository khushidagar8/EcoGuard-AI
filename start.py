import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox

folder = os.path.dirname(os.path.abspath(__file__))
login_file = os.path.join(folder, "login.py")

if os.path.exists(login_file):
    subprocess.Popen([sys.executable, login_file])
else:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", "login.py not found!")
    root.destroy()
