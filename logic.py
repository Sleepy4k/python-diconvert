# Author: @sleepy4k
# License: MIT License
# Description: A simple number convertion application with Python.
# Clears the command prompt.
import os

class Converter:
    def __init__(self, base, config, translate):
        self.base = base
        self.config = config
        self.translate = translate
        self.logic()

    # Clears the command prompt.
    def clear_cmd(self, os_name):
        os_name = os_name.lower()
        if os_name == "nt":
            os.system("cls")
        elif os_name == "posix":
            os.system("clear")
        else:
            print(self.translate["unknown"])

    # Prints a separator line.
    def separator(self):
        print(self.translate["separator"] * self.config["separator"])

    # Prints the application title.
    def title(self):
        self.clear_cmd(os.name)
        self.separator()
        print(self.translate["title"])
        self.separator()

    # Prints the menu options.
    def menu(self):
        self.title()
        for base in self.base:
            print(f"{base.value}. {base.name}")
        print(self.translate["exit"].format(len(self.base) + 1))
        self.separator()

    # Prompts the user for input data.
    def get_input(self, base):
        self.title()
        data = input(self.translate["input"].format(base.name.lower()))
        if not data:
            raise ValueError(self.translate["required"].format(base.name.lower()))
        return data

    # Handles errors and prompts the user to continue or exit.
    def error(self, err):
        self.separator()
        print(self.translate["error"].format(err))
        self.separator()
        choice = input(self.translate["prompt"])
        if choice.lower() in ["yes", "y"]:
            return True
        elif choice.lower() in ["no", "n"]:
            self.logic()
        else:
            return self.error(self.translate["invalid_choice"])

    # Converts the input data to decimal and other bases.
    def convertion(self, base, data):
        try:
            match base:
                case self.base.DECIMAL:
                    decimal = int(data)
                case self.base.BINARY:
                    decimal = int(data, 2)
                case self.base.OCTAL:
                    decimal = int(data, 8)
                case self.base.HEXADECIMAL:
                    decimal = int(data, 16)
                case self.base.ASCII:
                    """Convert string to array."""
                    decimal = [ord(character) for character in data]

                    """Convert array to other bases."""
                    binary = ' '.join([bin(character)[2:] for character in decimal])
                    octal = ' '.join([oct(character)[2:] for character in decimal])
                    hexadecimal = ' '.join([hex(character)[2:] for character in decimal])
                    asci = ''.join([chr(character) for character in decimal])

                    """Convert array to decimal."""
                    decimal = ' '.join([str(character) for character in decimal])

                    """Return the result."""
                    return [decimal, binary, octal, hexadecimal, asci]
            """Convert decimal to other bases."""
            binary = bin(decimal)[2:]
            octal = oct(decimal)[2:]
            hexadecimal = hex(decimal)[2:]
            asci = chr(decimal)

            """Return the result."""
            return [decimal, binary, octal, hexadecimal, asci]
        except ValueError as valErr:
            self.error(valErr)
        except TypeError as typeErr:
            self.error(typeErr)
        except Exception as err:
            self.error(err)
        """Return the result."""
        return self.main(base)

    # Prompts the user to retry or exit.
    def retry(self, base):
        choice = input(self.translate["continue"])
        self.separator()
        if choice.lower() in ["yes", "y"]:
            self.main(base)
        elif choice.lower() in ["no", "n"]:
            self.logic()
        else:
            self.error(self.translate["invalid_choice"])
            return self.retry(base)

    # Main logic.
    def main(self, base):
        try:
            data = self.get_input(base)
            conversions = self.convertion(base, data)
            self.separator()
            print(f"Decimal     : {conversions[0]}")
            print(f"Binary      : {conversions[1]}")
            print(f"Octal       : {conversions[2]}")
            print(f"Hexadecimal : {conversions[3]}")
            print(f"ASCII       : {conversions[4]}")
            self.separator()
            self.retry(base)
        except ValueError as err:
            self.error(err)
            self.main(base)

    # Initial Logic
    def logic(self):
        self.menu()
        select = input(self.translate["select"])
        self.separator()
        if select == str(len(self.base) + 1):
            exit()
        elif select not in [str(base.value) for base in self.base]:
            self.error(self.translate["invalid_choice"])
        else:
            self.main(self.base(int(select)))
