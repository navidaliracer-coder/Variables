try:
    age = input("Enter your age: ")

    # Try converting input to integer
    age = int(age)

    # Check for logical age range
    if age < 0 or age > 130:
        raise ValueError("Age is not realistic.")

    # Check odd or even
    if age % 2 == 0:
        print("The age is EVEN.")
    else:
        print("The age is ODD.")

except ValueError:
    print("Error: Please enter a valid integer age (no letters, decimals, or symbols).")

except Exception as e:
    print("Unexpected error:", e)