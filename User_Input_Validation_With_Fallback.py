allowed_fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

while True:
    try:
        favorite_fruit = input("Enter your favorite fruit: ").lower()
        if favorite_fruit not in allowed_fruits:
            raise ValueError("Fruit not in the list.")
    except ValueError as ve:
        print(ve)
        print("Please choose a fruit from the list.")
    else:
        print(f"Great choice! Your favorite fruit is {favorite_fruit}.")
        break