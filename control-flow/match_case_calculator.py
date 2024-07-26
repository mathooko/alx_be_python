fNumber = int(input("Enter the first number: "))
sNumber = int(input("Enter the second number: "))

operator1 = input("Choose the operation (+, -, *, /): ")

match operator1:
    case "+":
        # print(str(result)=fNumber+sNumber)#Ask why this does not work
        # str(result=fNumber+sNumber)#Match case does not always need a print
        result=fNumber+sNumber
        print(f"The result is {result}")
    case "-":
        result=fNumber-sNumber
        print(f"The result is {result}")
    case "*":
        result=fNumber*sNumber
        print(f"The result is {result}")
    case "/":
        if sNumber != 0:
            result=fNumber/sNumber
            print(f"The result is {result}")
        else:
            print("Number cannot divide 0")
    case _:
        print("Invalid input")