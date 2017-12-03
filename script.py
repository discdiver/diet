# this is a python project by Jeff to look at carbs and protein and other data
import pandas as pd

fd = pd.read_csv("USDA_nutritional_data_2017.csv")

print(fd.head(3))
