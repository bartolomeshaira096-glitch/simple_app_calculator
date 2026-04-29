import tkinter as tk
import math

class CalculatorCore:
    def add_numbers(self, first_number, second_number):
        return first_number + second_number
    
    def subtract_numbers(self, first_number, second_number):
        return first_number - second_number
    
    def multiply_numbers(self, first_number, second_number):
        return first_number * second_number
    
    def modulus_numbers(self, first_number, second_number):
        return first_number % second_number
    
    def divide_numbers(self, first_number, second_number):
        if second_number == 0:
            return "Error"
        return first_number / second_number
    
class ScientificCalculatorApplication(CalculatorCore):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Math Warrior Calculator")

        self.window.geometry("380x600")
        self.window.minsize(350, 550)
        self.window.resizable(True, True)

        self.current_expression = ""
        self.last_answer_value = 0

        self.build_user_interface()

        self.window.mainloop()

 # ---------------- UI SETUP ----------------
    def build_user_interface(self):

        self.window.columnconfigure(0, weight=3)
        self.window.columnconfigure(1, weight=2)
        self.window.rowconfigure(0, weight=1)

        calculator_frame = tk.Frame(self.window, bg="#1e1e1e")
        calculator_frame.grid(row=0, column=0, sticky="nsew")

        history_frame = tk.Frame(self.window, bg="#111111")
        history_frame.grid(row=0, column=1, sticky="nsew")

        # DISPLAY
        self.expression_display = tk.Entry(
            calculator_frame,
            font=("Consolas", 22),
            bg="#000000",
            fg="white",
            justify="right"
        )
        self.expression_display.grid(
            row=0,
            column=0,
            columnspan=5,
            sticky="nsew",
            padx=5,
            pady=5
        )

        # HISTORY TITLE
        history_title_label = tk.Label(
            history_frame,
            text="HISTORY",
            bg="#111111",
            fg="white",
            font=("Arial", 12, "bold")
        )
        history_title_label.pack()

        self.history_listbox = tk.Listbox(
            history_frame,
            bg="#1e1e1e",
            fg="white",
            font=("Consolas", 10)
        )
        self.history_listbox.pack(fill="both", expand=True)