number1 = int(input("Введіть перше число: "))
sign = (input("Введіть дію над двома числами: "))
number2 = int(input("Введіть друге число: "))

if sign == '+':
    print(number1 + number2)
elif sign == '-':
    print(number1 - number2)
elif sign == '*':
    print(number1 * number2)
elif sign == '/' and number2 != 0:
    print(number1 / number2)
else:
    print('Помилка - другий дільник дорівнює 0')