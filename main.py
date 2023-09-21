import math


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Кто делит на 0?"


def exponentiation(a, b):
    return a ** b


def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Нельзя извлечь квадратный корень из отрицательного числа:("


def factorial(a):
    if a >= 0:
        return math.factorial(a)
    else:
        return "Нельзя вычислить факториал отрицательного числа:("


def sine(a):
    return math.sin(a)


def cosine(a):
    return math.cos(a)


def tangent(a):
    return math.tan(a)


def validate_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Другую цифру впиши")


def validate_operation_input(prompt, valid_operations):
    while True:
        operation = input(prompt)
        if operation in valid_operations:
            return operation
        else:
            print("давай другую операцию")


valid_operations = ['+', '-', '*', '/', '^', 'sqrt', '!', 'sin', 'cos', 'tan']

print("Дароу!")

while True:
    operation = validate_operation_input("Выбери че будет (+, -, *, /, ^, sqrt, !, sin, cos, tan): ",
                                         valid_operations)

    if operation in ['+', '-', '*', '/', '^']:
        num1 = validate_number_input("Го первую цифру: ")
        num2 = validate_number_input("А теперь вторую: ")

        if operation == '+':
            result = addition(num1, num2)
        elif operation == '-':
            result = subtraction(num1, num2)
        elif operation == '*':
            result = multiplication(num1, num2)
        elif operation == '/':
            result = division(num1, num2)
        elif operation == '^':
            result = exponentiation(num1, num2)

    elif operation in ['sqrt', '!']:
        num1 = validate_number_input("Введите цифорку: ")

        if operation == 'sqrt':
            result = square_root(num1)
        elif operation == '!':
            result = factorial(num1)

    elif operation in ['sin', 'cos', 'tan']:
        num1 = validate_number_input("Введите цифорку: ")

        if operation == 'sin':
            result = sine(num1)
        elif operation == 'cos':
            result = cosine(num1)
        elif operation == 'tan':
            result = tangent(num1)

    print("Результат:", result)

    choice = input("Мне кажется ты понял(a) не до конца? (да/нет): ")
    if choice.lower() != 'да':
        break

print("Согласись, калькулятор топ!")