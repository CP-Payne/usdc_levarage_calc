import tkinter as tk
from tkinter import messagebox

def calculate_position_size():
    try:
        leverage = float(leverage_entry.get())
        stop_loss_percent = float(stop_loss_entry.get()) / 100  # Convert to decimal
        risk_amount = float(risk_entry.get())
        
        if stop_loss_percent == 0 or leverage == 0:
            messagebox.showerror("Input Error", "Leverage and stop-loss cannot be zero.")
            return
        
        # Formula: Position Size = Risk Amount / (Stop Loss % * Leverage)
        position_size = risk_amount / (abs(stop_loss_percent) * leverage)
        
        result_label.config(text=f"You need to enter the trade with: {position_size:.2f} USDC")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the main window
root = tk.Tk()
root.title("Leverage Position Size Calculator")
root.geometry("400x300")

# Input fields and labels
tk.Label(root, text="Leverage (e.g., 10 for 10x):").pack(pady=5)
leverage_entry = tk.Entry(root)
leverage_entry.pack(pady=5)

tk.Label(root, text="Stop-Loss % (e.g., -0.5 for -0.5%):").pack(pady=5)
stop_loss_entry = tk.Entry(root)
stop_loss_entry.pack(pady=5)

tk.Label(root, text="Risk Amount in USD:").pack(pady=5)
risk_entry = tk.Entry(root)
risk_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_position_size)
calculate_button.pack(pady=15)

# Result label
result_label = tk.Label(root, text="", font=('Helvetica', 12, 'bold'))
result_label.pack(pady=10)

# Run the app
root.mainloop()
