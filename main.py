# Import Modules
import os

# Clear Command
def clear_cmd():
    os.system('cls') if os.name == 'nt' else os.system('clear')

# Seperator
def seperator():
    print("-" * 30)

# Title
def title():
    clear_cmd()
    seperator()
    print("Number Convertion with Python")
    seperator()

# Menu
def menu():
    title()
    print("1. Decimal")
    print("2. Binary")
    print("3. Octal")
    print("4. Hexadecimal")
    print("5. Exit")
    seperator()

# Get Input
def get_input(base):
    title()
    data = input(f"Input your {base} number : ")
    if not data:
        raise ValueError(f"{base} number is required")
    return data

# Error
def error(err):
    seperator()
    print(err)
    seperator()
    choice = input("Do you want to continue? [yes/no] : ")
    init() if choice.lower() in ["yes", "y"] else exit()

# Convertion
def convertion(base, data):
    try:
        if base == 1:
            decimal = int(data)
            binary = bin(decimal)[2:]
            octal = oct(decimal)[2:]
            hexadecimal = hex(decimal)[2:]
        elif base == 2:
            decimal = int(data, 2)
            binary = data
            octal = oct(decimal)[2:]
            hexadecimal = hex(decimal)[2:]
        elif base == 3:
            decimal = int(data, 8)
            binary = bin(decimal)[2:]
            octal = data
            hexadecimal = hex(decimal)[2:]
        elif base == 4:
            decimal = int(data, 16)
            binary = bin(decimal)[2:]
            octal = oct(decimal)[2:]
            hexadecimal = data
        return (decimal, binary, octal, hexadecimal)
    except ValueError:
        error("System has value error")
    except TypeError:
        error("System has data type error")
    except Exception as err:
        error(f"System error: {err}")

# Confirmation
def confirmation(func):
    choice = input("Do you want to try again? [yes/no] : ")
    seperator()
    if choice.lower() in ["yes", "y"]:
        functions = {
            'decimal': decimal,
            'binary': binary,
            'octal': octal,
            'hexadecimal': hexadecimal,
        }
        function = functions.get(func, error)
        function()
    elif choice.lower() in ["no", "n"]:
        init()
    else:
        error("Invalid choice")

# Result
def result(decimal, binary, octal, hexadecimal):
    seperator()
    print(f"Decimal     : {decimal}")
    print(f"Binary      : {binary}")
    print(f"Octal       : {octal}")
    print(f"Hexadecimal : {hexadecimal}")
    seperator()

# Main
def decimal():
    data = get_input("decimal")
    decimal, binary, octal, hexadecimal = convertion(1, data)
    result(decimal, binary, octal, hexadecimal)
    confirmation("decimal")

def binary():
    data = get_input("binary")
    decimal, binary, octal, hexadecimal = convertion(2, data)
    result(decimal, binary, octal, hexadecimal)
    confirmation("binary")

def octal():
    data = get_input("octal")
    decimal, binary, octal, hexadecimal = convertion(3, data)
    result(decimal, binary, octal, hexadecimal)
    confirmation("octal")

def hexadecimal():
    data = get_input("hexadecimal")
    decimal, binary, octal, hexadecimal = convertion(4, data)
    result(decimal, binary, octal, hexadecimal)
    confirmation("hexadecimal")

# Logic
def logic():
    select = input('Select your output : ')
    print('-----------------------------')
    functions = {
        '1': decimal,
        '2': binary,
        '3': octal,
        '4': hexadecimal,
        '5': exit
    }
    function = functions.get(select, error)
    function()

# Init
def init():
    menu()
    logic()

# Run
init()