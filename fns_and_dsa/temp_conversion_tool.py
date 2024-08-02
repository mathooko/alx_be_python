FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    return celsius*CELSIUS_TO_FAHRENHEIT_FACTOR+32
    
def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
  
# def main():

temp1=int(input("Enter the temperature to convert:"))
temperatureUnit=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperatureUnit=="F":
    convert = convert_to_celsius(temp1)
    print(f"{temp1}\u00B0F is {convert}\u00B0C")
    
    # convert_to_celsius(temp1)#temp1 is input
    # fahrenheit=temp1
    
elif temperatureUnit=="C":
    convert = convert_to_fahrenheit(temp1)
    print(f"{temp1}\u00B0C is {convert}\u00B0F")
    
    # convert_to_fahrenheit(celsius)
    # celsius=temp1
    
else:
    print("Invalid input")
    
# main()

# if temperatureUnit=="C":
#     convert_to_celsius(fahrenheit)
#     print(temp2)
# elif temperatureUnit=="F":
#     convert_to_fahrenheit(celsius)
#     print(temp2)
# else:
#     print("Invalid input")

# print(temp2)

