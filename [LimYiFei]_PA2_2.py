from os.path import join, expanduser
import pandas as pd

df = pd.read_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), index_col=False)

df["Season"].replace([-1, -0.33, 0.33, 1], [1, 2, 3, 4], inplace=True)
print(df["Season"].value_counts().sort_index())

df.to_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), header=True, index=False)