### Hard
#
# 4. Перенесите глобальный счетчик на уровень объемлющей функции. Будет ли работать наш код? Если да, то как поменялся
# смысл написанного кода? Если нет, то что надо изменить, чтобы всё заработало?

counter_sum = 0


def prepare_sum():
    global counter_sum
    counter_sum += 1

    def make_sum(arg_1, arg_2, arg_3, arg_4, *args, **kwargs):
        my_sum = arg_1 + arg_2 + arg_3 + arg_4
        for i in args:
            my_sum += i
        for j in kwargs.values():
            my_sum += j
        return my_sum
    return make_sum


running_sum = prepare_sum()

print(running_sum(1, 2, 3, 4, 5))  # 15
print(counter_sum)  # 1
print(running_sum(1, 2, 3, 4, 5))
print(counter_sum)  # 1 - счетчик не увеличивается, т.к. не вызывается функция prepare_sum


# вариант 1 - каждый раз явно вызывать prepare_sum
print(prepare_sum()(1, 2, 3, 4, 5))
print(counter_sum)  # 2


# вариант 2 - использовать декоратор


def light_horse(some_func):
    def dark_horse(*args, **kwargs):
        global counter_sum
        counter_sum += 1
        return some_func(*args, **kwargs)
    return dark_horse


@light_horse
def make_sum_2(arg_1, arg_2, arg_3, arg_4, *args, **kwargs):
    my_sum = arg_1 + arg_2 + arg_3 + arg_4
    for i in args:
        my_sum += i
    for j in kwargs.values():
        my_sum += j
    return my_sum


print(make_sum_2(1, 2, 3, 4, 5))  # 15
print(counter_sum)  # 3
print(make_sum_2(1, 2, 3, 4, 5))  # 15
print(counter_sum)  # 4

# не удалось понять, как можно использовать для этой задачи nonlocal и как в этом случае получать значение счётчика,
# приходит в голову только что-то подобное, но вроде бы в задании говорится не про это


def outer():
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        return counter

    return inner


my_counter = outer()
print(my_counter())  #1
print(my_counter())  #2
