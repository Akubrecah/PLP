# Advanced Fun Calculator 🎉

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def show_menu():
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Integer Division (//)")
    print("0. Exit")

def calculate(num1, num2, choice):
    if choice == '1':
        return num1 + num2, "Sum"
    elif choice == '2':
        return num1 - num2, "Difference"
    elif choice == '3':
        return num1 * num2, "Product"
    elif choice == '4':
        if num2 == 0:
            return "Error: Division by zero!", None
        return num1 / num2, "Quotient"
    elif choice == '5':
        return num1 ** num2, "Power"
    elif choice == '6':
        if num2 == 0:
            return "Error: Modulus by zero!", None
        return num1 % num2, "Modulus"
    elif choice == '7':
        if num2 == 0:
            return "Error: Integer division by zero!", None
        return num1 // num2, "Integer Division"
    else:
        return None, None

def main():
    print("🎉 Welcome to the Advanced Fun Calculator! 🎉")
    while True:
        show_menu()
        choice = input("Enter your choice (0-7): ")
        if choice == '0':
            print("Goodbye! 👋")
            break
        if choice not in [str(i) for i in range(8)]:
            print("Invalid choice! Please select a valid option.")
            continue
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        result, label = calculate(num1, num2, choice)
        if label:
            print(f"{label}: {result}")
        else:
            print(result)
        again = input("Do you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Thanks for using the calculator! 🚀")
            break

if __name__ == "__main__":
    main()
