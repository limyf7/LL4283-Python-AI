'''
Alcohol consumption was recalibrated to start from least consuming frequency, to remove the negative
coefficient. The p value reduced a little, from 0.152 to 0.146. The null hypothesis is that these
variables have no effect on sperm health. There is a 14.6% chance that the data collected will fall
under the value of the collected data. If the significance level is set at 0.15, we can reject the
null hypothesis and conclude that it is not true that alcohol consumption does not have an effect on
sperm health.

Season was recalibrated such that the labels start with the least frequent data point, but it did not work.
Smoking was recalibrated to remove negative values, but did not have much effect, as p value changed from
0.669 to 0.662. Reducing data categories by bins (eg. sitting hours, age) were considered, but was not used
in the end because it significantly increased the p values, likely due to categorisation of data.

The rsquared value was reduced, but reducing the p value was prioritised, as finding a statistically
significant relationship is more important than fitting the graph in an analysis of probabilities. The
standard error did not change much, mostly by 0.01, meaning the accuracy of the sample data representing
the population did not change much.
'''