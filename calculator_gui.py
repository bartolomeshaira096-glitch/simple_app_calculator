import tkinter as tk
import math
from calculator_core import CalculatorCore
from scientific_calculator import ScientificCalculator

class CalculatorGUI(CalculatorCore, ScientificCalculator):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Math Warrior Calculator")

        self.window.geometry("380x600")
        self.window.minsize(350, 550)
        self.window.resizable(True, True)

        self.current_expression = ""
        self.last_answer_value = 0

        self.build_ui()
        self.window.mainloop()

    def build_ui(self):
        self.window.columnconfigure(0, weight=3)
        self.window.columnconfigure(1, weight=2)
        self.window.rowconfigure(0, weight=1)

        calculator_frame = tk.Frame(self.window, bg="#1e1e1e")
        calculator_frame.grid(row=0, column=0, sticky="nsew")

        history_frame = tk.Frame(self.window, bg="#111111")
        history_frame.grid(row=0, column=1, sticky="nsew")

        self.display = tk.Entry(
            calculator_frame,
            font=("Consolas", 22),
            bg="black",
            fg="white",
            justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew")

        self.history = tk.Listbox(
            history_frame,
            bg="#1e1e1e",
            fg="white"
        )
        self.history.pack(fill="both", expand=True)
