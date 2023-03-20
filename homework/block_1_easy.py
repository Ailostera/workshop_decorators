"""
1. Написать простую функцию, которая на вход принимает строку ('test') и целое число (3), а возвращает строку вида
'testTESTtest' - исходную строку, умноженную на 3, в разном регистре.
2. Записать эту функцию в произвольную переменную. Напечатать эту переменную на экран. Что вы видите?
3. Вызвать функцию суммирования через переменную, в которую вы только что её записали.
"""


def str_multiply(string: str, number: int) -> str:
    mult_str = ''
    for i in range(number):
        if i % 2 == 0:
            mult_str += string
        else:
            mult_str += string.upper()
    return mult_str


random_var = str_multiply
print(random_var)
# <function str_multiply at 0x7f50fd163d90>

print(random_var('happy', 5))
# happyHAPPYhappyHAPPYhappy
