#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
#Для генерации случайного числа используйте код:

from random import randint
n = randint(1, 1000)
k = int(input("Угадайте целое число от 1 до 1000. Попытка №1 - "))
ATTEMPT = 2
while (k != n) and (ATTEMPT <= 10):
    k = int(input(f"Попытка № {ATTEMPT} (осталось попыток {10-ATTEMPT})  - "))  
    if k < n:
        print("Ваше число меньше, чем загадала программа")
    elif k > n:
        print("Ваше число больше, чем загадала программа")
    else:
        print("Ура! Вы угадали!")
       # print(f'Ваш ответ', k)
       # print(f'Загадала программа', n)
    #k = int(input(f'Повторите {p+1} попытку:')) 
    ATTEMPT += 1  
print ('Извините! Ваш лимит попыток ИСЧЕРПАН!')    