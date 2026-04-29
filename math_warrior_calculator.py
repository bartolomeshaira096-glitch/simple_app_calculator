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

        # BUTTON LAYOUT
        button_layout = [
            ["AC", "⌫", "(", ")", "%"],
            ["sin", "cos", "tan", "log", "ln"],
            ["√", "π", "e", "**", "/"],
            ["7", "8", "9", "*", "-"],
            ["4", "5", "6", "+", "Ans"],
            ["1", "2", "3", ".", "="],
            ["0"]
        ]

        button_actions = {
            "AC": self.clear_expression,
            "⌫": self.delete_last_character,
            "=": self.calculate_expression,
            "√": lambda: self.insert_expression("math.sqrt("),
            "π": lambda: self.insert_expression(str(math.pi)),
            "e": lambda: self.insert_expression(str(math.e)),
            "power": lambda: self.insert_expression("**"),
            "add": lambda: self.insert_expression("+"),
            "subtract": lambda: self.insert_expression("-"),
            "multiply": lambda: self.insert_expression("*"),
            "divide": lambda: self.insert_expression("/"),
            "modulus": lambda: self.insert_expression("%"),
            "answer": self.insert_last_answer,
            "sine": lambda: self.apply_scientific_function("sin"),
            "cosine": lambda: self.apply_scientific_function("cos"),
            "tangent": lambda: self.apply_scientific_function("tan"),
            "logarithm": lambda: self.apply_scientific_function("log"),
            "natural_log": lambda: self.apply_scientific_function("ln"),
            "zero": lambda: self.insert_expression("0"),
            "one": lambda: self.insert_expression("1"),
            "two": lambda: self.insert_expression("2"),
            "three": lambda: self.insert_expression("3"),
            "four": lambda: self.insert_expression("4"),
            "five": lambda: self.insert_expression("5"),
            "six": lambda: self.insert_expression("6"),
            "seven": lambda: self.insert_expression("7"),
            "eight": lambda: self.insert_expression("8"),
            "nine": lambda: self.insert_expression("9"),
            "decimal": lambda: self.insert_expression("."),
            "open_parenthesis": lambda: self.insert_expression("("),
            "close_parenthesis": lambda: self.insert_expression(")")
        }

        for row_index, row_items in enumerate(button_layout):
            for column_index, button_name in enumerate(row_items):

                button_action = button_actions.get(
                    button_name,
                    lambda value=button_name: self.insert_expression(value)
                )

                tk.Button(
                    calculator_frame,
                    text=button_name,
                    font=("Arial", 10),
                    bg="#2b2b2b",
                    fg="white",
                    command=button_action
                ).grid(
                    row=row_index + 1,
                    column=column_index,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )

        for column_index in range(5):
            calculator_frame.columnconfigure(column_index, weight=1)

        for row_index in range(8):
            calculator_frame.rowconfigure(row_index, weight=1)

    # ---------------- DISPLAY CONTROL ----------------
    def update_expression_display(self):
        self.expression_display.delete(0, tk.END)
        self.expression_display.insert(0, self.current_expression)

    def insert_expression(self, value_to_insert):
        self.current_expression += str(value_to_insert)
        self.update_expression_display()

    def clear_expression(self):
        self.current_expression = ""
        self.update_expression_display()

    def delete_last_character(self):
        self.current_expression = self.current_expression[:-1]
        self.update_expression_display()

    def insert_last_answer(self):
        self.current_expression += str(self.last_answer_value)
        self.update_expression_display()

    # ---------------- CALCULATION ----------------
    def calculate_expression(self):
        try:
            computed_result = eval(self.current_expression)
            self.last_answer_value = computed_result

            self.history_listbox.insert(
                tk.END,
                f"{self.current_expression} = {computed_result}"
            )

            self.current_expression = str(computed_result)
            self.update_expression_display()

        except:
            self.current_expression = "Error"
            self.update_expression_display()

    # ---------------- SCIENTIFIC FUNCTIONS ----------------
    def apply_scientific_function(self, function_name):
        try:
            numeric_value = eval(self.current_expression)

            if function_name == "sin":
                result_value = math.sin(math.radians(numeric_value))
            elif function_name == "cos":
                result_value = math.cos(math.radians(numeric_value))
            elif function_name == "tan":
                result_value = math.tan(math.radians(numeric_value))
            elif function_name == "log":
                result_value = math.log10(numeric_value)
            elif function_name == "ln":
                result_value = math.log(numeric_value)
            else:
                result_value = numeric_value

            self.history_listbox.insert(
                tk.END,
                f"{function_name}({numeric_value}) = {result_value}"
            )

            self.current_expression = str(result_value)
            self.update_expression_display()

        except:
            self.current_expression = "Error"
            self.update_expression_display()

# ---------------- PROGRAM ENTRY POINT ----------------
def main():
    scientific_calculator_application = ScientificCalculatorApplication()
    return scientific_calculator_application

main()



