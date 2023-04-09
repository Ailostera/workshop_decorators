# Задача 6
#
# 6.1 Написать декоратор, который будет запрашивать у пользователя пароль при попытке функции осуществить вызов. Если
# введён верный пароль, то функция будет выполнена и вернется результат её работы. Если нет - в консоли появляется
# соответствующее сообщение.
# 6.2 Параметризовать декоратор таким образом, чтобы можно было задавать индивидуальный пароль для каждой декорируемой
# функции.

from typing import Callable


def take_password(password: str):
    def take_function(some_func: Callable) -> Callable:
        def inner(*args, **kwargs):
            enter_pass = input('Введите пароль: ')
            if enter_pass == password:
                return some_func(*args, **kwargs)
            return 'Неверный пароль'
        return inner
    return take_function


@take_password('qwerty')
def counter(number: int):
    return number * 3


print(counter(3))
