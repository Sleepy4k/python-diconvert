# Import Modules
import os

def clearcmd():
    os.system('cls') if os.name == 'nt' else os.system('clear')

def title():
    print("-----------------------------")
    print("Number Convertion with Python")
    print("-----------------------------")

def menu():
    clearcmd()
    title()
    print("1. Decimal")
    print("2. Binary")
    print("3. Octal")
    print("4. Hexadecimal")
    print("5. Exit")
    print("-----------------------------")

def get_input(base):
    data = input(f"Input your {base} number : ")
    if not data:
        raise ValueError(f"{base} number is required")
    return data

def error(err):
    print("-----------------------------")
    print(err)
    print("-----------------------------")
    choice = str(input("Do you want to continue? [yes/no] : "))
    init() if choice.lower() in ["yes", "y"] else exit()

def convertion(base, data):
    try:
        if base == 1:
            decimal = int(data)
            binary = bin(decimal).replace("0b", "")
            octal = oct(decimal).replace("0o","")
            hexadecimal = hex(decimal).replace("0x","")
        elif base == 2:
            binary = int(data, 2)
            decimal = int(data, 2)
            octal = oct(decimal).replace("0o","")
            hexadecimal = hex(decimal).replace("0x","")
        elif base == 3:
            octal = int(data, 8)
            decimal = int(data, 8)
            binary = bin(decimal).replace("0b","")
            hexadecimal = hex(decimal).replace("0x","")
        elif base == 4:
            hexadecimal = data
            decimal = int(data, 16)
            binary = bin(decimal).replace("0b","")
            octal = oct(decimal).replace("0o","")
        return (decimal, binary, octal, hexadecimal)
    except ValueError:
        error("System has value error")
    except TypeError:
        error("System has data type error")
    except Exception as err:
        error(f"System error: {err}")

def confirmation(func):
    choice = input("Do you want to try again? [yes/no] : ")
    if choice.lower() in ["yes", "y"]:
        func()
    elif choice.lower() in ["no", "n"]:
        init()
    else:
        error("Invalid choice")

def result(decimal, binary, octal, hexadecimal):
    print("-----------------------------")
    print(f"Decimal     : {decimal}")
    print(f"Binary      : {binary}")
    print(f"Octal       : {octal}")
    print(f"Hexadecimal : {hexadecimal}")
    print("-----------------------------")

def decimal():
    data = get_input("decimal")
    decimal, binary, octal, hexadecimal = convertion(1, data)
    result(decimal, binary, octal, hexadecimal)
    confirmation(decimal)

def binary():
    data = get_input("binary")
    decimal, binary, octal, hexadecimal = conversion(2, data)
    result(decimal, binary, octal, hexadecimal)
    confirmation(binary)

def octal():
    data = get_input("octal")
    decimal, binary, octal, hexadecimal = conversion(3, data)
    result(decimal, binary, octal, hexadecimal)
    confirmation(octal)

def hexadecimal():
    data = get_input("hexadecimal")
    decimal, binary, octal, hexadecimal = conversion(4, data)
    result(decimal, binary, octal, hexadecimal)
    confirmation(hexadecimal)

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

def init():
    menu()
    logic()

init()