from os.path import join, expanduser
import pandas as pd

df = pd.read_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), index_col=False)

df["Diagnosis"].replace(["N", "O"], [0, 1], inplace=True)
print(df["Diagnosis"].value_counts().sort_index())

df.to_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), header=True, index=False)
