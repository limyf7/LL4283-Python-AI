from os.path import join, expanduser
import pandas as pd

df = pd.read_csv(join(expanduser("~"), "LimYiFei_PA_3_data.csv"), index_col=False)

attribute = list(df)

# create list of categorical variables
v_cat = []
v_quant = ['fine', 'type_pd', 'persons_affected', 'extent', 'fine_lg', 'persons_affected_lg']
vquant_df = df[v_quant].copy()

for v in attribute:
    if v in v_quant:
        continue
    else:
        v_cat.append(v)

# print value count for categorical variables
for v in v_cat:
    print(v)
    print(df[v].value_counts().sort_index())
    print('\n')

# print data analysis for non-categorical variables
with pd.option_context('display.max_columns', 50):
    print(vquant_df.describe(include='all'))