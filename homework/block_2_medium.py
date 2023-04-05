# 2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться в качестве
# результата работы из объемлющей функции.
# 3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную. Напечатайте результат на экран.
# Что наблюдаете?
# 4. Осуществите вызов функции суммирования из полученной переменной.


from random import randint

counter_sum = 0


def prepare_sum():
    def make_sum(arg_1, arg_2, arg_3, arg_4, *args, **kwargs):
        global counter_sum
        my_sum = arg_1 + arg_2 + arg_3 + arg_4
        for i in args:
            my_sum += i
        for j in kwargs.values():
            my_sum += j
        counter_sum += 1
        return my_sum
    return make_sum


running_sum = prepare_sum()
print(running_sum)
# <function prepare_sum.<locals>.make_sum at 0x7f559cb89ea0>

print(running_sum(1, 2, 3, 4, 5))
# 15

print(counter_sum)
#1

print(running_sum(1, 2, 3, 4, 5))
# 15

print(counter_sum)
#2


