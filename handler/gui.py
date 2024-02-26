import tkinter as tk
from config import CONFIG
from tkinter import ttk, messagebox, font as tkFont

class GUI:
  # Define protected variables
  _result = []
  _type = None
  _logic = None
  _font1 = None
  _font2 = None
  _font3 = None
  _value = None
  _translate = {}

  # Define private variables
  __config = {}
  __base = None
  __window = None

  def __init__(self, base, logic):
    """
    Base constructor
    :param base: Enum
    :param logic: Function
    :return: None
    """

    self.__base = base
    self.__config = CONFIG["GUI"]

    self._logic = logic
    self._translate = CONFIG["lang"]

    self.__window = tk.Tk()
    self.__window.configure(bg = "peach puff2")
    self.__window.title(self._translate["title"])
    self.__window.resizable(self.__config["resizable"], self.__config["resizable"])
    self.__window.geometry(f"{self.__config['size'][0]}x{self.__config['size'][1]}")

    self._font1 = tkFont.Font(family = "helvetica", size = 10)
    self._font2 = tkFont.Font(family = "helvetica", size = 20)
    self._font3 = tkFont.Font(family = "helvetica", size = 30)

    self._result = []
    self._type = tk.StringVar()
    self._value = tk.StringVar()

    self.__form()
    self.__create()

    self.__window.mainloop()

  def __handle_type(self, event):
    """
    Handle the dropdown form
    :param event: Void
    :return: None
    """

    unit = event.widget.get()
    self._type.set(unit)

  def __handle_submit(self):
    """
    Handle the submit button
    :return: Messagebox
    """

    unit = self._type.get()
    label = self._value.get()

    if not unit:
      return messagebox.showerror("Error", self._translate["required"].format("Type"))
    elif not label:
      return messagebox.showerror("Error", self._translate["required"].format("Number"))
    elif unit not in [str(base.name) for base in self.__base]:
      return messagebox.showerror("Error", self._translate["invalid_choice"])
    elif "-" in label:
      return messagebox.showerror("Error", self._translate["error"].format("Negative numbers are not supported."))
    else:
      try:
        convert = self._logic(unit, label)
        self._result = convert
        self.__form()
      except ValueError as valueErr:
        return messagebox.showerror("Error", valueErr)
      except TypeError as typeErr:
        return messagebox.showerror("Error", typeErr)
      except Exception as err:
        return messagebox.showerror("Error", err)

  def __create(self):
    """
    Create the form
    :return: None
    """

    main = tk.Label(self.__window, text = self._translate["sub_title"], bg = "peach puff2")
    main["font"] = self._font3
    main.place(relx = "0.48", rely = "0.1", anchor = "center")

    unit = tk.Label(self.__window, text = "Type -:", bg = "peach puff2")
    unit["font"] = self._font1
    unit.place(relx = "0.24", rely = "0.19")

    unit_func = ttk.Combobox(self.__window, state = "readonly", width = 35, textvariable = self._type)
    unit_func["values"] = [base.name for base in self.__base]
    unit_func.place(relx = "0.57", rely = "0.21", anchor = "center")
    unit_func.current(0)
    unit_func.bind("<<ComboboxSelected>>", self.__handle_type)

    label_from = tk.Label(self.__window, text = "Number -:", bg = "peach puff2")
    label_from["font"] = self._font1
    label_from.place(relx = "0.205", rely = "0.27")

    label_func = tk.Entry(self.__window, width = 38, textvariable = self._value)
    label_func.place(relx = "0.57", rely = "0.287", anchor = "center")

    get_answer = tk.Button(self.__window, text = "Result", bg = "cyan2", width = 10, command = self.__handle_submit)
    get_answer["font"] = self._font1
    get_answer.place(relx = "0.46", rely = "0.35")

  def __form(self):
    """
    Create the result window
    :return: None
    """

    enum = [enums.value for enums in self.__base]

    if 10 in enum:
      decimal_label = tk.Label(self.__window, text = "Decimal -:", bg = "peach puff2")
      decimal_label["font"] = self._font1
      decimal_label.place(relx = "0.077", rely = "0.48")

      decimal_col = tk.Label(self.__window, text = None, bg = "white", width = 20)
      decimal_col["font"] = self._font2
      decimal_col.place(relx = "0.21", rely = "0.47")
      decimal_col["text"] = self._result[0] if self._result else None

    if 2 in enum:
      binary_label = tk.Label(self.__window, text = "Binary -:", bg = "peach puff2")
      binary_label["font"] = self._font1
      binary_label.place(relx = "0.10", rely = "0.58")

      binary_col = tk.Label(self.__window, text = None, bg = "white", width = 20)
      binary_col["font"] = self._font2
      binary_col.place(relx = "0.21", rely = "0.57")
      binary_col["text"] = self._result[1] if self._result else None

    if 8 in enum:
      octal_label = tk.Label(self.__window, text = "Octal -:", bg = "peach puff2")
      octal_label["font"] = self._font1
      octal_label.place(relx = "0.112", rely = "0.68")

      octal_col = tk.Label(self.__window, text = None, bg = "white", width = 20)
      octal_col["font"] = self._font2
      octal_col.place(relx = "0.21", rely = "0.67")
      octal_col["text"] = self._result[2] if self._result else None

    if 16 in enum:
      hexa_label = tk.Label(self.__window, text = "Hexadecimal -:", bg = "peach puff2")
      hexa_label["font"] = self._font1
      hexa_label.place(relx = "0.025", rely = "0.78")

      hexa_col = tk.Label(self.__window, text = None, bg = "white", width = 20)
      hexa_col["font"] = self._font2
      hexa_col.place(relx = "0.21", rely = "0.77")
      hexa_col["text"] = self._result[3] if self._result else None

    if 256 in enum:
      ascii_label = tk.Label(self.__window, text = "ASCII -:", bg = "peach puff2")
      ascii_label["font"] = self._font1
      ascii_label.place(relx = "0.11", rely = "0.88")

      ascii_col = tk.Label(self.__window, text = None, bg = "white", width = 20)
      ascii_col["font"] = self._font2
      ascii_col.place(relx = "0.21", rely = "0.87")
      ascii_col["text"] = self._result[4] if self._result else None
