'''
The model appears to have high accuracy, perfect precision, and low recall. All these in combination indicates that
while the model made the correct diagnosis for all the healthy cases (perfect precision), it has a high rate of
misdiagnosing unhealthy cases as healthy, leading to low recall (where the number of people diagnosed only represent a
small part of the unhealthy cases). However since there are very few unhealthy cases compared to healthy cases, it
leads to high accuracy (relatively few people are misdiagnosed overall).

In medical cases, this would not be a useful model, because while cases misdiagnosed as unhealthy (false positive) can
receive attention and perform a second test for confirmation, cases who are misdiagnosed as healthy often result in
complacency, as they are mistaken for one of the many true positives, thus as no second tests are performed. As a
result, the number of cases that are correctly flagged out and removed from the sperm donor pool is very little
compared to the number of cases that will slip through unnoticed. This defeats the purpose of the prediction, which is
to identify as many of the true positives (unhealthy cases) as possible, to maintain the quality of the sperm bank.
As we can see, models with low recall are not useful when there are a lot of true negatives, as the false negative can
easily slip by unnoticed. Especially when mislabelling a positive case as false negative is undesirable.

High accuracy and perfect precision does mean that this model could be more useful in certain scenarios, where the
consequences of mislabelling the data as false positives is far more severe than mislabelling the data as false
negatives. An example could be a model that predicts the "guilt" of a suspect, where, depending on your philosophical
ideals, you may find convicting an innocent of a crime he did not commit far worse than letting a guilty criminal go.
'''