

while True:
    num1 = float(input("Enter first number, please: "))
    op = input("Enter operation, please: ")
    if op == "quit":
        break

    num2 = float(input("Enter second number, please: "))
    if op == "+":
        result = num1 + num2
        print(result)
        continue

    elif op == "-":
        result = num1 - num2
        print(result)
        continue

    elif op == "*":
        result = num1 * num2
        print(result)
        continue

    elif op == "/":
        if num2 == 0:
            print("Syntax Error")
        elif num2 != 0:
            result = num1 / num2
            print(result)
            continue

input ('Press enter to exit')





