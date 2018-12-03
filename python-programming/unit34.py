import pandas as pd
import numpy as np

alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
alco2009

population = pd.read_csv("population.csv", index_col="State")
population.head()

df = pd.merge(alco2009, population, left_index=True,
right_index=True)
df.head()


