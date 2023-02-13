# Import Modules
from os import replace, system

def menu():
    system('cls')

    print('-----------------------------')
    print('Number Convertion with Python')
    print('-----------------------------')
    print('1. Decimal')
    print('2. Binary')
    print('3. Octal')
    print('4. Hexadecimal')
    print('5. Exit')
    print('-----------------------------')

def error(error = 'Output not available!'):
    print('-----------------------------')
    print(error)
    print('-----------------------------')
    
    choice = input('Do you want to continue? [yes/no] : ')

    if choice == 'yes' or choice == 'y':
        init()
    elif choice == 'no' or choice == 'n':
        exit()
    else:
        error()

def confirmation(func):
    choice = input('Do you want to try again? [yes/no] : ')

    if choice == 'yes' or choice == 'y':
        if func == 'decimal':
            decimal()
        elif func == 'binary':
            binary()
        elif func == 'octal':
            octal()
        elif func == 'hexadecimal':
            Hexadecimal()
    elif choice == 'no' or choice == 'n':
        init()
    else:
        error()

def result(decimal, binary, octal, hexadecimal):
    print('-----------------------------')
    print('Decimal     : ', decimal)
    print('Binary      : ', binary)
    print('Octal       : '. octal)
    print('Hexadecimal : ', hexadecimal)
    print('-----------------------------')

def decimal():
    try:
        decimal = int(input('Input your decimal number : '))
    except ValueError:
        error('The number does not match')

    binary = bin(decimal).replace('0b','')
    octal = oct(decimal).replace('0o','')
    hexadecimal = hex(decimal).replace('0x','')

    result(decimal, binary, octal, hexadecimal)
    error('decimal')

def binary():
    try:
        binary = input('Input your binary number : ')
    except ValueError:
        error('The number does not match')

    decimal = int(binary, 2)
    octal = oct(binary).replace('0o', '')
    hexadecimal = hex(binary).replace('0x', '')
    
    result(decimal, binary, octal, hexadecimal)
    error('binary')

def octal():
    try:
        binary = input('Input your octal number : ')
    except ValueError:
        error('The number does not match')

    decimal = int(binary, 2)
    octal = oct(binary).replace('0o', '')
    hexadecimal = hex(binary).replace('0x', '')
    
    result(decimal, binary, octal, hexadecimal)
    error('octal')

def hexadecimal():
    try:
        binary = input('Input your hexadecimal number : ')
    except ValueError:
        error('The number does not match')

    decimal = int(binary, 2)
    octal = oct(binary).replace('0o', '')
    hexadecimal = hex(binary).replace('0x', '')
    
    result(decimal, binary, octal, hexadecimal)
    error('hexadecimal')

def logic():
    select = input('Select your output : ')
    print('-----------------------------')

    if select == '1':
        decimal()
    elif select == '2':
        binary()
    elif select == '3':
        octal()
    elif select == '4':
        hexadecimal()
    elif select == '5':
        exit()
    else:
        error()

def init():
    menu()
    logic()

init()