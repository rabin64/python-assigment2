#17. Write a program that serves as a basic calculator. It asks for two
#numbers, then it asks for an operator. Gracefully deal with input that
#doesn't cleanly convert to numbers. Deal with division by zero errors.

class Calculator:
    def __init__(self, num1, num2, operator):
        try:
            num1 = int(num1)
            num2 = int(num2)
            self.number1 = num1
            self.number2 = num2
        except ValueError:
            raise ValueError('Enter integers only. ')
        self.operator = operator

    def calculate(self):
        operators = {
            '+': self.add(),
            '-': self.subtract(),
            '*': self.multiply(),
            '/': self.divide()
        }
        return operators.get(self.operator)

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        try:
            result = self.number1 / self.number2
        except ZeroDivisionError:
            result = 0
        return result


first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')
operator = input('Enter the one operator among: + , - , / , *  ')
obj1 = Calculator(first_number, second_number, operator)
print(obj1.calculate())