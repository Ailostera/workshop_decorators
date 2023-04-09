from collections.abc import Callable
from datetime import datetime


def time_it(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return inner


def writer(file_path: str):
    def take_func(some_func: Callable) -> Callable:
        def inner(*args, **kwargs):
            result = some_func(*args, **kwargs)
            with open(file_path, 'w') as my_file:
                my_file.write(str(result))
            return result
        return inner
    return take_func


@time_it
@writer('My_file')
def counter(some_obj):
    return some_obj * 3


@writer('My_file_2')
@time_it
def counter_2(some_obj):
    return some_obj * 3


print(counter(5))  # time_it(writer('My_file')(counter))(5)
#  0:00:00.001142
#  15
print(counter_2(5))  # writer(My_file_2)(time_it(counter_2))(5)
# 0:00:00.000057
# 15
