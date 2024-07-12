def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")
if __name__ == "__main__":
    main()


#     fNumber = int(input(def perform_operation():"Enter the first number: "))
# sNumber = int(input("Enter the second number: "))

# operator1 = input("Choose the operation (+, -, *, /): ")
def perform_operation(num1, num2, operation):

    match operation:
        case "+":
            print(result=num1+num2)
        case "-":
            print(result=num1-num2)
        case "*":
            print(result=num1*num2)
        case "/":
            if num2 == 0:
                print("Number cannot divide 0")
            else:
                result=num1/num2
                print(result)
        case _:
            print("Invalid input")
