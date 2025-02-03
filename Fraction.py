class Fraction(object):

    def __init__(self, numerator=0, denominator=1):

        if isinstance(numerator, float):
            raise TypeError ("Numerator cannot be a decimal.")
        if isinstance(denominator, float):
            raise TypeError ("Denominator cannot be a float.")
        
        if isinstance(numerator, str):
            string_list = numerator.split("/", 1)
            self.numerator = int(string_list[0])
            self.denominator = int(string_list[1])
        elif isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator
        
        if self.denominator == 0:
            raise ZeroDivisionError ("Denominator cannot be zero.")
        
        if self.numerator < 0 and self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        elif self.numerator > 0 and self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        
        greatest_common_div = Fraction.gcd(self.numerator, self.denominator)
        if greatest_common_div != 0:
            self.numerator //= greatest_common_div
            self.denominator //= greatest_common_div
        
    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        else:
            while b:
                a, b = b, a % b
            return abs(a)

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        if self.numerator == 0:
            return "0"
        else:
            return str(self.numerator) + "/" + str(self.denominator)