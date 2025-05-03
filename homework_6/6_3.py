input_1 = str(input("Введіть число: "))

def multiply(n):
    new_number = 1
    for i in n:
        new_number*=int(i)
    if new_number <=9:
        return new_number
    else:
       return multiply(str(new_number))

print(multiply(input_1))