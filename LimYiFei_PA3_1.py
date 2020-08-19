from os.path import join, expanduser
import pandas as pd
import statsmodels.formula.api as sm

df = pd.read_csv("/Users/limyifei/Downloads/fertility_Diagnosis.csv", header=None)
df.columns = ["Season", "Age", "Disease", "Accident", "Surgery", "Fever", "Alcohol", "Smoking", "Sitting", "Diagnosis"]

# recalibration
df["Season"].replace([-1, -0.33, 0.33, 1], [1, 2, 3, 4], inplace=True)
df.Age = ((df.Age + 1) * 18).astype(int)
df["Fever"].replace([1, 0, -1], [0, 1, 2], inplace=True)
df.Sitting = df.Sitting * 24
df["Diagnosis"].replace(["N", "O"], [0, 1], inplace=True)
df["Smoking"].replace([-1, 0, 1], [1, 2, 3], inplace=True)
df["Alcohol"].replace([0.2, 0.4, 0.6, 0.8, 1.0], [5, 4, 3, 2, 1], inplace=True)

# linear model
lm = sm.ols('Diagnosis ~ Season + Age + Disease + Accident + Surgery + Fever + Alcohol + Smoking + Sitting', data=df).fit()
df["Diagnosis_hat"] = lm.predict(df)

predictedOutput = list(df["Diagnosis_hat"])
actualOutput = list(df["Diagnosis"])

# function
def StatisticalMeasures(predictedOutput, actualOutput):
	truePositives = 0
	trueNegatives = 0
	falsePositives = 0
	falseNegatives = 0

	for i in range(len(actualOutput)):
		if predictedOutput[i] < 0.5 and actualOutput[i] == 0:
			trueNegatives += 1
		elif predictedOutput[i] >= 0.5 and actualOutput[i] == 0:
			falsePositives += 1
		elif predictedOutput[i] >= 0.5 and actualOutput[i] == 1:
			truePositives += 1
		elif predictedOutput[i] < 0.5 and actualOutput[i] == 1:
			falseNegatives += 1

	return [truePositives, trueNegatives, falsePositives, falseNegatives]

def Accuracy(predictedOutput, actualOutput):
	truePositives = StatisticalMeasures(predictedOutput, actualOutput)[0]
	trueNegatives = StatisticalMeasures(predictedOutput, actualOutput)[1]

	try:
		accuracyValue = (truePositives + trueNegatives)/len(actualOutput)
	except ZeroDivisionError:
		return print('zero division error')

	return accuracyValue

def Precision(predictedOutput, actualOutput):
	truePositives = StatisticalMeasures(predictedOutput, actualOutput)[0]
	falsePositives = StatisticalMeasures(predictedOutput, actualOutput)[2]

	try:
		precisionValue = truePositives/(truePositives + falsePositives)
	except ZeroDivisionError:
		return print('zero division error')

	return precisionValue


def Recall(predictedOutput, actualOutput):
	falseNegatives = StatisticalMeasures(predictedOutput, actualOutput)[3]
	truePositives = StatisticalMeasures(predictedOutput, actualOutput)[0]

	try:
		recallValue = truePositives/(truePositives + falseNegatives)
	except ZeroDivisionError:
		return print('zero division error')

	return recallValue
