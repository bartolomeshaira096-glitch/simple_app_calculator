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