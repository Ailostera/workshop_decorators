# 7.1 Написать декоратор, который после выполнения функции будет возвращать результат и записывать его в текстовый файл.
from typing import Callable


def writer(file_path: str):
    def take_func(some_func: Callable) -> Callable:
        def inner(*args, **kwargs):
            result = some_func(*args, **kwargs)
            with open(file_path, 'w') as my_file:
                my_file.write(str(result))
            return result
        return inner
    return take_func


@writer('My_file')
def counter(some_obj):
    return some_obj * 3


print(counter('8'))
