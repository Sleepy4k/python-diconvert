from enums import ENUMS
from config import CONFIG, change_lang

class Base:
  # Define protected variables
  _config = {}

  # Define private variables
  __base = None

  def __init__(self, config):
    """
    Base constructor
    :return: None
    """

    self.__base = ENUMS["data_type"]

    if config.get("lang") is None: config["lang"] = CONFIG["lang"]
    elif config.get("lang").get("default") is None: config["lang"]["default"] = CONFIG["lang"]["default"]
    else:
      change_lang(config["lang"]["default"])
      self._config["lang"] = CONFIG["lang"]

    from handler import HANDLER

    if CONFIG["output"].value == 1: HANDLER["gui"](self.__base, self.__conversion)
    else: HANDLER["cmd"](self.__base, self.__conversion)

  def __conversion(self, base, data):
    """
    Converts the data to the specified base
    :param base: String
    :param data: String
    :return: List
    """

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

if __name__ == "__main__": print("Please run main.py instead. Thank you.")
