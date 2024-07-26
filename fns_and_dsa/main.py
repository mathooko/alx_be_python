from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()


# def main():
#     shopping_list = []
#     while True:
#         display_menu()
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             # Prompt for and add an item
#             pass
#         elif choice == '2':
#             # Prompt for and remove an item
#             pass
#         elif choice == '3':
#             # Display the shopping list
#             pass
#         elif choice == '4':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

# def main():

#     temp1=int(input("Enter the temperature to covert: "))
#     temperatureUnit=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

#     if temperatureUnit=="C":
#         convert_to_celsius(fahrenheit)
#         global fahrenheit=temp1
        
#     elif temperatureUnit=="F":
#         convert_to_fahrenheit(celsius)
#         global celsius=temp1
        
#     else:
#         print("Invalid input")
    
# main()