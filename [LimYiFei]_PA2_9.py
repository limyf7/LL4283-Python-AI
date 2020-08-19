from os.path import join, expanduser
import pandas as pd

df = pd.read_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), index_col=False)

a1 = df.Age.quantile(0.05)
a2 = df.Age.quantile(0.95)

s1 = df.Sitting.quantile(0.05)
s2 = df.Sitting.quantile(0.95)

percentile = pd.DataFrame([[a1, a2], [s1, s2]], ["age", "sitting"])
percentile.columns = ["5%", "95%"]

print(percentile)

df.to_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), header=True, index=False)











