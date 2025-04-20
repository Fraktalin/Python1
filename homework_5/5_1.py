import string
import keyword
from itertools import count

# my_variable = "_"
# my_variable = "__"
# my_variable = "___"
# my_variable = "x"
# my_variable = "get_value"
# my_variable = "get value"
# my_variable = "get!value"
# my_variable = "some_super_puper_value"
# my_variable = "Get_value"
# my_variable = "get_Value"
# my_variable = "getValue"
# my_variable = "3m"
# my_variable = "m3"
# my_variable = "assert"
my_variable = "assert_exception"


starts_with_digit = my_variable[0].isdigit()
has_uppercase = any(c.isupper() for c in my_variable)
has_invalid_char = any(c in string.punctuation.replace("_", "") or c.isspace() for c in my_variable)
is_keyword = my_variable in keyword.kwlist
more_than_one_underscore = my_variable.count("_") > 1
print(string.punctuation)
is_valid = not (
    starts_with_digit or
    has_uppercase or
    has_invalid_char or
    is_keyword or
    more_than_one_underscore
)

print(is_valid)