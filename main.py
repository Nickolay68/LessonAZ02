import pandas as pd
import numpy as np

# Создание DataFrame
data = {
    'Студент': [f'Ученик {i+1}' for i in range(10)],
    'Русский язык': [5, 4, 3, 4, 5, 4, 3, 5, 4, 5],
    'Математика': [4, 5, 4, 3, 4, 5, 3, 4, 5, 4],
    'Кибернетика': [3, 4, 5, 3, 4, 5, 4, 3, 5, 4],
    'ИТ': [5, 5, 4, 4, 5, 4, 3, 4, 4, 5],
    'Мироустройство': [4, 4, 5, 4, 3, 5, 4, 5, 4, 3]
}

df = pd.DataFrame(data)

# Вывод первых строк DataFrame
print("Первые строки DataFrame:")
print(df.head())

# Вычисление средней оценки по каждому предмету
print("\nСредняя оценка по каждому предмету:")
print(df.mean(numeric_only=True))

# Вычисление медианной оценки по каждому предмету
print("\nМедианная оценка по каждому предмету:")
print(df.median(numeric_only=True))

# Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"\nQ1 для математики: {Q1_math}")
print(f"Q3 для математики: {Q3_math}")
print(f"IQR для математики: {IQR_math}")

# Вычисление стандартного отклонения
print("\nСтандартное отклонение по каждому предмету:")
print(df.std(numeric_only=True))