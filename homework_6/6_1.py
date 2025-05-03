import string

ascii_letters = string.ascii_letters
input_1 = input("Введіть 2 літери через дефіз: ")
splitted = input_1.split("-")
first_letter = ascii_letters.find(splitted[0])
second_letter = ascii_letters.find(splitted[1])
new_string = ''
for i in range(first_letter,second_letter+1):
    new_string += ascii_letters[i]
print(new_string)
