import tkinter as tk
from tkinter import messagebox

def calculate_position_size():
    try:
        balance = float(balance_entry.get())
        leverage = float(leverage_entry.get())
        stop_loss_percent = float(stop_loss_entry.get()) / 100  # Convert to decimal

        if leverage == 0 or stop_loss_percent == 0:
            messagebox.showerror("Input Error", "Leverage and stop-loss cannot be zero.")
            return

        # Determine risk amount
        if risk_type_var.get() == "percentage":
            risk_percent = float(risk_percent_entry.get()) / 100
            risk_amount = balance * risk_percent  # Risk in USD
        else:
            risk_amount = float(risk_entry.get())  # Fixed risk amount in USD

        # Formula: Position Size = Risk Amount / (Stop Loss % * Leverage)
        position_size = risk_amount / (abs(stop_loss_percent) * leverage)

        result_label.config(text=f"You need to enter the trade with: {position_size:.2f} USDC")
        risk_amount_after_calc.config(text=f"Risking: {risk_amount:.2f} USDC")
        two_reward.config(text=f"1:2 reward: {risk_amount * 2:.2f} USDC")
        three_reward.config(text=f"1:3 reward: {risk_amount * 3:.2f} USDC")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the main window
root = tk.Tk()
root.title("Leverage Position Size Calculator")
root.geometry("400x700")
root.resizable(True, True)

# Balance Input
tk.Label(root, text="Current Balance (USD):").pack(pady=5)
balance_entry = tk.Entry(root)
balance_entry.pack(pady=5)

# Leverage Input
tk.Label(root, text="Leverage (e.g., 10 for 10x):").pack(pady=5)
leverage_entry = tk.Entry(root)
leverage_entry.pack(pady=5)

# Stop Loss Input
tk.Label(root, text="Stop-Loss % (e.g., -0.5 for -0.5%):").pack(pady=5)
stop_loss_entry = tk.Entry(root)
stop_loss_entry.pack(pady=5)

# Risk Type Selection
risk_type_var = tk.StringVar(value="fixed")

risk_type_frame = tk.Frame(root)
tk.Radiobutton(risk_type_frame, text="Fixed Risk (USD)", variable=risk_type_var, value="fixed").pack(side="left")
tk.Radiobutton(risk_type_frame, text="Percentage of Balance", variable=risk_type_var, value="percentage").pack(side="left")
risk_type_frame.pack(pady=5)

# Fixed Risk Amount Input
tk.Label(root, text="Risk Amount in USD:").pack(pady=5)
risk_entry = tk.Entry(root)
risk_entry.pack(pady=5)

# Risk Percentage Input
tk.Label(root, text="Risk % of Balance:").pack(pady=5)
risk_percent_entry = tk.Entry(root)
risk_percent_entry.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_position_size)
calculate_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=('Helvetica', 12, 'bold'))
result_label.pack(pady=10)

risk_amount_after_calc = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
risk_amount_after_calc.pack(pady=10)

two_reward = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
two_reward.pack(pady=10)

three_reward = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
three_reward.pack(pady=10)

# Run the app
root.mainloop()