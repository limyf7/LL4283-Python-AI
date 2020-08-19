from os.path import join, expanduser
import pandas as pd
import statsmodels.formula.api as sm

df = pd.read_csv(join(expanduser("~"), "fertility_Diagnosis.csv"), index_col=False)

lm = sm.ols('Diagnosis ~ Season + Age + Disease + Accident + Surgery + Fever + Alcohol + Smoking + Sitting',
            data=df).fit()
print(lm.summary())

# r squared
print("\n" + "rsquared = " + str(lm.rsquared) + "\n")

# coefficient

# standard error
print("standard error = " + "\n" + str(lm.bse) + "\n")

# t-values
print("tvalues = " + "\n" + str(lm.tvalues) + "\n")

# p-values
print("pvalues = " + "\n" + str(lm.pvalues) + "\n")