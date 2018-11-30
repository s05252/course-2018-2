import pandas as pd
import numpy as np

alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
alco2009

alco2009 = pd.DataFrame([(1.20, 0.22, 0.58),
 (1.31, 0.54, 1.16),
 (1.19, 0.38, 0.74),
 (1.45, 0.22, 1.10)],
 columns = ("Beer", "Wine", "Spirits"),
 index = ("Alabama", "Alaska", "Wisconsin", "Wyoming"))

alco2009 = pd.DataFrame({"Beear" : (1.20, 1.31),
"Wine" : (0.22, 0.54),
"Spirits" : (0.58, 1.16)},
index=("Alabama", "Alaska"))

alco2009["Wine"].head()

alco2009.Beer.tail()

alco2009["Total"] = 0
alco2009.head()

alco2009.columns.values

alco2009.index.values

alco2009.reset_index().set_index("Beer").head()

alco2009.ix["Nebraska"]

"Samoa" in alco2009.index

s_states = [state for state in alco2009.index if state[0] =='S'] + ["Samoa"]

s_states

drinks = list(alco2009.columns) + ["Water"]
drinks

nan_alco = alco2009.reindex(s_states, columns=drinks)
nan_alco

