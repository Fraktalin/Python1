# my_list = [1, 2, 3, 4, 5, 6]
# my_list = [1, 2, 3]
# my_list = [1, 2, 3, 4, 5]
my_list = [1]
# my_list = []
if not my_list:
    result = [[], []]
else:
    half = (len(my_list) + 1) // 2
    result = [my_list[:half], my_list[half:]]

print(result)