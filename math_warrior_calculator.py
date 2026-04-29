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