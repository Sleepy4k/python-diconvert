# Author: @sleepy4k
# License: MIT License
# Description: A simple number conversion application with Python.
import gui as tkinter
import console as cmd


class Converter:
    __base = None  # Private Variable
    _config = {}  # Protected Variable

    # Base constructor
    # @param base: Enum
    # @param config: Array
    # @param translate: Array
    # @return: None
    def __init__(self, base, config, translate):
        self.__base = base
        self._config = config

        if self._config["gui"]:
            tkinter.GUI(base, config, translate, self.__conversion)
        else:
            cmd.Console(base, config, translate, self.__conversion)

    # Conversion function
    # @param base: String
    # @param data: String
    # @return: List
    def __conversion(self, base, data):
        if not base or not data:
            return []

        decimal = 0
        enum = [enums.name for enums in self.__base]

        if base == 'DECIMAL' and 'DECIMAL' in enum:
            decimal = int(data)
        elif base == 'BINARY' and 'BINARY' in enum:
            decimal = int(data, 2)
        elif base == 'OCTAL' and 'OCTAL' in enum:
            decimal = int(data, 8)
        elif base == 'HEXADECIMAL' and 'HEXADECIMAL' in enum:
            decimal = int(data, 16)
        elif base == 'ASCII' and 'ASCII' in enum:
            decimal = [ord(character) for character in data]
            binary = ' '.join([bin(character)[2:] for character in decimal])
            octal = ' '.join([oct(character)[2:] for character in decimal])
            hexadecimal = ' '.join([hex(character)[2:] for character in decimal])
            asi = ''.join([chr(character) for character in decimal])

            decimal = ' '.join([str(character) for character in decimal])

            return [decimal, binary, octal, hexadecimal, asi]

        binary = bin(decimal)[2:]
        octal = oct(decimal)[2:]
        hexadecimal = hex(decimal)[2:]
        asi = chr(decimal)

        return [decimal, binary, octal, hexadecimal, asi]
