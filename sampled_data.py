from matplotlib import pyplot as plt
import pandas as pd
from scipy import interpolate


def main():
    df = pd.read_csv('greenland-mass-change.csv')
    all_xs = df['year']
    all_ys = df['mass change']
    spline_fn = interpolate.UnivariateSpline(all_xs, all_ys)
    plt.plot(all_xs, spline_fn(all_xs), 'b-')

    plt.title('Greenland mass change raw data')
    plt.xlabel('Time')
    plt.ylabel('Mass')
    plt.grid(True)
    plt.savefig('sampled_data.png')
 
 
if __name__ == '__main__':
    main()
