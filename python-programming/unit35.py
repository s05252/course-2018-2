import pandas as pd

population = pd.read_csv("population.csv", index_col="State")
population.head()

population.sort_index().head()

population.sort_values("Population").head()

alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
alco2009

alco2009.max()

alco2009.min(axis=1)

dna = "AGTCCGCGAATACAGGCTCGGT"
dna_as_series = pd.Series(list(dna), name="genes")
dna_as_series.head()

dna_as_series.unique()
valid_nucs = list("ACGT")
dna_as_series.isin(valid_nucs).all()