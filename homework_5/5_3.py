my_string = (input("Введіть рядок: "))
my_string = my_string.title()
new_string = chr(35) + "".join(my_string.split())[:140]

print(new_string)