class Fraction(object):

    def __init__(self, numerator=0, denominator=1):

        if isinstance(numerator, float):
            raise TypeError ("Numerator cannot be a decimal.")
        if isinstance(denominator, float):
            raise TypeError ("Denominator cannot be a float.")
        
        if denominator == 0:
            raise ZeroDivisionError ("Denominator cannot be zero.")
        
        if isinstance(numerator, str):
            string_list = numerator.split("/", 1)
            self.numerator = int(string_list[0])
            self.denominator = int(string_list[1])
        elif isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator
        
    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass