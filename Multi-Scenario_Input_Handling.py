while True:
    try:
        user_age = input("Enter your age: ")
        age = int(user_age)
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120")
    except ValueError as ve:
        if "invalid literal" in str(ve):
            print("That's not a number. Please enter your age using digits.")
        else:
            print(ve)
    else:
        print(f"Thank you. Your age is recorded as {age}.")
        break