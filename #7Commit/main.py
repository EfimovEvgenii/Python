import Calcul

while True:
    Input_symbol = input('Выберите действие (+/-//:/^/RAN/MOD/!/acos): ')

    if Input_symbol in ('+', '-', '', '^', ':'):
        calc.Calculator.standart(Input_symbol, Input_symbol)
    if Input_symbol in ("MOD", "!", "acos"):
        calc.Calculator.upgrade(Input_symbol, Input_symbol)
    if Input_symbol == "RAN":
        calc.Calculator.random(Input_symbol)
