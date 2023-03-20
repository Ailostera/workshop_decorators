# 1. Модифицировать функцию таким образом, чтобы для суммирования брались только обязательные аргументы,
# первые 2 аргумента из дополнительных позиционных аргументов и любой аргумент из дополнительных аргументов (если они есть),
# переданных по ключу (если они есть).


from random import choice


def make_sum(arg_1, arg_2, arg_3, arg_4, *args, **kwargs):
    my_sum = arg_1 + arg_2 + arg_3 + arg_4
    for i in args[:2]:
        my_sum += i
    my_sum += choice([*kwargs.values()])
    return my_sum


strings_1 = ('take a ', 'choice: ', 'how ', 'you ', 'want ', 'to ', 'die ')
strings_2 = {'one, ': 'SCARY', 'two, ': 'VERY SCARY', 'three': 'NOT SCARY AT ALL'}

print(make_sum('I ', 'came ', 'to ', 'ask you ', *strings_1, **strings_2))
