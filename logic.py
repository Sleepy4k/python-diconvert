# Author: @sleepy4k
# License: MIT License
# Description: A simple number convertion application with Python.
import gui as tkinter
import console as cmd

class Converter:
    # Base contructor
    # @param base: Enum
    # @param config: Array
    # @param translate: Array
    # @return: None
    def __init__(self, base, config, translate):
        self.base = base
        self.config = config
        self.translate = translate

        if self.config["gui"]:
            tkinter.GUI(base, config, translate, self.convertion)
        else:
            cmd.Console(base, config, translate, self.convertion)

    # Convertion function
    # @param base: String
    # @param data: String
    # @return: List
    def convertion(self, base, data):
        match base:
            case self.base.DECIMAL.name:
                decimal = int(data)
            case self.base.BINARY.name:
                decimal = int(data, 2)
            case self.base.OCTAL.name:
                decimal = int(data, 8)
            case self.base.HEXADECIMAL.name:
                decimal = int(data, 16)
            case self.base.ASCII.name:
                decimal = [ord(character) for character in data]
                binary = ' '.join([bin(character)[2:] for character in decimal])
                octal = ' '.join([oct(character)[2:] for character in decimal])
                hexadecimal = ' '.join([hex(character)[2:] for character in decimal])
                asci = ''.join([chr(character) for character in decimal])

                decimal = ' '.join([str(character) for character in decimal])

                return [decimal, binary, octal, hexadecimal, asci]

        binary = bin(decimal)[2:]
        octal = oct(decimal)[2:]
        hexadecimal = hex(decimal)[2:]
        asci = chr(decimal)

        return [decimal, binary, octal, hexadecimal, asci]
