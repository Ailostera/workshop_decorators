# 3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с
# которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
# 3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической
# очистки кэша в процессе выполнения функций.
# 3.3 Параметризовать время кэширования в декораторе.

from typing import Callable
from datetime import datetime
from time import sleep

cash = {}


def take_time(seconds: int|float):
    def cash_decorator(some_func: Callable) -> Callable:
            def inner(*args, **kwargs):
                args_for_search = tuple([*args] + [value for value in kwargs.values()])
                if args_for_search in cash and datetime.timestamp(datetime.now()) - cash[args_for_search][1] <= seconds:
                    cash[args_for_search][1] = datetime.timestamp(datetime.now())
                    return cash[args_for_search][0]
                else:
                    result = some_func(*args, **kwargs)
                    cash[args_for_search] = [result, datetime.timestamp(datetime.now())]
                    return result
            return inner
    return cash_decorator


@take_time(3)
def counter(some_obj, number: int):
    return some_obj * number


print(counter(5, number=3))  # 15
print(cash)  # {(5, 3): [15, 1681075787.754072]}
print(counter(8, number=2))  # 16
print(cash)  # {(5, 3): [15, 1681075787.754072], (8, 2): [16, 1681075787.754179]}
sleep(5)
print(counter(5, number=3))  #15
print(cash)  # {(5, 3): [15, 1681075792.758361], (8, 2): [16, 1681075787.754179]}
