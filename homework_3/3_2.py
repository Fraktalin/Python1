# my_list = [12, 3, 4, 10]
# my_list = [1]
# my_list = []
my_list = [12, 3, 4, 10, 8]
if len(my_list) == 0:
    print (my_list)
else:
    last_elem = my_list[-1]
    my_list.pop(-1)
    my_list.insert(0, last_elem)
    print(my_list)