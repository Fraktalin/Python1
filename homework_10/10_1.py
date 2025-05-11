from typing import Callable, Generator
def pow(x:int) -> int:
    return x ** 2

def some_gen(begin: int, end: int, func: Callable[[int], int]) -> Generator[int, None, None]:
    value = begin
    for i in range(end):
        yield value
        value = func(value)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
