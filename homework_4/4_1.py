# my_list = [0, 1, 0, 12, 3]
# my_list =[0]
# my_list =[1, 0, 13, 0, 0, 0, 5]
my_list =[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]



count_of_zero = my_list.count(0)
for i in range(count_of_zero):
    my_list.remove(0)
    my_list.append(0)
print(my_list)
