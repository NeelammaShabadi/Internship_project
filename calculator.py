def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter numbers.")

calculator()
