from re import sub as re_sub
from string import ascii_uppercase


class Conversion:
    """
    these values are used to avoid "magic numbers" later on in the format_values method
    they allow a clean way to iterate through the alphabet to convert digits over 9 to
    the corresponding hex value. The full alphabet is kept to allow up to Hexatridecimal
    number conversion if that is ever desired.
    """
    alphabet = ascii_uppercase
    digits = range(10)

    @staticmethod
    def format_values(value: list):

        for i, n in enumerate(value):
            if len(Conversion.alphabet) >= n >= len(Conversion.digits):
                value[i] = Conversion.alphabet[n - len(Conversion.digits)]

        return re_sub('[^0-9a-zA-Z]+', '', str(value))

    @staticmethod
    def format_input(value: int|str):
        value = [digit for digit in str(value)]
        for i, n in enumerate(value):
            try:
                value[i] = int(n)
            except ValueError:
                pass

            try:
                if n.upper() in Conversion.alphabet:
                    value[i] = Conversion.alphabet.index(n) + len(Conversion.digits)
            except ValueError:
                pass

        return value

    @staticmethod
    def to_decimal(passed_value: int|str, conversion_base: int):
        value_digits = Conversion.format_input(passed_value)
        converted_value = 0
        digit_place = 0

        for n in value_digits[::-1]:
            converted_value += n * conversion_base ** digit_place
            digit_place += 1

        return converted_value
