FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temp1=int(input("Enter the temperature to covert: "))
temperatureUnit=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_fahrenheit(celsius):
    temp2=temp1*(CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    return print(temp2)
def convert_to_celsius(fahrenheit):
    temp2=temp1*(FAHRENHEIT_TO_CELSIUS_FACTOR)-32
    return print(temp2)

if temperatureUnit=="C":
    convert_to_celsius(fahrenheit)
    fahrenheit=temp1
    
elif temperatureUnit=="F":
    convert_to_fahrenheit(celsius)
    celsius=temp1
    
else:
    print("Invalid input")

# if temperatureUnit=="C":
#     convert_to_celsius(fahrenheit)
#     print(temp2)
# elif temperatureUnit=="F":
#     convert_to_fahrenheit(celsius)
#     print(temp2)
# else:
#     print("Invalid input")

# print(temp2)

