from enum import Enum

class DataType(Enum):
  DECIMAL = (1, 10)
  BINARY = (2, 2)
  OCTAL = (3, 8)
  HEXADECIMAL = (4, 16)
  ASCII = (5, 256)
