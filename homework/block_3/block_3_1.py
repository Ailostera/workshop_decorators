# 1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет показывать
# в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.
# 1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было задавать
# как параметр во время декорирования.
from typing import Callable


def print_it(message: str):
    def take_function(some_func: Callable) -> Callable:
        def inner(*args, **kwargs):
            print(message)
            return some_func(*args, **kwargs)
        return inner
    return take_function


@print_it('Покупайте змей, они меньше едят!')
def counter(number: int):
    return number * 3


print(counter(5))

