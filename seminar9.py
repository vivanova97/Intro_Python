import pandas as pd

# Самостоятельная практика №1

# Прочесть с помощью pandas файл california_housing_test.csv
df = pd.read_csv('california_housing_test.csv')
# Посмотреть сколько в нем строк и столбцов
print(df.shape)
# (Доп) Определить какой тип данных имеют столбцы
print(df.dtypes)
# (Доп) Проверить есть ли в файле пустые значения
print(df.isnull().sum())


# Самостоятельная практика №2

# Показать median_house_value где median_income < 2
print(df[df['median_income'] < 2]['median_house_value'])
# (Доп) Показать данные в первых 2 столбцах
print(df[['longitude', 'latitude']])
# (Доп) Выбрать данные где housing_median_age < 20 и median_house_value > 70000
print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])


# Самостоятельная практика №3

# Определить какое максимальное и минимальное значение median_house_value
print(df['median_house_value'].max())
print(df['median_house_value'].min())
# (Доп) Показать максимальное median_house_value, где median_income = 3.1250
print(df[df['median_income'] == 3.1250]['median_house_value'].max())
# (Доп) Узнать какая максимальная population в зоне минимального значения median_house_value
min_house_value = df['median_house_value'].min()
min_house_value_zone = df[df['median_house_value'] == min_house_value]
print(min_house_value_zone['population'].max())
