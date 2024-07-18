# class robust_division_calculator:

#     def __init__(self,numerator, denominator):

#          self.numerator=numerator
#          self.denominator=denominator

def safe_divide(numerator,denominator):
        #Ask Why remove self in this instance
        try:
            num = float(numerator)
            denom = float(denominator)
            result = num/denom 
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        except ValueError:
            return "Error: Please enter numeric values only."


#Ask Why remove self in this instance