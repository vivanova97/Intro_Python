import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

df = pd.read_csv('Practice5_data.csv', sep=',')

sb.scatterplot(data = df, x = 'experience', y = 'salary')

plt.show()

# cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
# g = sb.PairGrid(df[cols])
# g.map(sb.scatterplot)

df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Young'
