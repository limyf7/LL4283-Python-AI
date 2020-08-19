'''
LimYiFei_PA3_data.csv is a collection of all published public directions and cases downloaded from the PDPC website, as
well as the variables extracted from the cases. Each case was manually reviewed to determine the data for selected
criterias, that were either stated by PDPC guidelines to be a factor in determining finding of breach and fine amount,
or brainstormed as a possible factor that could influence the results.

First, factors that PDPC guidelines stated to be considered when assessing the quantum of fines were extracted into the
dataframe (aggravating, mitigating, remedial, voluntary, meaningful_engagement, admission). The fine amount was recorded
as well. Some factors were not included due to difficulty categorising or quantifying the data, such as the
"seriousness" of the breach, or "sufficient deterrence".

To further elaborate on the factor "seriousness" of the breach, factors that were listed as considerations to determine
the seriousness of the breach are also extracted. This includes (fault, knowledge, extent, persons_affected, appointment
, type_pd). Whether the organisation had previously breached the PDPA was not included, as there are too few data
points. Similarly the "impact" of the organisation's breach was not included. The end result - the type of enforcement
action (fines, directions, or otherwise) was recorded to indicate the "seriousness" of the breach.

Further data such as whether the organisation is a public or private company (type), whether the party is an individual,
society or company(ownership), was recorded as possible variables that may influence the fine amount.

All these variables will be compared against the fine amount, to determine possible correlation between them. However
limitations exist, as many of the criteria were not explicitly listed in the cases, thus some errors in data collection
will be present. For example, even if the case doesn't state that the firm explicitly admitted liability, does
voluntary notification and not disputing the outcome, but merely asking for reduction in fine, count as admission?
If a company sent emails to the victims notifying them of the breach incident, but it was not mentioned whether they
offered "solutions" or whether anyone responded to it, does that count as meaningful engagement? Or even whether to
infer "cooperativeness" from the actions when it was not explicitly stated in the case decision? Cases with unknown
number of persons affected was just put as 1 in the data. In the end this will just be a rough estimation.
'''