def common_elements()->set:
    first_range = range(3, 100, 3)
    first_numbers = {0}
    for i in first_range:
        first_numbers.add(i)

    second_range = range(5, 100, 5)
    second_numbers = {0}
    for i in second_range:
        second_numbers.add(i)
    return first_numbers&second_numbers


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

