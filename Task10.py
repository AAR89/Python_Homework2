# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите число монеток: '))
mincountcoin = 0
for i in range(n):
    x = int(input('Введите 0 или 1: '))
    if x == 0:
        mincountcoin += 1
    elif x != 0 and x != 1:
        print('Вы ввели некорректное число')
        break
print(f'Минимальное количество монет, которое нужно перевернуть - {mincountcoin}' if mincountcoin<n/2 else n-mincountcoin)