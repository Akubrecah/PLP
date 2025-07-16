import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Advanced Fun Calculator 🎉")
        self.create_widgets()  # Initialize all widgets

    def create_widgets(self):
        # Label and entry for first number
        self.num1_label = tk.Label(self.root, text="First Number:")
        self.num1_label.grid(row=0, column=0)
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.grid(row=0, column=1)

        # Label and entry for second number
        self.num2_label = tk.Label(self.root, text="Second Number:")
        self.num2_label.grid(row=1, column=0)
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.grid(row=1, column=1)

        # Dropdown for selecting operation
        self.operation_label = tk.Label(self.root, text="Operation:")
        self.operation_label.grid(row=2, column=0)
        self.operation_var = tk.StringVar(value="Addition (+)")
        self.operations = [
            "Addition (+)", "Subtraction (-)", "Multiplication (*)",
            "Division (/)", "Power (^)", "Modulus (%)", "Integer Division (//)"
        ]
        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, *self.operations)
        self.operation_menu.grid(row=2, column=1)

        # Button to perform calculation
        self.calc_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calc_button.grid(row=3, column=0, columnspan=2)

        # Label to display result
        self.result_label = tk.Label(self.root, text="Result: ")
        self.result_label.grid(row=4, column=0, columnspan=2)

    def calculate(self):
        # Try to convert input to float, show error if invalid
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return

        # Get selected operation and perform calculation
        op = self.operation_var.get()
        if op == "Addition (+)":
            result = num1 + num2
            label = "Sum"
        elif op == "Subtraction (-)":
            result = num1 - num2
            label = "Difference"
        elif op == "Multiplication (*)":
            result = num1 * num2
            label = "Product"
        elif op == "Division (/)":
            if num2 == 0:
                messagebox.showerror("Math Error", "Division by zero!")
                return
            result = num1 / num2
            label = "Quotient"
        elif op == "Power (^)":
            result = num1 ** num2
            label = "Power"
        elif op == "Modulus (%)":
            if num2 == 0:
                messagebox.showerror("Math Error", "Modulus by zero!")
                return
            result = num1 % num2
            label = "Modulus"
        elif op == "Integer Division (//)":
            if num2 == 0:
                messagebox.showerror("Math Error", "Integer division by zero!")
                return
            result = num1 // num2
            label = "Integer Division"
        else:
            result = "Unknown operation"
            label = ""

        # Update result label
        self.result_label.config(text=f"Result ({label}): {result}")

# Main loop to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
