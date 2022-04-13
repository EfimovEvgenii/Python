import random
import math

class Calculator:
    def random(self):
        print(random.randint(0, 100))

    def upgrade(self, Input_symbol):
        F_number1 = float(input("Введите число: "))
        if Input_symbol == 'MOD':
            print('Ответ: ', math.fabs(F_number1))
        if Input_symbol == '!':
            print('Ответ: ', math.factorial(F_number1))
        if Input_symbol == 'acos':
            c = math.acos(F_number1)
            print('Ответ: ', c)

    def standart(self, Input_symbol):
        F_number = float(input('Введите первое число: '))
        S_number = float(input('Введите второе число: '))
        if Input_symbol == '+':
            print('Ответ: ', F_number + S_number)
        elif Input_symbol == '-':
            print('Ответ: ', F_number - S_number)
        elif Input_symbol == '*':
            print('Ответ: ', F_number * S_number)
        elif Input_symbol == ':':
            if S_number == 0:
                print("Нельзя на нуль делить.")
                return
            print('Ответ: ', F_number / S_number)
        elif Input_symbol == '^':
            print('Ответ: ', pow(F_number, S_number))
