# Greenland climate change
## Predicting future mass of greenland using statistical methods

This investigation uses a NASA [data source](http://climate.nasa.gov/system/internal_resources/details/original/499_GRN_ANT_mass_changes.csv) showing the mass of Greenland with time.

The work largely demonstrates the dichotomy between bias (underfitting) and variance (overfitting). Typically it is more appropriate to deal with time-series data using something like Holt-Winters but that is for another day...

Below is a sample of the data taken a few years ago. See [sampled_data.py](sampled_data.py) to reproduce.

![Sampled data](sampled_data.png)

So how to best describe the trend of this data? We could use linear regression; a line of best fit, a polynomial regression with 2 degrees of freedom

By eye it is clear that linear fit would yield poor accuracy - it doesn't match the trend's shape - but clearly overfitting will be reached if we use a polynomial which can adjust very precisely to the graph's shape. 

![Too little and too much fitting](under_overfit.png)

Produced by [under_overfit.py](under_overfit.py)

So which of these is the best curve? You can see that drawing a straight line through the data with linear regression, does not capture the downward curve of the trend. With the 40 degree curve, the tails curl biased by the last few data points which are likely to not match the general shape. The same is true of the 20&#176; model. How can we find a better way to find the closest fit to the data?

Before looking at the success (or error as is the preferred name) of each polynomial, we will first divide the data in to training and test portions. The curve we choose to represent the mass of Greenland will be made as if the date is 1 January 2011; a range from 2002 to 2010. We omit 2011 onwards to the remaining time can test how the predictions deviate from the real data collected by NASA. We now have a way. There will therefore be two types of error: 
 - error of the training data - how closely a linear, simple quadratic or a quadratic with many degrees of freedom behaves when superimposed of the 2002 - 2010 data
 - test data error - having chosen the curve that best fits the data, how does it perform when we use it in the "future" i.e. 2011 onwards.

The below graph shows the error of each polynomial from 1 (linear regression) to a 40 degree polynomial testing just with the training data. It can be seen that the error of linear fit is the worst, 2 and 3 degree models are not great but after that a plateau is reached. 4 degrees of freedom seems to be the optimal solution at present: not overfitting and keeping to as few degrees as possible.

![Polynomial errors](polynomial_errors.png)

Measuring each model's error. Calculated by [polynomial_errors.py](polynomial_errors.py)
