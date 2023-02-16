# Import Modules
import os
from enum import Enum

# Class
class Base(Enum):
    DECIMAL = 1
    BINARY = 2
    OCTAL = 3
    HEXADECIMAL = 4

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
        if base == Base.DECIMAL:
            decimal = int(data)
        elif base == Base.BINARY:
            decimal = int(data, 2)
        elif base == Base.OCTAL:
            decimal = int(data, 8)
        elif base == Base.HEXADECIMAL:
            decimal = int(data, 16)
        else:
            error("Invalid base")
        binary = bin(decimal)[2:]
        octal = oct(decimal)[2:]
        hexadecimal = hex(decimal)[2:]
        return (decimal, binary, octal, hexadecimal)
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
def result(decimal, binary, octal, hexadecimal):
    separator()
    print(f"Decimal     : {decimal}")
    print(f"Binary      : {binary}")
    print(f"Octal       : {octal}")
    print(f"Hexadecimal : {hexadecimal}")
    separator()

# Main
def main(base):
    data = get_input(base)
    decimal, binary, octal, hexadecimal = convertion(base, data)
    result(decimal, binary, octal, hexadecimal)
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