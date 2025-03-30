number = int(input("Введіть 5-значне число: "))

digit1 = number % 10
number = number // 10

print(digit1)

digit2 = number % 10
number = number // 10

print(digit2)

digit3 = number % 10
number = number // 10

print(digit3)

digit4 = number % 10
number = number // 10

print(digit4)

digit5 = number % 10

print(digit5)

reversed_number = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5


print(reversed_number)
