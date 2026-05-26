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

        buttons = [
            ["AC", "⌫", "(", ")", "%"],
            ["sin(", "cos(", "tan(", "log(", "ln("],
            ["√", "π", "e", "**", "/"],
            ["7", "8", "9", "*", "-"],
            ["4", "5", "6", "+", "Ans"],
            ["1", "2", "3", ".", "="],
            ["0"]
        ]

        actions = {
            "AC": self.clear,
            "⌫": self.backspace,
            "=": self.calculate,
            "√": lambda: self.add("sqrt("),
            "π": lambda: self.add(str(math.pi)),
            "e": lambda: self.add(str(math.e)),
            "Ans": self.use_last_answer
        }

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                cmd = actions.get(text, lambda v=text: self.add(v))

                tk.Button(
                    calculator_frame,
                    text=text,
                    command=cmd,
                    bg="#2b2b2b",
                    fg="white"
                ).grid(row=r + 1, column=c, sticky="nsew")

    def add(self, value):
        self.current_expression += str(value)
        self.update_display()

    def clear(self):
        self.current_expression = ""
        self.update_display()

    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.update_display()

    def use_last_answer(self):
        self.current_expression += str(self.last_answer_value)
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_expression)

    def calculate(self):
        try:
            safe_dict = {
                "__builtins__": None,
                "sin": self.sin_deg,
                "cos": self.cos_deg,
                "tan": self.tan_deg,
                "log": math.log10,
                "ln": math.log,
                "sqrt": math.sqrt,
                "pi": math.pi,
                "e": math.e
            }

            result = eval(self.current_expression, safe_dict)

            self.last_answer_value = result

            self.history.insert(tk.END, f"{self.current_expression} = {result}")

            self.current_expression = str(result)
            self.update_display()

        except Exception as e:
            self.current_expression = "Error"
            self.update_display()
            print("ERROR:", e)
