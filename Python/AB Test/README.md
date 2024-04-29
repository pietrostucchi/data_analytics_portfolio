# A/B Test - Permutation Test

## Summary

This is an example of A/B test to assess, with a permutation test, the conversion rate variation after a hypothetical change applied to an e-commerce web site.  
I've used these libraries:
* os
* pandas
* numpy
* scipy
* matplotlib
* seaborn

You can see the dataset in data folder as csv file.

## Files
```data```: csv data folder  
```AB_test_permutation```: Jupyter Notebook for the test

## Permutation Test

After loading the dataset, I've checked its info to verify its composition and, if necessary, fix data types.  
In particular, there are 6177 unique observations. They are about 3000 per group:
* GRP A is the control group
* GRP B is the treatment group

The amount of observations is not equally divided by the two groups and time taken to collect data seems like too long. A whole year could be too much time for a business. Thus, maybe the experiment could have been design better, but this is just a guess since I don't know which business the data come from.

Then, I've looked at two other statistics about each group of observations: amount of conversion and conversion rate.
Given a baseline conversion rate of 26.77% and about 3000 observations per group, the minimum detectable effect is about 3.2%.

### Hypothesis

* Null Hypothesis (H0): the difference between the treatment group conversion rate and that of the control group, if it exists, is not statistically significant

* Alternative Hypothesis (H1): the difference is statistically significant

### Test steps

* Chosen significance level (alpha): 5%

* Calculation of the Observed Test Statistic:  
$\mu_{t}-\mu_{c}$  
difference between the mean (conversion rate) of the treatment and that of the control group

* Calculation of the Average Simulated Test Statistic (permutation process):  
differences between the conversion rate of enough sample random groups

* Histogram of the distribution of the means obtained with the permutation process

* Given a significance level (alpha) of 5%, calculation of the p-value

* Since p-value is 0.026, i.e. it's less than alpha, the Null Hypothesis (H0) is rejected, while the Alternative (H1) is accepted.

### Conclusions

Since the Null Hypothesis has been rejected, it can be said that the change applied to the web page has increased the conversion rate with a statistical significance.

### Thanks for reading!