import string
my_string = (input("Введіть рядок: "))
cleaned =''
for char in my_string:
    if char not in string.punctuation:
        cleaned += char
cleaned = cleaned.title()
new_string = chr(35) + "".join(cleaned.split())[:140]


print(new_string)