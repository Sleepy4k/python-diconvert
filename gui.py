# Author: @sleepy4k
# License: MIT License
# Description: A simple number convertion application with Python.
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox

class GUI:
    # Base contructor
    # @param base: Enum
    # @param config: Array
    # @param translate: Array
    # @param logic: Function
    # @return: None
    def __init__(self, base, config, translate, logic):
        self.base = base
        self.logic = logic
        self.config = config
        self.translate = translate

        self.window = tk.Tk()
        self.window.title(translate["title"])
        self.window.configure(bg="peach puff2")
        self.window.geometry(f"{config['gui_size'][0]}x{config['gui_size'][1]}")
        self.window.resizable(config["gui_resizable"], config["gui_resizable"])

        self.font1 = font.Font(family='helvetica', size=10)
        self.font2 = font.Font(family='helvetica', size=20)
        self.font3 = font.Font(family='helvetica', size=30)

        self.type = tk.StringVar()
        self.value = tk.StringVar()
        self.result = []

        self.create()
        self.form()

        self.window.mainloop()

    # Handle the dropdown form
    # @param event: Void
    # @return: None
    def handle_type(self, event):
        unit = event.widget.get()
        self.type.set(unit)

    #  Handle the submit button
    # @return: Messagebox
    def handle_submit(self):
        unit = self.type.get()
        label = self.value.get()

        if not unit:
            return messagebox.showerror("Error", "Please select a unit")
        elif not label:
            return messagebox.showerror("Error", "Please enter a value")
        elif unit not in [str(base.name) for base in self.base]:
            return messagebox.showerror("Error", "Invalid choice")
        else:
            try:
                convert = self.logic(unit, label)
                self.result = convert
                self.form()
                return messagebox.showinfo("Success", "Successfully converted")
            except ValueError as err:
                return messagebox.showerror("Error", err)
            except TypeError as typeErr:
                return messagebox.showerror("Error", err)
            except Exception as err:
                return messagebox.showerror("Error", err)


    # Create the main window
    # @return: None
    def create(self):
        main = tk.Label(self.window, text=self.translate['sub_title'], bg="peach puff2")
        main['font'] = self.font3
        main.place(relx='0.48', rely='0.1', anchor='center')

        unit = tk.Label(self.window, text="From -:", bg="peach puff2")
        unit['font'] = self.font1
        unit.place(relx='0.24', rely='0.19')

        unit_func = ttk.Combobox(self.window, state='readonly', width=35, textvariable=self.type)
        unit_func['values'] = [base.name for base in self.base]
        unit_func.place(relx='0.57', rely='0.21', anchor='center')
        unit_func.current(0)
        unit_func.bind("<<ComboboxSelected>>", self.handle_type)

        label_from = tk.Label(self.window, text="Value -:", bg="peach puff2")
        label_from['font'] = self.font1
        label_from.place(relx='0.235', rely='0.27')

        label_func = tk.Entry(self.window, width=38, textvariable=self.value)
        label_func.place(relx='0.57', rely='0.287', anchor='center')

        get_answer = tk.Button(self.window, text="Result", bg="cyan2", width=10, command=self.handle_submit)
        get_answer['font'] = self.font1
        get_answer.place(relx='0.46', rely='0.35')


    # Create the result window
    # @return: None
    def form(self):
        result1_label = tk.Label(self.window, text="Decimal -:", bg="peach puff2")
        result1_label['font'] = self.font1
        result1_label.place(relx='0.077', rely='0.48')

        result1 = tk.Label(self.window, text="", bg="white", width=20)
        result1['font'] = self.font2
        result1.place(relx='0.21', rely='0.47')
        result1['text'] = self.result[0] if self.result else ""

        result2_label = tk.Label(self.window, text="Binary -:", bg="peach puff2")
        result2_label['font'] = self.font1
        result2_label.place(relx='0.10', rely='0.58')

        result2 = tk.Label(self.window, text="", bg="white", width=20)
        result2['font'] = self.font2
        result2.place(relx='0.21', rely='0.57')
        result2['text'] = self.result[1] if self.result else ""

        result3_label = tk.Label(self.window, text="Octal -:", bg="peach puff2")
        result3_label['font'] = self.font1
        result3_label.place(relx='0.112', rely='0.68')

        result3 = tk.Label(self.window, text="", bg="white", width=20)
        result3['font'] = self.font2
        result3.place(relx='0.21', rely='0.67')
        result3['text'] = self.result[2] if self.result else ""

        result4_label = tk.Label(self.window, text="Hexadecimal -:", bg="peach puff2")
        result4_label['font'] = self.font1
        result4_label.place(relx='0.025', rely='0.78')

        result4 = tk.Label(self.window, text="", bg="white", width=20)
        result4['font'] = self.font2
        result4.place(relx='0.21', rely='0.77')
        result4['text'] = self.result[3] if self.result else ""

        result5_label = tk.Label(self.window, text="ASCII -:", bg="peach puff2")
        result5_label['font'] = self.font1
        result5_label.place(relx='0.11', rely='0.88')

        result5 = tk.Label(self.window, text="", bg="white", width=20)
        result5['font'] = self.font2
        result5.place(relx='0.21', rely='0.87')
        result5['text'] = self.result[4] if self.result else ""
