# Machine Learning

## Summary

Here, you can see some Notebooks about Machine Learning.  
In particular, I've written codes for examples about Simple Linear Regression, Multiple Linear Regression and Logistic Regression.  

I've used these libraries:

* pandas
* numpy
* matplotlib
* seaborn
* statsmodels
* scikit-learn

## Files
`data`: data folder with csv file  
`simple_linear_regression.ipynb`: Jupyter Notebook for simple linear regression  
`multiple_linear_regression.ipynb`: Jupyter Notebook for multiple linear regression  
`logistic_regression.ipynb`: Jupyter Notebook for logistic regression  

## Notebooks Details

In `simple_linear_regression.ipynb`, I've loaded [Engel (1857) food expenditure data](https://www.statsmodels.org/devel/datasets/generated/engel.html) from statsmodels library. A dataset about income and food expenditure for 235 working class households in 1857 Belgium.  
After checking its info, I've plotted the relationship between its two variables, income and food expenditure, using a scatterplot. Since it has shown a strong and positive correlation, I've checked it out printing their correlation coefficient, that is very high. So, it has been possible to think of building a simple linear regression model with `income` as independet variable, or predictor, and `foodexp` as dependent one, or target.  
Then, after evaluating $R^2$, coefficients and their p-value, I've drawn the regression line on the scatterplot highlighting a specific predicted value and its 95% confidence interval.  
In the end, I've made another simple linear regression model, but using scikit-learn library this time.  

In `multiple_linear_regression.ipynb`, I've loaded `kc_housing_data.csv` file from data folder, but you can download this dataset from [GeoDa Data and Lab](https://geodacenter.github.io/data-and-lab/KingCounty-HouseSales2015/) or [Kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction).  
This dataset is about home sales prices and characteristics for Seattle and King County, WA (May 2014 - 2015).  
After checking its info, I've printed the correlation coefficient between `price`, target variable, and all the other variables. Then, I've built a multiple linear regression model with some predictors.  
This model has fitted data quite well, but it could have been improved by adding a new variable. So, I've done it by creating a new one taking care to avoid multicollinearity.  
After that, I've used the model to predict a price value.
Then, I've defined a multiple linear regression model in which dataset was randomly divided in training and testing data (size of 0.67 and 0.33 respectively).  
After that, I've evaluated the quality of the model by calculating some performance metrics for training and testing sets: Mean Absolute Error, Mean Absolute Percentage Error, Root Mean Squared Error, $R^2$ and Adjusted $R^2$.  
In the end, I've tried to improve further the model by adding other three predictors and I've evaluated it, again, with some performance metrics.

In `logistic_regression.ipynb`, I've loaded `titanic` dataset from seaborn library. A dataset about the sinking of the Titanic. It has some variables about a group of passengers features and, for each of them, a "surviving" label: 1 if survived, 0 otherwise. This last variable is the target for a classification model.  
After checking its info and a first assessment of the useful features as predictors, I've converted 'sex' in a binary variable. Then, I've filled in 'age' missing values. I've imputed them randomly based on the distribution of the actual values (in particular, mean and standard deviation). After that, I've filled in 'deck' missing values. Specifically, I've given 'deck A' to all the passengers from the 'first class' because that deck was really reserved for those people. For the other decks, I've assigned them randomly but with specified probabilities based on the existing values. Then, I've converted this feature in a dummy variable and I've dropped useless dataset columns.  
With a heatmap, I've shown the correlation coefficients between all the variables pairs to verify my choice.  
Finally, I've built a logistic regression model with only some of the choosen variables to avoid multicollinearity (i.e. not all the decks). The model has been built with scikit-learn and, with the same library, I've evaluated its performance in both training and test sets. I've also printed a confusion matrix for each of the splitted sets (train and test set).  
Then, I've plotted the Receiver Operating Characteristic (ROC) curve with the Area Under Curve (AUC) value to visually check the performance in another way.  
In the end, I've calculated the mean accuracy of the model with another function with k-fold cross validation. So, I could compare this last value to the first test accuracy.  
Finally, since training and test accuracy look alike (about 79%), just like the mean accuracy of last method, the model has not overfitted training data and is quite good.  


### Thanks for reading!