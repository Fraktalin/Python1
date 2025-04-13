import random

rand_list = []
rand_length = random.randint(3,10)

for i in range(rand_length):
    rand_list.append(random.randint(1,9))

print(rand_list)

new_list = [rand_list[0], rand_list[2], rand_list[-2]]

print(new_list)