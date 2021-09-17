import csv
import pandas as pd
df=pd.read_csv("stars.csv")
print(df.columns)
del df["Luminosity"]
del df["Unnamed: 6"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
print(df.shape)
print(df.columns)
df.to_csv("finalstars.csv")