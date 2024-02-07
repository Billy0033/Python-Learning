import numpy as np
import random
'''Задача 3 Раздел 2 
    Создать массив случайных чисел. Для некоторого случайного значения n найти ближайшее
значение в массиве.
'''

list = [np.random.randint(1, 5) for i in range(5)]
n = np.random.randint(10)

def find_nearest(list, n):
    list = np.asarray(list)
    index = (np.abs(list - n)).argmin()
    return list[index]

print(list)
print(n)
print(find_nearest(list, n))