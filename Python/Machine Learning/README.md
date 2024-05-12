# Machine Learning

## Summary

Here, you can see some Notebooks about Machine Learning.  
In particular, I've written codes for examples about Simple Linear Regression and Multiple Linear Regression.

## Files
`data`: data folder with csv file  
`simple_linear_regression.ipynb`: Jupyter Notebook for simple linear regression  
`multiple_linear_regression.ipynb`: Jupyter Notebook for multiple linear regression   

## Notebooks Details

In `simple_linear_regression.ipynb`, I've loaded [Engel (1857) food expenditure data](https://www.statsmodels.org/devel/datasets/generated/engel.html) from statsmodels library. A dataset about income and food expenditure for 235 working class households in 1857 Belgium.  
After checking its info, I've plotted the relationship between its two variables, income and food expenditure, using a scatterplot. Since it has shown a strong and positive correlation, I've checked it out printing their correlation coefficient, that is very high. So, it has been possible to think of building a simple linear regression model with `income` as independet variable, or predictor, and `foodexp` as dependent one, or target.  
Then, after evaluating $R^2$, coefficients and their p-value, I've drawn the regression line on the scatterplot with a predicted value and its confidence interval.  
In the end, I've made another simple linear regression model, but using scikit-learn library this time.  

In `multiple_linear_regression.ipynb`, I've loaded `kc_housing_data.csv` file from data folder, but you can download this dataset from [GeoDa Data and Lab](https://geodacenter.github.io/data-and-lab/KingCounty-HouseSales2015/) or [Kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction).  
This dataset is about home sales prices and characteristics for Seattle and King County, WA (May 2014 - 2015).  
After checking its info, I've printed the correlation coefficient between `price`, target variable, and all the other variables. Then, I've built a multiple linear regression model with some predictors.  
This model has fitted data quite well, but it could have been improved by adding a new variable. So, I've done it by creating a new one taking care to avoid multicollinearity.  
After that, I've used the model to predict a price value.
Then, I've defined a multiple linear regression model in which dataset was randomly divided in training and testing data (size of 0.67 and 0.33 respectively).  
After that, I've evaluated the quality of the model by calculating some performance metrics for training and testing sets: Mean Absolute Error, Mean Absolute Percentage Error, Root Mean Squared Error, $R^2$ and Adjusted $R^2$.  
In the end, I've tried to improve further the model by adding other three predictors and I've evaluated it, again, with some performance metrics.

### Thanks for reading!