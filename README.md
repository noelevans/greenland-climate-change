# Greenland climate change
## Predicting future mass of greenland using statistical methods

This investigation uses a NASA [data source](http://climate.nasa.gov/system/internal_resources/details/original/499_GRN_ANT_mass_changes.csv) showing the mass of Greenland with time.

The work largely demonstrates the dichotomy between bias (underfitting) and variance (overfitting). Typically it is more appropriate to deal with time-series data using something like Holt-Winters but that is for another day...

Below is a sample of the data taken a few years ago. See [sampled_data.py](sampled_data.py) to reproduce.

![Sampled data](sampled_data.png)

So how to best describe the trend of this data? We could use linear regression; a line of best fit, a polynomial regression with 2 degrees of freedom

By eye it is clear that linear fit would yield poor accuracy - it doesn't match the trend's shape - but clearly overfitting will be reached if we use a polynomial which can adjust very precisely to the graph's shape. 

![Too little and too much fitting](under_overfit.png)
