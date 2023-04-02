# Author: @sleepy4k
# License: MIT License
# Description: A simple number convertion application with Python.
import os

class Console:
    # Base contructor
    # @param base: Enum
    # @param config: Array
    # @param translate: Array
    # @param logic: Function
    def __init__(self, base, config, translate, logic):
        self.base = base
        self.logic = logic
        self.config = config
        self.translate = translate

        self.create()

    # Clears the command prompt.
    # @param os_name: String
    # @return: None
    def clear_cmd(self, os_name):
        os_name = os_name.lower()
        if os_name == "nt":
            os.system("cls")
        elif os_name == "posix":
            os.system("clear")
        else:
            print(self.translate["unknown"])

    # Prints a separator line.
    # @return: None
    def separator(self):
        print(self.translate["separator"] * self.config["cmd_separator"])

    # Prints the application title.
    # @return: None
    def title(self):
        self.clear_cmd(os.name)
        self.separator()
        print(self.translate["title"])
        self.separator()

    # Prints the menu options.
    # @return: None
    def menu(self):
        self.title()
        for base in self.base:
            print(f"{base.value}. {base.name}")
        print(self.translate["exit"].format(len(self.base) + 1))
        self.separator()

    # Prompts the user for input data.
    # @param base: Enum
    # @return: String
    def get_input(self, base):
        self.title()
        data = input(self.translate["input"].format(base.name.lower()))
        if not data:
            raise ValueError(self.translate["required"].format(base.name.lower()))
        return data

    # Handles errors and prompts the user to continue or exit.
    # @param err: String
    # @return: None
    def error(self, err):
        self.separator()
        print(self.translate["error"].format(err))
        self.separator()
        choice = input(self.translate["prompt"])
        if choice.lower() in ["yes", "y"]:
            return True
        elif choice.lower() in ["no", "n"]:
            self.create()
        else:
            return self.error(self.translate["invalid_choice"])

    # Converts the input data to decimal and other bases.
    # @param base: Enum
    # @param data: String
    # @return: None
    def convertion(self, base, data):
        try:
            return self.logic(base.name, data)
        except ValueError as valErr:
            self.error(valErr)
        except TypeError as typeErr:
            self.error(typeErr)
        except Exception as err:
            self.error(err)

        return self.main(base)

    # Prompts the user to retry or exit.
    # @param base: Enum
    # @return: None
    def retry(self, base):
        choice = input(self.translate["continue"])
        self.separator()
        if choice.lower() in ["yes", "y"]:
            self.main(base)
        elif choice.lower() in ["no", "n"]:
            self.create()
        else:
            self.error(self.translate["invalid_choice"])
            return self.retry(base)

    # Main application.
    # @param base: Enum
    # @return: None
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

    # Creates the application.
    # @return: None
    def create(self):
        self.menu()
        select = input(self.translate["select"])
        self.separator()
        if select == str(len(self.base) + 1):
            exit()
        elif select not in [str(base.value) for base in self.base]:
            self.error(self.translate["invalid_choice"])
        else:
            self.main(self.base(int(select)))
