def calculator():
    print("Простой калькулятор")
    print("Операции: +, -, *, /")
    try:
        num1 = float(input("Введите первое число: "))
        op = input("Введите операцию: ")
        num2 = float(input("Введите второе число: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Ошибка: деление на ноль!"
        else:
            return "Неверная операция!"
        return f"Результат: {result}"
    except ValueError:
        return "Ошибка: введите числа!"


print(calculator())