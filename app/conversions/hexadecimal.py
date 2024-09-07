from .conversion import Conversion


class Hexadecimal(Conversion):
    def __init__(self, value):
        self.decimal_value = Hexadecimal.to_decimal(value, 16)
        self.binary_value = Hexadecimal.to_binary(value, 2)
        self.hexadecimal_value = value

    @staticmethod
    def to_binary(hexadecimal_value, conversion_base):
        byte_list = Hexadecimal.format_input(hexadecimal_value)
        converted_value = ""

        for i, byte in enumerate(byte_list):
            byte_list[i] = []
            running = True

            while running:
                bit = byte % conversion_base
                byte_list[i].insert(0, bit)
                byte = byte // conversion_base

                if byte == 0:
                    while len(byte_list[i]) < 4:
                        byte_list[i].insert(0, 0)

                    byte_list[i] = str(Hexadecimal.format_values(byte_list[i]))
                    running = False

            converted_value += byte_list[i]
        converted_value = int(converted_value)

        return converted_value


if __name__ == "__main__":
    d = Hexadecimal("AB1A")

    print(d.__dict__)