
import tkinter as tk
from tkinter import messagebox
from math import sqrt
from collections import Counter

# Illustrative training data
# Features: pH, Turbidity, Dissolved Oxygen
training_data = [
    ([7.0, 1.0, 8.0], "Good"),
    ([7.2, 2.0, 7.5], "Good"),
    ([6.8, 1.5, 8.5], "Good"),

    ([6.5, 5.0, 6.0], "Moderate"),
    ([7.8, 8.0, 5.5], "Moderate"),
    ([6.2, 7.0, 6.2], "Moderate"),

    ([5.5, 20.0, 3.0], "Poor"),
    ([9.0, 30.0, 2.0], "Poor"),
    ([5.0, 15.0, 2.5], "Poor")
]

def predict_water():
    try:
        ph = float(ph_entry.get())
        turbidity = float(turb_entry.get())
        oxygen = float(do_entry.get())

        if not 0 <= ph <= 14:
            raise ValueError("pH must be between 0 and 14")

        if not 0 <= turbidity <= 1000:
            raise ValueError("Invalid turbidity value")

        if not 0 <= oxygen <= 20:
            raise ValueError("DO must be between 0 and 20")

        sample = [ph, turbidity, oxygen]
        distances = []

        for features, label in training_data:
            distance = sqrt(
                ((sample[0] - features[0]) / 14) ** 2 +
                ((sample[1] - features[1]) / 1000) ** 2 +
                ((sample[2] - features[2]) / 20) ** 2
            )

            distances.append((distance, label))

        distances.sort(key=lambda x: x[0])

        nearest = distances[:3]
        votes = Counter(item[1] for item in nearest)
        prediction = votes.most_common(1)[0][0]

        result.config(
            text="Water Quality: " + prediction
        )

    except ValueError as error:
        messagebox.showerror("Input Error", str(error))

root = tk.Tk()
root.title("EcoGuard AI - Water Quality ML")
root.geometry("550x600")
root.configure(bg="#10251d")

tk.Label(
    root,
    text="WATER QUALITY AI PREDICTOR",
    font=("Arial", 20, "bold"),
    bg="#10251d", fg="white"
).pack(pady=30)

def create_input(label):
    tk.Label(
        root, text=label,
        font=("Arial", 12),
        bg="#10251d", fg="white"
    ).pack(pady=8)

    entry = tk.Entry(root, font=("Arial", 13), width=22)
    entry.pack(pady=5)
    return entry

ph_entry = create_input("Enter pH Level (0-14)")
turb_entry = create_input("Enter Turbidity (NTU)")
do_entry = create_input("Dissolved Oxygen (mg/L)")

tk.Button(
    root,
    text="PREDICT WATER QUALITY",
    command=predict_water,
    bg="#35a66a", fg="white",
    font=("Arial", 12, "bold"),
    padx=20, pady=12
).pack(pady=30)

result = tk.Label(
    root,
    text="Prediction will appear here",
    font=("Arial", 16, "bold"),
    bg="#10251d", fg="#9ee6b2"
)
result.pack(pady=15)

tk.Label(
    root,
    text="Algorithm: K-Nearest Neighbors",
    bg="#10251d", fg="white"
).pack(pady=10)

root.mainloop()
