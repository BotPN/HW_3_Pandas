'''2. Чтение из файла и группировка

Имеется [файл](https://drive.google.com/file/d/1uf1XpRGe_xhvQmX8Hyyq_XImy9UV1tDU/view) с данными о продажах фруктов в нескольких магазинах компании. 
Напишите программу для определения:
- Самого прибыльного магазинах.
- Самого популярного вида фруктов.
- Постройте точеченый график (scatter-plot) для столбцов Количество и Цена. Проанализируйте смысл этого графика.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('sales_data.csv')

data['Итого'] = data['Количество'] * data['Цена']

profit_store=data.groupby('Магазин')['Итого'].sum()
most_profit_store=profit_store.idxmax()

print(f'Прибыльный магазин: {most_profit_store}')

populer_fruit=data.groupby('Фрукт')['Количество'].sum()
most_populer_fruit=populer_fruit.idxmax()

print(f'Самый популярный фрукт: {most_populer_fruit}')

count_fruit = np.array(data['Количество'])
price_fruits = np.array(data['Цена'])

plt.scatter([1,2,3], [4,5,6])
plt.show()

