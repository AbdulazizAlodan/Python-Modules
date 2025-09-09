from mymath import add, multiply, divide, power, square_root, sub as s

operation = input("Choose operation (add/sub/multiply/divide/power/square_root): ").strip().lower()

result = None

if operation == "square_root":
    a = float(input("Enter the number: "))
    try:
        result = square_root(a)
    except ValueError as e:
        print("Error:", e)
else:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "sub":
            result = s(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        elif operation == "power":
            result = power(a, b)
        else:
            print("Invalid operation")
    except ZeroDivisionError:
        print("Error: division by zero")
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)

if result is not None:
    print("Result =", result)
