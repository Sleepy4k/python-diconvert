# Author: @sleepy4k
# License: MIT License
# Description: A simple number conversion application with Python.
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox


class GUI:
    _result = []  # Protected Variable
    _type = None  # Protected Variable
    __base = None  # Private Variable
    _logic = None  # Protected Variable
    _font1 = None  # Protected Variable
    _font2 = None  # Protected Variable
    _font3 = None  # Protected Variable
    _value = None  # Protected Variable
    _translate = {}  # Protected Variable
    __window = None  # Private Variable

    # Base constructor
    # @param base: Enum
    # @param config: Array
    # @param translate: Array
    # @param logic: Function
    # @return: None
    def __init__(self, base, config, translate, logic):
        self.__base = base
        self._logic = logic
        self._translate = translate

        self.__window = tk.Tk()
        self.__window.title(translate["title"])
        self.__window.configure(bg="peach puff2")
        self.__window.geometry(f"{config['gui_size'][0]}x{config['gui_size'][1]}")
        self.__window.resizable(config["gui_resizable"], config["gui_resizable"])

        self._font1 = font.Font(family='helvetica', size=10)
        self._font2 = font.Font(family='helvetica', size=20)
        self._font3 = font.Font(family='helvetica', size=30)

        self._type = tk.StringVar()
        self._value = tk.StringVar()
        self._result = []

        self.__create()
        self.__form()

        self.__window.mainloop()

    # Handle the dropdown form
    # @param event: Void
    # @return: None
    def __handle_type(self, event):
        unit = event.widget.get()
        self._type.set(unit)

    #  Handle the submit button
    # @return: Messagebox
    def __handle_submit(self):
        unit = self._type.get()
        label = self._value.get()

        if not unit:
            return messagebox.showerror("Error", self._translate["required"].format("Type"))
        elif not label:
            return messagebox.showerror("Error", self._translate["required"].format("Number"))
        elif unit not in [str(base.name) for base in self.__base]:
            return messagebox.showerror("Error", self._translate["invalid_choice"])
        else:
            try:
                convert = self._logic(unit, label)
                self._result = convert
                self.__form()

                return messagebox.showinfo("Success", self._translate["success"])
            except ValueError as valueErr:
                return messagebox.showerror("Error", valueErr)
            except TypeError as typeErr:
                return messagebox.showerror("Error", typeErr)
            except Exception as err:
                return messagebox.showerror("Error", err)

    # Create the main window
    # @return: None
    def __create(self):
        main = tk.Label(self.__window, text=self._translate['sub_title'], bg="peach puff2")
        main['font'] = self._font3
        main.place(relx='0.48', rely='0.1', anchor='center')

        unit = tk.Label(self.__window, text="Type -:", bg="peach puff2")
        unit['font'] = self._font1
        unit.place(relx='0.24', rely='0.19')

        unit_func = ttk.Combobox(self.__window, state='readonly', width=35, textvariable=self._type)
        unit_func['values'] = [base.name for base in self.__base]
        unit_func.place(relx='0.57', rely='0.21', anchor='center')
        unit_func.current(0)
        unit_func.bind("<<ComboboxSelected>>", self.__handle_type)

        label_from = tk.Label(self.__window, text="Number -:", bg="peach puff2")
        label_from['font'] = self._font1
        label_from.place(relx='0.205', rely='0.27')

        label_func = tk.Entry(self.__window, width=38, textvariable=self._value)
        label_func.place(relx='0.57', rely='0.287', anchor='center')

        get_answer = tk.Button(self.__window, text="Result", bg="cyan2", width=10, command=self.__handle_submit)
        get_answer['font'] = self._font1
        get_answer.place(relx='0.46', rely='0.35')

    # Create the result window
    # @return: None
    def __form(self):
        enum = [enums.name for enums in self.__base]

        if "DECIMAL" in enum:
            decimal_label = tk.Label(self.__window, text="Decimal -:", bg="peach puff2")
            decimal_label['font'] = self._font1
            decimal_label.place(relx='0.077', rely='0.48')

            decimal = tk.Label(self.__window, text="", bg="white", width=20)
            decimal['font'] = self._font2
            decimal.place(relx='0.21', rely='0.47')
            decimal['text'] = self._result[0] if self._result else ""
        if "BINARY" in enum:
            binary_label = tk.Label(self.__window, text="Binary -:", bg="peach puff2")
            binary_label['font'] = self._font1
            binary_label.place(relx='0.10', rely='0.58')

            binary = tk.Label(self.__window, text="", bg="white", width=20)
            binary['font'] = self._font2
            binary.place(relx='0.21', rely='0.57')
            binary['text'] = self._result[1] if self._result else ""
        if "OCTAL" in enum:
            octal_label = tk.Label(self.__window, text="Octal -:", bg="peach puff2")
            octal_label['font'] = self._font1
            octal_label.place(relx='0.112', rely='0.68')

            octal = tk.Label(self.__window, text="", bg="white", width=20)
            octal['font'] = self._font2
            octal.place(relx='0.21', rely='0.67')
            octal['text'] = self._result[2] if self._result else ""
        if "HEXADECIMAL" in enum:
            hexadecimal_label = tk.Label(self.__window, text="Hexadecimal -:", bg="peach puff2")
            hexadecimal_label['font'] = self._font1
            hexadecimal_label.place(relx='0.025', rely='0.78')

            hexadecimal = tk.Label(self.__window, text="", bg="white", width=20)
            hexadecimal['font'] = self._font2
            hexadecimal.place(relx='0.21', rely='0.77')
            hexadecimal['text'] = self._result[3] if self._result else ""
        if "ASCII" in enum:
            ascii_label = tk.Label(self.__window, text="ASCII -:", bg="peach puff2")
            ascii_label['font'] = self._font1
            ascii_label.place(relx='0.11', rely='0.88')

            ascii = tk.Label(self.__window, text="", bg="white", width=20)
            ascii['font'] = self._font2
            ascii.place(relx='0.21', rely='0.87')
            ascii['text'] = self._result[4] if self._result else ""
