""" 
    Comparing linear regression with model using 
    many degrees of freedom: both have their flaws
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate, poly1d


def model(xs, ys, n=3):
    coefficients = np.polyfit(xs, ys, n)
    polynomial = poly1d(coefficients)
    return polynomial(xs)


def set_subplot(axs, coords, xs, ys, degrees, label):
    spline_fn = interpolate.UnivariateSpline(xs, ys)
    axs[coords].plot(xs, spline_fn(xs), 'b-', alpha=0.3)
    axs[coords].plot(xs, model(xs, ys, degrees))
    axs[coords].set_title(label)
    axs[coords].set_yticklabels([])
    axs[coords].set_xticklabels([])


def main():
    df = pd.read_csv('greenland-mass-change.csv')
    xs = df['year']
    ys = df['mass change']

    fig, axs = plt.subplots(2, 2)
    set_subplot(axs, (0, 0), xs, ys,  1, 'Linear')
    set_subplot(axs, (0, 1), xs, ys, 10, '10 deg polynomial')
    set_subplot(axs, (1, 0), xs, ys, 20, '20 deg polynomial')
    set_subplot(axs, (1, 1), xs, ys, 40, '40 deg polynomial')

    plt.savefig('under_overfit.png')
    plt.show()


if __name__ == '__main__':
    main()

