# Author: @sleepy4k
# License: MIT License
# Description: A simple number convertion application with Python.
from enum import Enum
import logic as convertion

# Enumerate the base numbers.
class Base(Enum):
    DECIMAL = 1
    BINARY = 2
    OCTAL = 3
    HEXADECIMAL = 4
    ASCII = 5

# Application configuration.
CONFIG = {
    "separator": 40,
}

# Application translation.
TRANSLATE = {
    "exit": "{}. Exit",
    "error": "System error : {}",
    "input": "Input your {} number or word : ",
    "title": "Simple Number Convertion with Python",
    "prompt": "Do you want to continue? [yes/no] : ",
    "select": "Select your output : ",
    "unknown": "Unsupported operating system",
    "required": "{} number is required",
    "continue": "Do you want to continue? [yes/no] : ",
    "separator": "-",
    "invalid_choice": "Invalid choice",
}

# Run the application.
if __name__ == "__main__":
    convertion.Converter(Base, CONFIG, TRANSLATE)
