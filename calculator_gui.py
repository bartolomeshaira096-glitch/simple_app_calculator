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