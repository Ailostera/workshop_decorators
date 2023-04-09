# 2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае успешного
# выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение функции было
# повторено ещё раз с теми же самыми аргументами, но не более 10 раз. Если после последней попытки функцию так и не
# удастся выполнить успешно, то бросать исключение.
# 2.2 Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции можно было задавать как
# параметр во время декорирования.
from typing import Callable


def take(number_attempts: int):
    def take_function(some_func: Callable) -> Callable:
        def inner(*args, **kwargs):
            attempts = 0
            while attempts != number_attempts:
                try:
                    return some_func(*args, **kwargs)
                except:
                    attempts += 1
            return some_func(*args, **kwargs)
        return inner
    return take_function


@take(5)
def counter(x):
    return 100 / x


print(counter(0))
