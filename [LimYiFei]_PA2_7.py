from os.path import join, expanduser
import pandas as pd

df = pd.read_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), index_col=False)
# df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

with pd.option_context('display.max_columns', 50):
    print(df.describe(include='all'))

df.to_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), header=True, index=False)
