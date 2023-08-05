# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код:

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT) 
print(num)
print("Попробуйте угадать число: ")


def guess_number(count):
    attempts = 10
    answer = int(input(f"\nПопытка № {count}. Введите число: "))

    if count < attempts:
        if answer > num:
            print("\nМеньше! ")
            return guess_number(count + 1)
        elif answer < num:
            print("\nБольше!")
            return guess_number(count + 1)
        elif answer == num:
            print("\nВы угадали!")
    else:
        print("попытки закончились. Вы не угадали число...")

count = 1
guess_number(count)
