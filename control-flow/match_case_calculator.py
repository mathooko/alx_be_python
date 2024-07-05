fNumber = int(input("Enter the first number: "))
sNumber = int(input("Enter the second number"))

operator1 = input("Choose the operation (+, -, *, /): ")

match operator1:
    case "+":
        print(result=fNumber+sNumber)
    case "-":
        print(result=fNumber-sNumber)
    case "*":
        print(result=fNumber*sNumber)
    case "/":
        print(result=fNumber/sNumber)
    case _:
        print("Invalid input")