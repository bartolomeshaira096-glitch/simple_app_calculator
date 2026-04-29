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

# ---------------- SCIENTIFIC FUNCTIONS ----------------
    def sin_deg(self, x):
        return math.sin(math.radians(x))

    def cos_deg(self, x):
        return math.cos(math.radians(x))

    def tan_deg(self, x):
        return math.tan(math.radians(x))

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
            ["sin(", "cos(", "tan(", "log(", "ln("],
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
            "√": lambda: self.insert_expression("sqrt("),
            "π": lambda: self.insert_expression(str(math.pi)),
            "e": lambda: self.insert_expression(str(math.e)),
            "Ans": self.insert_last_answer,
        }

        for row_index, row_items in enumerate(button_layout):
            for column_index, button_name in enumerate(row_items):

                action = button_actions.get(
                    button_name,
                    lambda value=button_name: self.insert_expression(value)
                )

                tk.Button(
                    calculator_frame,
                    text=button_name,
                    font=("Arial", 10),
                    bg="#2b2b2b",
                    fg="white",
                    command=action
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

    def insert_expression(self, value):
        self.current_expression += str(value)
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
            expression = self.current_expression

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

            result = eval(expression, safe_dict)

            self.last_answer_value = result

            self.history_listbox.insert(
                tk.END,
                f"{expression} = {result}"
            )

            self.current_expression = str(result)
            self.update_expression_display()

        except Exception as error:
            self.current_expression = "Error"
            self.update_expression_display()
            print("DEBUG ERROR:", error)

# ---------------- PROGRAM ENTRY POINT ----------------
def main():
    scientific_calculator_application = ScientificCalculatorApplication()
    return scientific_calculator_application

main()



