from os import get_terminal_size
from conversions.binary import Binary
from conversions.decimal import Decimal
from conversions.hexadecimal import Hexadecimal


class TUI:
    def __init__(self):
        self.width = get_terminal_size().columns
        self.height = get_terminal_size().lines
        self.footer_height = 7

        self.command_message = self.default_commands()
        self.current_conversion = None

        self.running = True
        self.converting = False
        self.welcome()

    @staticmethod
    def default_commands():
        return "Which would you like to convert next?: [D]ecimal | [B]inary | [H]exadecimal"

    def divider_print(self, character='#'):
        print(character * self.width)

    def center_print(self, message):
        whitespace = " " * ((self.width - len(message)) // 2)
        print(whitespace + message + whitespace)

    def header_message(self, messages: list):
        message_height = self.height - self.footer_height - 1
        self.divider_print()

        print()
        message_height -= 3
        for message in messages:
            self.center_print(message)
            message_height -= 1
        print("\n" * message_height)

    def footer_message(self):
        self.divider_print()
        print()
        print()
        self.center_print(self.command_message)
        self.center_print("Enter [Q] at any time to [Q]uit")
        print()
        self.divider_print("-")

    def command_flow(self):
        while self.running:
            if not self.converting:
                self.command_message = self.default_commands()

            self.footer_message()

            next_command = input("> ")

            if next_command.upper().startswith("Q"):
                self.running = False
                break

            elif self.converting == "DECIMAL":
                self.current_conversion = Decimal(int(next_command))
                self.header_message([
                    "",
                    "",
                    f"DECIMAL: {self.current_conversion.decimal_value}",
                    f"BINARY: {self.current_conversion.binary_value}",
                    f"HEXADECIMAL: {self.current_conversion.hexadecimal_value}",
                ])
                self.converting = False

            elif self.converting == "BINARY":
                self.current_conversion = Binary(int(next_command))
                self.header_message([
                    "",
                    "",
                    f"DECIMAL: {self.current_conversion.decimal_value}",
                    f"BINARY: {self.current_conversion.binary_value}",
                    f"HEXADECIMAL: {self.current_conversion.hexadecimal_value}",
                ])
                self.converting = False

            elif self.converting == "HEXADECIMAL":
                self.current_conversion = Hexadecimal(int(next_command))
                self.header_message([
                    "",
                    "",
                    f"DECIMAL: {self.current_conversion.decimal_value}",
                    f"BINARY: {self.current_conversion.binary_value}",
                    f"HEXADECIMAL: {self.current_conversion.hexadecimal_value}",
                ])
                self.converting = False

            elif next_command.upper().startswith("D"):
                self.header_message(["DECIMAL MODE"])
                self.command_message = "Enter your decimal number below... ensure it is an integer..."
                self.converting = "DECIMAL"

            elif next_command.upper().startswith("B"):
                self.header_message(["BINARY MODE"])
                self.command_message = "Enter your binary number below... ensure it is binary..."
                self.converting = "BINARY"

            elif next_command.upper().startswith("H"):
                self.header_message(["HEXADECIMAL MODE"])
                self.command_message = "Enter your hexadecimal number below... ensure it is valid hexadecimal..."
                self.converting = "HEXADECIMAL"

            else:
                self.header_message(["NOT A VALID INPUT"])

    def welcome(self):
        self.header_message(["WELCOME TO THE CONVERT-O-MATIX 1000"])
        self.command_flow()
