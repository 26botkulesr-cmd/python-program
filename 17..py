number = int(input("Enter an integer: "))

if number > 0 and number % 2 == 0:
    print(f"{number} is both positive and even.")
else:
    print(f"{number} does not satisfy both conditions.")
