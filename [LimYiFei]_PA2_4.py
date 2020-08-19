from os.path import join, expanduser
import pandas as pd

df = pd.read_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), index_col=False)

df["Fever"].replace([1, 0, -1], [0, 1, 2], inplace=True)
df["Fever"].astype(str)
print(df["Fever"].value_counts().sort_index())

df.to_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), header=True, index=False)
