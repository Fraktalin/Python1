import string
import keyword
from itertools import count

my_variable = (input("Введіть назву змінної: "))


starts_with_digit = my_variable[0].isdigit()
has_uppercase = any(c.isupper() for c in my_variable)
has_invalid_char = any((c in string.punctuation.replace("_", "")) or (c.isspace()) for c in my_variable)
is_keyword = my_variable in keyword.kwlist
only_underscores = all(c == "_" for c in my_variable)
more_than_one_underscore = only_underscores and my_variable.count("_") > 1


is_valid = not (
    starts_with_digit or
    has_uppercase or
    has_invalid_char or
    is_keyword or
    more_than_one_underscore
)

print(is_valid)

