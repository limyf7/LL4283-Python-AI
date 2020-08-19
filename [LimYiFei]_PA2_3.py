from os.path import join, expanduser
import pandas as pd

df = pd.read_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), index_col=False)

df.Age = ((df.Age + 1) * 18).astype(int)
print(df["Age"].value_counts().sort_index())

df.to_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), header=True, index=False)
