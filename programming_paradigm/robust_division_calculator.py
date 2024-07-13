import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
class robust_division_calculator:

    def __init__(self,numerator, denominator):

         self.numerator=numerator
         self.denominator=denominator


    def safe_divide(self, numerator,denominator):
        try:
            numerator/denominator
        except ZeroDivisionError:
            denominator==0
        else:
            ans=numerator/denominator

        