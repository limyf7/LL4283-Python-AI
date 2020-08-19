from os.path import join, expanduser
import pandas as pd

df = pd.read_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), index_col=False)

df.Sitting = df.Sitting * 24
print(df["Sitting"].value_counts().sort_index())


