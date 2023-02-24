# Author: @sleepy4k
# License: MIT License
# Description: A simple number convertion application with Python.
import os
from enum import Enum

# Enumerate the base numbers.
class Base(Enum):
    DECIMAL = 1
    BINARY = 2
    OCTAL = 3
    HEXADECIMAL = 4
    ASCII = 5

# Clears the command prompt.
def clear_cmd():
    os.system("cls") if os.name == "nt" else os.system("clear")

# Prints a separator line.
def separator():
    print("-" * 30)

# Prints the application title.
def title():
    clear_cmd()
    separator()
    print("Simple Number Convertion with Python")
    separator()

# Prints the menu options.
def menu():
    title()
    for base in Base:
        print(f"{base.value}. {base.name}")
    print(f"{len(Base) + 1}. Exit")
    separator()

# Prompts the user for input data.
def get_input(base):
    title()
    data = input(f"Input your {base.name.lower()} number or word : ")
    if not data:
        raise ValueError(f"{base.name.lower()} number is required")
    return data

# Handles errors and prompts the user to continue or exit.
def error(err):
    separator()
    print(f"System error : {err}")
    separator()
    choice = input("Do you want to continue? [yes/no] : ")
    if choice.lower() in ["yes", "y"]:
        return True
    elif choice.lower() in ["no", "n"]:
        logic()
    else:
        return error("Invalid choice")

# Converts the input data to decimal and other bases.
def convertion(base, data):
    try:
        match base:
            case Base.DECIMAL:
                decimal = int(data)
            case Base.BINARY:
                decimal = int(data, 2)
            case Base.OCTAL:
                decimal = int(data, 8)
            case Base.HEXADECIMAL:
                decimal = int(data, 16)
            case Base.ASCII:
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
        error(valErr)
    except TypeError as typeErr:
        error(typeErr)
    except Exception as err:
        error(err)
    """Return the result."""
    return main(base)

# Prompts the user to retry or exit.
def retry(base):
    choice = input("Do you want to try again? [yes/no] : ")
    separator()
    if choice.lower() in ["yes", "y"]:
        main(base)
    elif choice.lower() in ["no", "n"]:
        logic()
    else:
        error("Invalid choice")
        return retry(base)

# Main logic.
def main(base):
    try:
        data = get_input(base)
        conversions = convertion(base, data)
        separator()
        print(f"Decimal     : {conversions[0]}")
        print(f"Binary      : {conversions[1]}")
        print(f"Octal       : {conversions[2]}")
        print(f"Hexadecimal : {conversions[3]}")
        print(f"ASCII       : {conversions[4]}")
        separator()
        retry(base)
    except ValueError as err:
        error(err)
        main(base)

# Initial Logic
def logic():
    menu()
    select = input('Select your output : ')
    separator()
    if select == str(len(Base) + 1):
        exit()
    elif select not in [str(base.value) for base in Base]:
        error("Invalid choice")
    else:
        main(Base(int(select)))

# Run the application.
logic()
