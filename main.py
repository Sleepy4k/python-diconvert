# Author: @sleepy4k
# License: MIT License
# Description: A simple number conversion application with Python.
from enum import Enum, auto
import logic as conversion


# Enumerate the base numbers.
class Base(Enum):
    DECIMAL = auto()
    BINARY = auto()
    OCTAL = auto()
    HEXADECIMAL = auto()
    ASCII = auto()


# Application configuration.
CONFIG = {
    "gui": True,
    "cmd_separator": 40,
    "gui_size": (500, 600),
    "gui_resizable": False,
}

# Application translation.
TRANSLATE = {
    "exit": "{}. Exit",
    "error": "System error : {}",
    "input": "Input your {} number or word : ",
    "title": "Simple Number Conversion with Python",
    "prompt": "Do you want to continue? [yes/no] : ",
    "select": "Select your output : ",
    "unknown": "Unsupported operating system",
    "success": "Successfully converted",
    "required": "{} value is required",
    "continue": "Do you want to continue? [yes/no] : ",
    "separator": "-",
    "sub_title": "Number Conversion",
    "invalid_choice": "Invalid choice",
}

# Run the application.
if __name__ == "__main__":
    conversion.Converter(Base, CONFIG, TRANSLATE)
