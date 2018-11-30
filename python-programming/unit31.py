import pandas as pd
import numpy 

inflation = pd.Series((2.2, 3.4, 2.8, 1.6, 2.3, 2.7, 3.4, 3.2, 2.8, 3.8, -0.4, 1.6, 3.2, 2.1, 1.5, 1.5))
print(inflation)

len(inflation)

inflation.values

inflation.index

inflation.index.values

inflation.values[-1] = 1.6

inflation.index = pd.Index(range(1999, 2015))

inflation[2015] = numpy.nan

inflation.head()

inflation.tail()

