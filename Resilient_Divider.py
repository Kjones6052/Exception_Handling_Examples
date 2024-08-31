def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero is not allowed."

while True:
    try:
        numerator = float(input("Enter a numerator: "))
        denominator = float(input("Enter a denominator: "))
        result = safe_divide(numerator, denominator)
        print(f"The resul of division is: {result}")
    except ValueError:
        print("Please enter only numbers.")

    continue_input = input("Would you like to perform another division? (yes/no): ").lower()
    if continue_input != "yes":
        break