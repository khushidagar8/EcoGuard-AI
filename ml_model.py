
import tkinter as tk
from tkinter import messagebox
from collections import Counter
from math import sqrt

# Sample training dataset
# Features: PM2.5, PM10, NO2
training_data = [
    ([10, 20, 5], "Good"),
    ([15, 30, 8], "Good"),
    ([20, 35, 10], "Good"),
    ([35, 60, 15], "Moderate"),
    ([45, 75, 20], "Moderate"),
    ([55, 90, 25], "Moderate"),
    ([80, 120, 35], "Poor"),
    ([95, 150, 40], "Poor"),
    ([110, 170, 50], "Poor"),
    ([150, 220, 65], "Severe"),
    ([180, 260, 75], "Severe"),
    ([200, 300, 90], "Severe")
]

def train_model():
    return training_data

model = train_model()

def predict():
    try:
        pm25 = float(pm25_entry.get())
        pm10 = float(pm10_entry.get())
        no2 = float(no2_entry.get())

        if not (0 <= pm25 <= 500 and
                0 <= pm10 <= 500 and
                0 <= no2 <= 200):
            messagebox.showerror(
                "Error", "Values are outside allowed ranges."
            )
            return

        sample = [pm25, pm10, no2]

        distances = []

        for features, label in model:
            distance = sqrt(
                ((sample[0] - features[0]) / 500) ** 2 +
                ((sample[1] - features[1]) / 500) ** 2 +
                ((sample[2] - features[2]) / 200) ** 2
            )

            distances.append((distance, label))

        distances.sort(key=lambda x: x[0])

        nearest = distances[:3]
        votes = Counter(label for distance, label in nearest)
        prediction = votes.most_common(1)[0][0]

        result.config(
            text="ML Prediction: " + prediction
        )

    except ValueError:
        messagebox.showerror(
            "Error", "Please enter valid numeric values."
        )

root = tk.Tk()
root.title("EcoGuard AI - Machine Learning")
root.geometry("550x600")
root.configure(bg="#10251d")

tk.Label(
    root,
    text="ECOGUARD AI - ML ENGINE",
    font=("Arial", 21, "bold"),
    bg="#10251d", fg="white"
).pack(pady=30)

def add_input(label):
    tk.Label(
        root, text=label,
        font=("Arial", 12),
        bg="#10251d", fg="white"
    ).pack(pady=7)

    entry = tk.Entry(
        root, font=("Arial", 13), width=22
    )
    entry.pack(pady=5)
    return entry

pm25_entry = add_input("PM2.5 Level")
pm10_entry = add_input("PM10 Level")
no2_entry = add_input("NO2 Level")

tk.Button(
    root,
    text="TRAINED MODEL PREDICTION",
    command=predict,
    bg="#35a66a",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=20, pady=12
).pack(pady=30)

result = tk.Label(
    root,
    text="Prediction will appear here",
    font=("Arial", 16, "bold"),
    bg="#10251d",
    fg="#9ee6b2"
)
result.pack(pady=15)

tk.Label(
    root,
    text="Algorithm: K-Nearest Neighbors (KNN)",
    font=("Arial", 10),
    bg="#10251d", fg="white"
).pack(pady=10)

root.mainloop()
