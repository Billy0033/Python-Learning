import pandas as pd
import numpy as np

'''Задача 2 Раздел 3
Для каждой задачи необходимо создать Data Frame c колонками [A, B, C], заполненный случайными
числами. Data Frame должен иметь 30 строк. Элементы в колонке A могут принимать только
значения в интервале [0,10].
2. Для каждого значения в столбце А найти сумму всех значений столбца B'''

data = {
        'A':np.random.randint(0,11,30),
        'B':np.random.randint(0,10000,30),
        'C':np.random.randint(0,10000,30),
        }
df = pd.DataFrame(data)

df_2 = df.groupby('A')['B'].sum()
print(df_2)
