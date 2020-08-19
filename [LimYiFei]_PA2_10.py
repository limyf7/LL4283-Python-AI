from os.path import join, expanduser
import pandas as pd

df = pd.read_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), index_col=False)

ac1 = df.Alcohol.quantile(0.05)
ac2 = df.Alcohol.quantile(0.95)

data = {'5%': [ac1], '10%': [ac2]}
percentile = pd.DataFrame(data, index=['alcohol'])
print(percentile)

df.to_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), header=True, index=False)

