# 1. Написать функцию, которая на вход будет принимать произвольное количество аргументов и возвращать их сумму.
# 2. В сигнатуре функции объявить 4 обязательных аргумента, но оставить возможность передавать в неё сколько угодно
# дополнительных аргументов. Попробуйте вызвать функцию в следующих ситуациях и объясните результат:
#    - прокинуть в функцию только 1 аргумент
#    - прокинуть аргументы таким образом, чтобы обязательный аргумент был передан одновременно позиционно и по ключу
#    - создать кортеж со значениями и распаковать его при вызове функции с помощью *
#    - создать словарь со значениями и распаковать его при вызове функции с помощью * и **: что наблюдаете? Почему?


def make_sum(arg_1, arg_2, arg_3, arg_4, *args, **kwargs):
    my_sum = arg_1 + arg_2 + arg_3 + arg_4
    for i in args:
        my_sum += i
    for j in kwargs.values():
        my_sum += j
    return my_sum

if False:
    make_sum(1)
# TypeError: make_sum() missing 3 required positional arguments: 'arg_2', 'arg_3', and 'arg_4'
    make_sum(1, 2, 3, 4, arg_2=5)
# TypeError: make_sum() got multiple values for argument 'arg_2'


numbers = (10, 20)
print(make_sum(1, 2, 3, 4, *numbers))
# 40

strings = {'one, ': 'hello, ', 'two, ': 'my ', 'three': 'friend'}
print(make_sum('I ', 'came ', 'to ', 'say: ', *strings))
# I came to say: one, two, three (словарь перебирается по ключам -> ключи упаковываются в args)

print(make_sum('I ', 'came ', 'to ', 'say: ', **strings))
# I came to say: hello, my friend
