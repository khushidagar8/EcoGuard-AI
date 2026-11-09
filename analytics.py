
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("EcoGuard AI - Analytics")
root.geometry("850x600")
root.configure(bg="#10251d")

tk.Label(
    root,
    text="ENVIRONMENTAL ANALYTICS",
    font=("Arial", 22, "bold"),
    bg="#10251d",
    fg="white"
).pack(pady=25)

data = [
    ("Monday", 65),
    ("Tuesday", 80),
    ("Wednesday", 55),
    ("Thursday", 110),
    ("Friday", 90),
    ("Saturday", 70),
    ("Sunday", 45)
]

canvas = tk.Canvas(
    root, width=750, height=350,
    bg="#18382a", highlightthickness=0
)
canvas.pack(pady=20)

canvas.create_text(
    375, 25, text="Weekly AQI Analysis",
    fill="white", font=("Arial", 16, "bold")
)

for i, (day, value) in enumerate(data):
    x = 70 + i * 95
    height = value * 2

    canvas.create_rectangle(
        x, 300-height, x+45, 300,
        fill="#35a66a", outline=""
    )

    canvas.create_text(
        x+22, 285-height,
        text=str(value), fill="white"
    )

    canvas.create_text(
        x+22, 320,
        text=day[:3], fill="white"
    )

tk.Label(
    root,
    text="EcoGuard AI | Weekly Pollution Report",
    font=("Arial", 12),
    bg="#10251d", fg="#9ee6b2"
).pack(pady=15)

root.mainloop()
