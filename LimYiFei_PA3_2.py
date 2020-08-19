import pandas as pd
import statsmodels.formula.api as sm
from LimYiFei_PA3_1 import StatisticalMeasures, Accuracy, Precision, Recall

df = pd.read_csv("/Users/limyifei/Downloads/fertility_Diagnosis.csv", header=None)
df.columns = ["season", "age", "disease", "accident", "surgery", "fever", "alcohol", "smoking", "sitting", "diagnosis"]

# recalibration
df["season"] = df["season"].astype('category')
df["fever"] = df["fever"].astype('category')
df["smoking"] = df["smoking"].astype('category')
df["diagnosis"].replace(["N", "O"], [int(0), int(1)], inplace=True)

# categorical variables
print("season")
print(df["season"].value_counts().sort_index())

print("\n" + "fever")
print(df["fever"].value_counts().sort_index())

print("\n" + "smoking")
print(df["smoking"].value_counts().sort_index())
print('\n')

# quantitative  variables
df_qt = df.loc[:, ['age','disease','accident','surgery','alcohol','sitting']]
with pd.option_context('display.max_columns', 50):
    print(df_qt.describe())
    print('\n')

# logistic regression model
lg = sm.logit(formula='diagnosis ~ season + age + disease + accident + surgery + fever + alcohol + smoking + sitting',
              data=df).fit()
df["diagnosis_hat"] = lg.predict(df)
predictedOutput = list(df["diagnosis_hat"])
actualOutput = list(df["diagnosis"])

print(lg.summary())
print('accuracy: ' + str('%1.4f' % (Accuracy(predictedOutput, actualOutput))))
print('precision: ' + str('%1.4f' % (Precision(predictedOutput, actualOutput))))
print('recall: ' + str('%1.4f' % (Recall(predictedOutput, actualOutput))))
