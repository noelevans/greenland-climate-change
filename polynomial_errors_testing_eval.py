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

    models = [model(train_xs, train_ys, n) for n in range(1, 41)]
    train_diffs = [rmse(train_ys, m(x)) for x, m in zip(train_xs, models)]
    plt.plot(range(1, 41), train_diffs, label='Training error')

    # Collect the models built above then evaluate with test years' data
    test_diffs = [rmse(test_ys, m(test_xs)) for m in models]
    plt.plot(range(1, 41), test_diffs, label='Test error')

    print('Coefficients for 2 degree model:')
    print(models[1].coefficients)

    plt.title('Comparing training to test error')
    plt.xlabel('Degrees')
    plt.ylabel('Error')
    plt.grid(True)
    plt.legend()
    plt.gca().set_xlim(0)
    plt.savefig('polynomial_errors_testing_eval.png')
    plt.show()


if __name__ == '__main__':
    main()

