# ### Easy
#
# 1. Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск функции суммирования.
#
# ### Medium
#
# 1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той, котоая была
# решена для запуска функции суммирования.

from random import randint

counter_sum = 0
counter_sqr = 0
counter_win = 0
counter_deceive = 0


def make_sum(arg_1, arg_2, arg_3, arg_4, *args, **kwargs):
    global counter_sum
    my_sum = arg_1 + arg_2 + arg_3 + arg_4
    for i in args:
        my_sum += i
    for j in kwargs.values():
        my_sum += j
    counter_sum += 1
    return my_sum


def make_sqr(side: int, symbol: str):
    global counter_sqr
    symbol = symbol[0]
    print(f'{symbol + " "}' * side)
    for i in range(side - 2):
        print(f'{symbol}{" " * (2 * side - 3)}{symbol + " "}')
    print(f'{symbol + " "}' * side)
    counter_sqr += 1


def pick_winner(members: dict[int: str]):
    global counter_win
    counter_win += 1
    return members[randint(1, len(members))]


def deceive():
    global counter_deceive
    counter_deceive = randint(1, 1000)


if __name__ == '__main__':
    players = {0: 'John', 1: 'Daenerys', 2: 'Tyrion', 3: 'Melisandre', 4: 'No one'}
    print(make_sum(*players))
    make_sqr(len(players), '@')
    print(f'{pick_winner(players)} wins!', end="\n \n")
    deceive()

    print(f'counter_sum = {counter_sum}')
    print(f'counter_sqr = {counter_sqr}')
    print(f'counter_win = {counter_win}')
    print(f'counter_deceive = {counter_deceive}')



