
import tkinter as tk
from tkinter import messagebox

def predict_risk():
    try:
        aqi = float(aqi_entry.get())

        if not 0 <= aqi <= 500:
            messagebox.showerror("Error", "Enter AQI between 0 and 500")
            return

        if aqi <= 50:
            result = "Good"
        elif aqi <= 100:
            result = "Moderate"
        elif aqi <= 200:
            result = "Poor"
        elif aqi <= 300:
            result = "Very Poor"
        else:
            result = "Severe"

        output.config(
            text="Environmental Risk: " + result
        )

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

root = tk.Tk()
root.title("EcoGuard AI - Risk Predictor")
root.geometry("500x400")
root.configure(bg="#10251d")

tk.Label(
    root, text="AI POLLUTION RISK PREDICTOR",
    font=("Arial", 17, "bold"),
    bg="#10251d", fg="white"
).pack(pady=35)

tk.Label(
    root, text="Enter Air Quality Index (AQI):",
    font=("Arial", 12),
    bg="#10251d", fg="white"
).pack(pady=10)

aqi_entry = tk.Entry(root, font=("Arial", 15), width=15)
aqi_entry.pack(pady=10)

tk.Button(
    root, text="PREDICT RISK",
    command=predict_risk,
    bg="#35a66a", fg="white",
    font=("Arial", 12, "bold")
).pack(pady=20)

output = tk.Label(
    root, text="Prediction will appear here",
    font=("Arial", 15, "bold"),
    bg="#10251d", fg="#9ee6b2"
)
output.pack(pady=20)

root.mainloop()
