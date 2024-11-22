'''. Описание и агрегация данных в DataFrame:

Напишите программу, которая:
- Запрашивает у пользователя количество строк данных для ввода.
- Для каждой строки запрашивает данные по трем столбцам: "Имя", "Возраст", "Регион", разделённые пробелом.
- Создаёт DataFrame на основе введённых данных.
- Выводит общую информацию о DataFrame, включая количество записей, средний возраст, и количество уникальных регионов.
- Выбирает и выводит на экран данные о самом молодом участнике.

Пример вывода:

Введите количество строк: 3  
Введите данные (Имя Возраст Регион): Анна 25 Берлин  
Введите данные (Имя Возраст Регион): Борис 30 Гамбург  
Введите данные (Имя Возраст Регион): Света 22 Мюнхен  

Общая информация:  
Количество записей: 3  
Средний возраст: 25.67  
Количество уникальных регионов: 3  

Данные о самом молодом участнике:  
Имя: Света  
Возраст: 22  
Регион: Сочи '''

import pandas as pd
import numpy as np

count_rows = int(input('Введите количество строк: '))

df_agg = pd.DataFrame(columns=['Имя', 'Возраст', 'Регион'])

for i in range(count_rows):
    data_list = input(f'Введите данные {i+1} (Имя Возраст Регион): ').split(' ')
    data_list[1]=int(data_list[1])
    df_agg.loc[i]=data_list


print('\nОбщая информация: ')
print(f'Количество записей: {count_rows}')
print(f'Средний возраст: {df_agg['Возраст'].mean()}')
print(f'Количество уникальных регионов: {df_agg['Регион'].nunique()} \n')

print('Даннные о самом молодом участнике: ')

idx=df_agg.loc[(df_agg['Возраст'] == df_agg['Возраст'].min()), 'Имя']


print(f'Имя: {df_agg.loc[(df_agg['Возраст'] == df_agg['Возраст'].min()), 'Имя']}')
print(f'Возраст: {df_agg.loc[(df_agg['Возраст'] == df_agg['Возраст'].min()), 'Возраст']}')
print(f'Регион: {df_agg.loc[(df_agg['Возраст'] == df_agg['Возраст'].min()), 'Регион']}')