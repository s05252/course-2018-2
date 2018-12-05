import pandas as pd

dna = "AGTCCGCGAATACAGGCTCGGT"
dna1 = dna.replace("C", "")
dna2 = dna.replace("T", "")
dna_as_series1 = pd.Series(list(dna1), name="genes")
dna_as_series2 = pd.Series(list(dna2), name ="genes")
dna_as_series1.value_counts() + dna_as_series2.value_counts()

alco = pd.read_csv("niaaa-report.csv", index_col=["State", "Year"])
alco["Total"] = alco.Wine + alco.Spirits + alco.Beer
alco.head()

alco_noidx = alco.reset_index()
sum_alco = alco_noidx.groupby("Year").sum()
sum_alco.tail()

alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
alco2009

with_state = alco2009.reset_index()
abbrevs = with_state["State"].map(lambda x : x[:3].upper())
abbrevs.head()

wine_state = alco2009["Wine"] > alco2009["Wine"].mean()
beer_state = alco2009["Beer"] > alco2009["Beer"].mean()
pd.crosstab(wine_state, beer_state)
