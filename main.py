import tkinter as tk
from tkinter import messagebox
import math

# Functions for operations
def add():
    calculate(lambda x, y: x + y)

def subtract():
    calculate(lambda x, y: x - y)

def multiply():
    calculate(lambda x, y: x * y)

def divide():
    calculate(lambda x, y: x / y if y != 0 else "Error: Divide by 0")

def power():
    calculate(lambda x, y: x ** y)
def square():
    try:
        num = float(entry1.get())
        label_result.config(text=f"Result: {num ** 2}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def square_root():
    try:
    
        num = float(entry1.get())
        
        label_result.config(text=f"Result: {num ** 2}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def square_root():
    try:
        num = float(entry1.get())
        if num >= 0:
            label_result.config(text=f"Result: {math.sqrt(num)}")
        else:
            messagebox.showerror("Error", "Cannot find square root of a negative number.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = operation(num1, num2)
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create main window
window = tk.Tk()
window.title("Cool Scientific Calculator")
window.geometry("350x400")
window.config(bg="#d6e0f0")

# Create input fields
entry1 = tk.Entry(window, font=('Arial', 14), width=12, bg="#ffffff")
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(window, font=('Arial', 14), width=12, bg="#ffffff")
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create labels
label1 = tk.Label(window, text="First Number:", font=('Arial', 12), bg="#d6e0f0")
label1.grid(row=0, column=0)

label2 = tk.Label(window, text="Second Number:", font=('Arial', 12), bg="#d6e0f0")
label2.grid(row=1, column=0)

label_result = tk.Label(window, text="Result:", font=('Arial', 14), bg="#d6e0f0")
label_result.grid(row=6, column=0, columnspan=2, pady=20)

# Create buttons
button_add = tk.Button(window, text="+", width=8, height=2, bg="#90ee90", font=('Arial', 12), command=add)
button_add.grid(row=2, column=0, padx=5, pady=5)

button_subtract = tk.Button(window, text="-", width=8, height=2, bg="#90ee90", font=('Arial', 12), command=subtract)
button_subtract.grid(row=2, column=1, padx=5, pady=5)

button_multiply = tk.Button(window, text="*", width=8, height=2, bg="#add8e6", font=('Arial', 12), command=multiply)
button_multiply.grid(row=3, column=0, padx=5, pady=5)

button_divide = tk.Button(window, text="/", width=8, height=2, bg="#add8e6", font=('Arial', 12), command=divide)
button_divide.grid(row=3, column=1, padx=5, pady=5)

button_power = tk.Button(window, text="Power", width=8, height=2, bg="#ffa07a", font=('Arial', 12), command=power)
button_power.grid(row=4, column=0, padx=5, pady=5)

button_square = tk.Button(window, text="Square", width=8, height=2, bg="#ffa07a", font=('Arial', 12), command=square)
button_square.grid(row=4, column=1, padx=5, pady=5)

button_sqrt = tk.Button(window, text="Sqrt", width=8, height=2, bg="#ffb6c1", font=('Arial', 12), command=square_root)
button_sqrt.grid(row=5, column=0, padx=5, pady=5)

button_exit = tk.Button(window, text="Exit", width=8, height=2, bg="#ffcccb", font=('Arial', 12), command=window.destroy)
button_exit.grid(row=5, column=1, padx=5, pady=5)

# Run the application
window.mainloop()

