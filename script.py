# this is a python project by Jeff to look at carbs and protein and other data
import pandas as pd

fd = pd.read_csv("USDA_nutritional_data_2017.csv")

# print(fd.head(3))

print(fd.shape)

max_carbs = fd['Carbohydrt_(g)'].max()
fd['normalized_carbs'] = fd['Carbohydrt_(g)'] / max_carbs
print(fd['normalized_carbs'])

print(fd.sort_values('normalized_carbs', ascending = False).head(3))
