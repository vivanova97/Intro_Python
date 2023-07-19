import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_categories = list(set(lst))

one_hot_data = pd.DataFrame()

for category in unique_categories:
    one_hot_data[category] = [1 if item == category else 0 for item in lst]

data = pd.DataFrame(one_hot_data)
print(data.head())