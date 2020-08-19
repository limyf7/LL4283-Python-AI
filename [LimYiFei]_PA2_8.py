from os.path import join, expanduser
import pandas as pd
import matplotlib.pyplot as plt
from pandas import IntervalIndex

df = pd.read_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), index_col=False)

bins = [25, 30, 35, 40]
plt.hist(df['Age'], bins=bins)
plt.xticks(bins)
plt.xlabel("Age")
plt.ylabel("Number")

plt.show()
