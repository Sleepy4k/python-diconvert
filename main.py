# Import Modules
import os
from enum import Enum

# Class
class Base(Enum):
    DECIMAL = 1
    BINARY = 2
    OCTAL = 3
    HEXADECIMAL = 4
    ASCII = 5

# Clear Command
def clear_cmd():
    os.system("cls") if os.name == "nt" else os.system("clear")

# separator
def separator():
    print("-" * 30)

# Title
def title():
    clear_cmd()
    separator()
    print("Number Convertion with Python")
    separator()

# Menu
def menu():
    title()
    for base in Base:
        print(f"{base.value}. {base.name}")
    print(f"{len(Base)+1}. Exit")
    separator()

# Get Input
def get_input(base):
    title()
    data = input(f"Input your {base.name.lower()} number : ")
    if not data:
        raise ValueError(f"{base.name.lower()} number is required")
    return data

# Error
def error(err):
    separator()
    print(err)
    separator()
    choice = input("Do you want to continue? [yes/no] : ")
    if choice.lower() in ["yes", "y"]:
        logic()
    elif choice.lower() in ["no", "n"]:
        exit()
    else:
        error("Invalid choice")

# Convertion
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
                decimal = [ord(character) for character in data]
                binary = ''.join([bin(character)[2:] for character in decimal])
                octal = ''.join([oct(character)[2:] for character in decimal])
                hexadecimal = ''.join([hex(character)[2:] for character in decimal])
                asci = ''.join([chr(character) for character in decimal])

                # Convert to string
                decimal = ''.join([str(character) for character in decimal])
                return (decimal, binary, octal, hexadecimal, asci)
            case _:
                error("Invalid base")
        binary = bin(decimal)[2:]
        octal = oct(decimal)[2:]
        hexadecimal = hex(decimal)[2:]
        asci = chr(decimal)
        return (decimal, binary, octal, hexadecimal, asci)
    except ValueError:
        error("System has value error")
    except TypeError:
        error("System has data type error")
    except Exception as err:
        error(f"System error: {err}")

# Confirmation
def confirmation(base):
    choice = input("Do you want to try again? [yes/no] : ")
    separator()
    if choice.lower() in ["yes", "y"]:
        main(base)
    elif choice.lower() in ["no", "n"]:
        logic()
    else:
        error("Invalid choice")

# Result
def result(decimal, binary, octal, hexadecimal, asci):
    separator()
    print(f"Decimal     : {decimal}")
    print(f"Binary      : {binary}")
    print(f"Octal       : {octal}")
    print(f"Hexadecimal : {hexadecimal}")
    print(f"ASCII       : {asci}")
    separator()

# Main
def main(base):
    data = get_input(base)
    decimal, binary, octal, hexadecimal, asci = convertion(base, data)
    result(decimal, binary, octal, hexadecimal, asci)
    confirmation(base)

# Logic
def logic():
    menu()
    select = input('Select your output : ')
    separator()
    if select == str(len(Base)+1):
        exit()
    elif select not in [str(base.value) for base in Base]:
        error("Invalid choice")
    else:
        main(Base(int(select)))

# Run
logic()
