# class robust_division_calculator:

#     def __init__(self,numerator, denominator):

#          self.numerator=numerator
#          self.denominator=denominator

def safe_divide(self, numerator,denominator):
        try:
            self.num = float(numerator)
            self.denom = float(denominator)
            result = num/denom 
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        except ValueError:
            return "Error: Please enter numeric values only."
