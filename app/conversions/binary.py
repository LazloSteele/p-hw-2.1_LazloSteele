from .conversion import Conversion


class Binary(Conversion):
    def __init__(self, value):
        self.decimal_value = Binary.to_decimal(value, 2)
        self.binary_value = value
        self.hexadecimal_value = Binary.to_hexadecimal(value)

    @staticmethod
    def to_byte(bits: list):
        byte_list = []

        bit_place = 0

        for n in bits[::-1]:
            if bit_place % 4 == 0:
                byte_list.insert(0,[])
            byte_list[0].insert(0,n)
            bit_place += 1
        while len(byte_list[0]) < 4:
            byte_list[0].insert(0,0)

        return byte_list

    @staticmethod
    def to_hexadecimal(binary_value: int):
        bits = Binary.format_input(binary_value)

        byte_list = Binary.to_byte(bits)
        converted_value = []

        for byte in byte_list:
            converted_value.append(Binary.to_decimal(Binary.format_values(byte), 2))

        converted_value = Binary.format_values(converted_value)

        return converted_value

if __name__ == "__main__":
    d = Binary(1000111101100)

    print(d.__dict__)