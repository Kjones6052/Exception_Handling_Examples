def data_entry():
    data_list = []
    while True:
        user_input = input("Enter a number or type 'done' to finish: ")
        if user_input.lower() == "done":
            break

        try:
            try:
                number = float(user_input)
            except ValueError:
                print("That's not a number. Please enter a valid number.")
                continue
            else:
                data_list.append(number)
        except TypeError:
            print("An unexpected tpe error occurred.")
        finally:
            print("You can enter another number or type 'done' to finish. ")

    print(f"Data entered: {data_list}")




data_entry()