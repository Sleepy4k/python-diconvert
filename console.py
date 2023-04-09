# Author: @sleepy4k
# License: MIT License
# Description: A simple number conversion application with Python.
import os


class Console:
    __base = None  # Private Variable
    _config = {}  # Protected Variable
    _logic = None  # Protected Variable
    _translate = {}  # Protected Variable

    # Base constructor
    # @param base: Enum
    # @param config: Array
    # @param translate: Array
    # @param logic: Function
    def __init__(self, base, config, translate, logic):
        self.__base = base
        self._logic = logic
        self._config = config
        self._translate = translate

        self.__create()

    # Clears the command prompt.
    # @param os_name: String
    # @return: None
    def __clear_cmd(self, os_name):
        os_name = os_name.lower()

        if os_name == "nt":
            os.system("cls")
        elif os_name == "posix":
            os.system("clear")
        else:
            print(self._translate["unknown"])

    # Prints a separator line.
    # @return: None
    def __separator(self):
        print(self._translate["separator"] * self._config["cmd_separator"])

    # Prints the application title.
    # @return: None
    def __title(self):
        self.__clear_cmd(os.name)
        self.__separator()
        print(self._translate["title"])
        self.__separator()

    # Prints the menu options.
    # @return: None
    def __menu(self):
        self.__title()

        for base in self.__base:
            print(f"{base.value}. {base.name}")

        print(self._translate["exit"].format(len(self.__base) + 1))
        self.__separator()

    # Prompts the user for input data.
    # @param base: Enum
    # @return: String
    def __get_input(self, base):
        self.__title()
        data = input(self._translate["input"].format(base.name.lower()))

        if not data:
            raise ValueError(self._translate["required"].format(base.name.lower()))
        return data

    # Handles errors and prompts the user to continue or exit.
    # @param err: String
    # @return: None
    def __error(self, err):
        self.__separator()
        print(self._translate["error"].format(err))
        self.__separator()
        choice = input(self._translate["prompt"])
        if choice.lower() in ["yes", "y"]:
            return True
        elif choice.lower() in ["no", "n"]:
            self.__create()
        else:
            return self.__error(self._translate["invalid_choice"])

    # Converts the input data to decimal and other bases.
    # @param base: Enum
    # @param data: String
    # @return: None
    def __conversion(self, base, data):
        try:
            return self._logic(base.name, data)
        except ValueError as valErr:
            self.__error(valErr)
        except TypeError as typeErr:
            self.__error(typeErr)
        except Exception as err:
            self.__error(err)

        return self.__main(base)

    # Prompts the user to retry or exit.
    # @param base: Enum
    # @return: None
    def __retry(self, base):
        choice = input(self._translate["continue"])
        self.__separator()
        if choice.lower() in ["yes", "y"]:
            self.__main(base)
        elif choice.lower() in ["no", "n"]:
            self.__create()
        else:
            self.__error(self._translate["invalid_choice"])
            return self.__retry(base)

    # Main application.
    # @param base: Enum
    # @return: None
    def __main(self, base):
        try:
            data = self.__get_input(base)
            conversions = self.__conversion(base, data)
            self.__separator()
            enum = [enums.name for enums in self.__base]

            if "DECIMAL" in enum:
                print(f"Decimal     : {conversions[0]}")
            if "BINARY" in enum:
                print(f"Binary      : {conversions[1]}")
            if "OCTAL" in enum:
                print(f"Octal       : {conversions[2]}")
            if "HEXADECIMAL" in enum:
                print(f"Hexadecimal : {conversions[3]}")
            if "ASCII" in enum:
                print(f"ASCII       : {conversions[4]}")

            self.__separator()
            self.__retry(base)
        except ValueError as err:
            self.__error(err)
            self.__main(base)

    # Creates the application.
    # @return: None
    def __create(self):
        self.__menu()
        select = input(self._translate["select"])
        self.__separator()

        if select == str(len(self.__base) + 1):
            exit()
        elif select not in [str(base.value) for base in self.__base]:
            self.__error(self._translate["invalid_choice"])
        else:
            self.__main(self.__base(int(select)))
