from os.path import join, expanduser
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/limyifei/Downloads/LimYiFei_PA_3_data.csv")
df = df.drop(['Index'], axis=1)

# removes data where fine = 0
df = df[df.fine != 0]

# apply logarithmic transformation
df['fine_lg'] = df['fine'].apply(np.log10)
df['persons_affected_lg'] = df['persons_affected'].apply(np.log10)

# list of variables
attribute = list(df)

# creating list of quant/qual of variables
v_cat = []
v_quant = ['fine', 'fine_lg', 'type_pd', 'persons_affected', 'persons_affected_lg', 'extent']

for v in attribute:
    if v in v_quant:
        v_cat.append('quant')
    else:
        v_cat.append('qual')

# determining parameters of variables
def minmax(variable):
    min = df[variable].min()
    max = df[variable].max()
    if max == int(max):
        return str(min) + ' to ' + str(max)
    else:
        return str('{:.2f}'.format(min)) + ' to ' + str('{:.2f}'.format(max))

v_parameters = []
for v in attribute:
    v_parameters.append(minmax(v))

# describing variables
v_description = ['Total amount of fine to be paid in decision',
                 'The number of persons whose data is at risk or leaked, =1 if unknown',
                 '0 = Non-sensitive personal data, 1 = Sensitive personal data',
                 '0 = Private organisation, 1 = Publicly listed companies',
                 '0 = Individual, 1 = Society or NPO, 2 = Company',
                 'Number of section of PDPA breached',
                 '0 = Not deliberate or wilful, 1 = Done deliberately',
                 '0 = Did not know risk of serious breach, 1 = Ought to have known risk of serious breach',
                 '0 = DPO not appointed, 1 = DPO appointed, 2 = Not stated',
                 '0 = No admission of liability, 1 = Admission of liability',
                 '0 = Case initiated by 3P complaint, 1 = Case initiated by PDPC investigation, 2 = Case initiated by'
                 ' voluntary notification',
                 '0 = No remedial actions taken or mentioned, 1 = Remedial actions taken',
                 '0 = No meaningful engagement with victims, 1 = Meaningful engagement with victims',
                 '0 = Not cooperative, 1 = Cooperative, 2 = Not mentioned',
                 '0 = No aggravating factors mentioned, 1 = Has aggravating factors',
                 '0 = No steps taken to prevent further breach, 1 = Mitigative steps taken',
                 'logarithmic transformation on fine',
                 'logarithmic transformation on persons affected']

# printing the table
column = ['attribute', 'qual/quant', 'parameters', 'description/recalibrated']
table = [list(a) for a in zip(attribute, v_cat, v_parameters, v_description)]
table.insert(0, column)

row_format = "{:<25} {:<15} {:<15} {:<60}"
for item in table:
    print(row_format.format(*item))

df.to_csv(join(expanduser("~"), "LimYiFei_PA_3_data.csv"), header=True, index=False)