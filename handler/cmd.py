import os
from config import CONFIG

class CMD:
  # Define protected variables
  _logic = None
  _translate = {}

  # Define private variables
  __config = {}
  __base = None

  def __init__(self, base, logic):
    """
    Base constructor
    :param base: Enum
    :param logic: Function
    :return: None
    """

    self.__base = base
    self.__config = CONFIG["CMD"]

    self._logic = logic
    self._translate = CONFIG["lang"]

    self.__create()

  def __clear_cmd(self, os_name):
    """
    Clears the command prompt
    :param os_name: String
    :return: None
    """

    os_name = os_name.lower()

    if os_name == "nt": os.system("cls")
    elif os_name == "posix": os.system("clear")
    else: print(self._translate["unknown"])

  def __separator(self):
    """
    Prints a separator line
    :return: None
    """

    print(self.__config["separator"] * self.__config["separator_length"])

  def __title(self):
    """
    Prints the application title
    :return: None
    """

    self.__clear_cmd(os.name)
    self.__separator()
    print(self._translate["title"])
    self.__separator()

  def __menu(self):
    """
    Prints the menu options
    :return: None
    """

    self.__title()

    for base in self.__base:
      print(f"{base.value[0]}. {base.name}")

    print(self._translate["exit"].format(len(self.__base) + 1))
    self.__separator()

  def __get_input(self, base):
    """
    Prompts the user for input data
    :param base: Enum
    :return: String
    """

    self.__title()
    data = input(self._translate["input"].format(base.name.lower()))

    if not data: raise ValueError(self._translate["required"].format(base.name.lower()))

    return data

  def __error(self, err):
    """
    Handles errors and prompts the user to continue or exit
    :param err: String
    :return: Boolean
    """

    self.__separator()
    print(self._translate["error"].format(err))
    self.__separator()

    choice = input(self._translate["prompt"])

    if choice.lower() in ["yes", "y"]: return True
    elif choice.lower() in ["no", "n"]: return False
    else: return self.__error(self._translate["invalid_choice"])

  def __conversion(self, base, data):
    """
    Converts the input data to decimal and other bases
    :param base: Enum
    :param data: String
    :return: None
    """

    status = False

    try: return self._logic(base.name, data)
    except ValueError as valErr: status = self.__error(valErr)
    except TypeError as typeErr: status = self.__error(typeErr)
    except Exception as err: status = self.__error(err)

    if not status: return self.__create()
    else: self.__main(base)

  def __retry(self, base):
    """
    Prompts the user to continue or exit
    :param base: Enum
    :return: None
    """

    choice = input(self._translate["continue"])
    self.__separator()

    if choice.lower() in ["yes", "y"]: self.__main(base)
    elif choice.lower() in ["no", "n"]: self.__create()
    else:
      status = self.__error(self._translate["invalid_choice"])

      if not status: self.__create()
      else: self.__main(base)

  def __main(self, base):
    """
    Main application
    :param base: Enum
    :return: None
    """

    try:
      data = self.__get_input(base)
      conversions = self.__conversion(base, data)
      self.__separator()

      enum = [enums.value[0] for enums in self.__base]

      if 1 in enum: print(f"Decimal     : {conversions[0]}")
      if 2 in enum: print(f"Binary      : {conversions[1]}")
      if 3 in enum: print(f"Octal       : {conversions[2]}")
      if 4 in enum: print(f"Hexadecimal : {conversions[3]}")
      if 5 in enum: print(f"ASCII       : {conversions[4]}")

      self.__separator()
      self.__retry(base)
    except ValueError as err:
      print(err)
      self.__error(err)

  def __create(self):
    """
    Creates the application
    :return: None
    """

    self.__menu()
    select = input(self._translate["select"])
    self.__separator()

    length = len(self.__base) + 1

    if int(select) == length:
      exit()
    elif int(select) > 0 and int(select) < length:
      base = [base for base in self.__base if base.value[0] == int(select)][0]
      self.__main(base)
    else:
      status = self.__error(self._translate["invalid_choice"])
      self.__create() if status else exit()
