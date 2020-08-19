from os.path import join, expanduser
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(join(expanduser("~"), "LimYiFei_PA_3_data.csv"), index_col=False)

# graph 1: fine_lg vs persons_affected_lg
x = df["persons_affected_lg"]
y = df["fine_lg"]
plt.scatter(x, y)

plt.title('Scatter plot of amount of fine against number of persons affected')
plt.xlabel('Persons affected (log10)')
plt.ylabel('Fine (log10)')
plt.show()

'''
From this graph, there's somewhat a linear relationship between the variables fine_lg and persons_affected_lg. While
it can be expected that the higher the number of persons affected, the more severe the offence and thus the higher the
amount of fine awarded, it is interesting to note that the data includes all persons at risk of having their data
leaked, not just those who suffered actual harm as a result of the breach. As such, it appears that proving risk of 
harm is sufficient, which makes sense as PDPA is primarily an ex ante deterrent, acting to prevent such breaches. 
'''

# graph 2:
x = df["voluntary"]
y = df["fine_lg"]
plt.scatter(x, y)

plt.title('Scatter plot of fine amount against voluntary notification')
plt.xlabel('Voluntary notification')
plt.ylabel('Fine (log10)')
plt.show()

'''
It appears that there is no significant difference in fine amount, between cases initiated by 3P complaints (0), by 
PDPC investigation (1), or by voluntary notification (2). Although the fine amount appears to have a lower ceiling in 
cases initiated by voluntary notification, it could be explained by the category having fewer data points overall. This
possibly shows that despite 'voluntary notification' being listed as a criteria for considering fine amounts, PDPC 
still prioritise assessing the severity of breach with other criteria to determine fine amount. 
'''