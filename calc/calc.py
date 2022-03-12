import random


class Calc:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, numerator, denominator):
        return float(numerator) / denominator

    def random_operation(self, a, b):
        operation_number = random.randint(1, 4)
        if operation_number == 1:
            return self.add(a, b)
        if operation_number == 2:
            return self.subtract(a, b)
        if operation_number == 3:
            return self.multiply(a, b)
        if operation_number == 4:
            return self.divide(a, b)
