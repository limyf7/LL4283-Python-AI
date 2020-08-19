from os.path import join, expanduser
import pandas as pd

df = pd.read_csv("/Users/limyifei/Downloads/fertility_Diagnosis.csv", header=None)
df.columns = ["Season", "Age", "Disease", "Accident", "Surgery", "Fever", "Alcohol", "Smoking", "Sitting", "Diagnosis"]

print(df.iloc[:5], "\n\n", df.iloc[-5:])

df.to_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), header=True, index=False)