# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5

num = int(input('Сколько рядов у ёлки? '))
chr_tree_width = num * 2 - 1
stars = 1
for i in range(num):
    print(f"{' '* (num - 1)}{'*' * stars}")
    stars += 2
    num -= 1

# Еще один вариант: форматирование строки, удобно делать таблицы. 
num = int(input('Сколько рядов у ёлки? '))
for i in range(num):
    print(f'{"*" * (2*i+1):/^{(num * 2-1)}}')

    
