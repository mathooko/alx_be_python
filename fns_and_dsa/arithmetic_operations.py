#     fNumber = int(input(def perform_operation():"Enter the first number: "))
# sNumber = int(input("Enter the second number: "))

# operator1 = input("Choose the operation (+, -, *, /): ")
def perform_operation(num1, num2, operation):

    
        if operation=="add":
            return num1+num2
            # print(f"Result: {result}")# Will return None
             
        elif operation=="subtract":
            return num1-num2
           
        elif operation=="multiply":
            return num1*num2
           
        elif operation== "divide":
            if num2 == 0:
                return "Number cannot divide 0"
            else:
                result=num1/num2
                return result
        else:
            return "Invalid input"
