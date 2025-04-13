# my_list = [1, 3, 5]
# my_list = [6]
my_list = []

result = 0
length = len(my_list)
if length:
    for i in range(0,length,2):
        result += my_list[i]
    result = result * my_list[-1]
print(result)
