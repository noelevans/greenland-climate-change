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


def main():
    df = pd.read_csv('greenland-mass-change.csv')
    train = df[df['year'] < 2012]
    test  = df[df['year'] >= 2012]
    train_xs = train['year']
    train_ys = train['mass change']
    test_xs  = test['year']
    test_ys  = test['mass change']

    trend_model = model(train_xs, train_ys, 2)
    signal_no_trend = df['mass change'] - trend_model(df['year'])

    plt.plot(df['year'], signal_no_trend)

    plt.title('Signal removing downwards trend')
    plt.xlabel('Time')
    plt.ylabel('Mass')
    plt.grid(True)
    plt.savefig('seasonal_effect.png')
    plt.show()


if __name__ == '__main__':
    main()


