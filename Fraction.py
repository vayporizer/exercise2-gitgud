class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        try:
            if isinstance(numerator, float) or isinstance(denominator, float):
                raise TypeError
            
            if isinstance(numerator, str):
                fraction_string = numerator.split("/", 1)
                # too many inputs
                if len(fraction_string) > 2:
                    raise ValueError
                # checking for floats or words in the string
                try:
                    self.numerator = int(fraction_string[0])
                    self.denominator = int(fraction_string[1])
                except ValueError:
                    raise ValueError
                
            elif isinstance(numerator, int) and isinstance(denominator, int):
                self.numerator = numerator
                self.denominator = denominator
                
            if self.denominator == 0:
                raise ZeroDivisionError

        except (TypeError, ValueError):
            self.numerator = 0
            self.denominator = 1
        
        except ZeroDivisionError:
            raise ZeroDivisionError ("Denominator cannot be zero.")
        
        if self.numerator < 0 and self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        elif self.numerator > 0 > self.denominator:
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
