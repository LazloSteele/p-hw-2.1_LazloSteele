# import the parent class to inherit
from conversion import Conversion


class Decimal(Conversion):
    def __init__(self, value):
        self.decimal_value = value
        self.binary_value = Decimal.convert(value, 2)
        self.hexadecimal_value = Decimal.convert(value, 16)

    @staticmethod
    def convert(decimal_value, conversion_base):
        try:
            int(decimal_value)
        except ValueError:
            print("hey dude, the value must be a valid decimal number")
            return

        try:
            int(conversion_base)
        except ValueError:
            print("hey dude, the value must be a valid integer")
            return

        result_value = []
        running = True

        while running:
            bit = decimal_value % conversion_base
            result_value.insert(0, bit)
            decimal_value = decimal_value // conversion_base

            if decimal_value == 0:
                running = False

        result_value = Conversion.format_values(result_value)

        return result_value


if __name__ == "__main__":
    d = Decimal(100)

    print(d.__dict__)
