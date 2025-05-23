def difference(*args: int | float) -> float:
    new_list = list(args)
    if len(new_list) == 0:
        return 0
    else:
        sorted_list = sorted(new_list)
        return round(sorted_list[-1] - sorted_list[0],2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
