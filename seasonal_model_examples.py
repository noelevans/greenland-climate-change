import math
import numpy as np
import pandas as pd
from scipy import interpolate, poly1d
import matplotlib.pyplot as plt
import warnings


def rmse(targets, predictions):
    return np.sqrt(((targets - predictions) ** 2).mean())


def model(xs, ys, n=3):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', np.RankWarning)
        coefficients = np.polyfit(xs, ys, n)
        return poly1d(coefficients)


def set_subplot(axs, coords, xs, ys, degrees, label):
    spline_fn = interpolate.UnivariateSpline(xs, ys)
    axs[coords].plot(xs, spline_fn(xs), 'b-', alpha=0.3)
    axs[coords].plot(xs, model(xs, ys, degrees))
    axs[coords].set_title(label)
    axs[coords].set_yticklabels([])
    axs[coords].set_xticklabels([])


def main():
    df = pd.read_csv('greenland-mass-change.csv')
    train = df[df['year'] < 2012]
    train_xs = train['year']
    train_ys = train['mass change']
    xs = df['year']

    # Establishing trend in same manner as before, just with training years
    trend_model = model(train_xs, train_ys, 2)
    signal_no_trend = df['mass change'] - trend_model(df['year'])
    print(xs)
    print(signal_no_trend)

    fig, axs = plt.subplots(2, 2)
    set_subplot(axs, (0, 0), xs, signal_no_trend,  1, 'Linear')
    set_subplot(axs, (0, 1), xs, signal_no_trend, 10, '10 deg polynomial')
    set_subplot(axs, (1, 0), xs, signal_no_trend, 20, '20 deg polynomial')
    set_subplot(axs, (1, 1), xs, signal_no_trend, 40, '40 deg polynomial')

    plt.savefig('seasonal_model_examples.png')
    plt.show()


if __name__ == '__main__':
    main()

