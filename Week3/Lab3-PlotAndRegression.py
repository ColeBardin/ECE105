import numpy as np
import matplotlib.pyplot as plt

"""
ECE 105: Programming for Engineers 2
Created September 5, 2020
Steven Weber
Zipf's Law solution

This code plots word frequencies on a log-log scale and computes regression line
"""

# reg_coef computes the coefficients of the regression line
def reg_coef(x, y):
    m = np.corrcoef(x,y)[0][1] * np.std(y) / np.std(x)
    b = np.mean(y) - m * np.mean(x)
    return m, b

# mean_error computes mean error of points (x,y) for line y = m x + b
def mean_error(x, y, m, b):
    return np.mean([(yi-(m*xi+b))**2 for xi,yi in zip(x,y)])

# coef_det computes coef. of det. (R^2) for linear regression
def coef_det(x, y, m, b):
    return 1 - mean_error(x, y, m, b) / np.var(y)

# get_data reads in a list of numerical data
def get_data(data_filename):
    with open(data_filename, 'r') as f:
        lines = [line.rstrip() for line in f]
    return [int(line.split()[1]) for line in lines]

# power_law returns the value of the power law y = b x^m
def power_law(x, m, b):
    return b * (x ** m)

# plot_data creates log-log plot of data w/ 2 regression lines
def plot_data(y, xlbl, ylbl, title, filename):
    x = range(1,len(y)+1) # x-axis is the rank
    plt.figure() # create figure (canvas)
    plt.scatter(x, y) # scatter plot of rank (x) vs. count (y)
    plt.xlim(1,len(y)+1) # set the x-axis limits
    plt.ylim(y[-1],y[0]) # set the y-axis limits
    X = list(map(np.log, x)) # take logs of the x-values
    Y = list(map(np.log, y)) # take logs of the y-values
    m1, b1 = reg_coef(X, Y) # compute regression line from X,Y
    # second regression line sets slope m = -1 and b = y[0]
    # NOTE: must cast m = -1 to a np.float64
    # Otherwise, exponentiation in power_law func. raises error
    m2, b2 = np.float64(-1), np.float64(y[0]) # 2nd reg. line
    plt.plot(x, power_law(x, m1, np.exp(b1)), '-r') # 1st red
    plt.plot(x, power_law(x, m2, b2), '-g') # 2nd line green
    plt.grid(True, which='both') # add grid
    plt.xscale('log') # set x-axis to log-scale
    plt.yscale('log') # set y-axis to log-scale
    plt.xlabel(xlbl) # add x label
    plt.ylabel(ylbl) # add y label
    rsq1 = coef_det(X,Y, m1, b1) # R^2 for 1st reg. line
    rsq2 = coef_det(X,Y, m2, np.log(b2)) # R^2 for 2nd line
    # print out the two power laws and their corresponding R^2
    print('y=b x^m, m={:.3f}, b={:.0f}, R2={:.3f}'.format(m1,np.exp(b1),rsq1))
    print('y=b x^m, m={:.3f}, b={:.0f}, R2={:.3f}'.format(m2,b2,rsq2))
    plt.title(title) # add title
    plt.savefig(filename) # save figure
    plt.show() # show figure

# main function
if __name__ == "__main__":
    # set parameters:
    data_file = 'HW3-Solution.txt' # input file
    xlbl = 'Word rank' # plot x-label
    ylbl = 'Word count' # plot y-label
    title = 'Ranked word count' # plot title
    plot_file = 'HW3-SampleOutput.pdf' # plot filename

    y = get_data(data_file) # get the data
    plot_data(y[:1000], xlbl, ylbl, title, plot_file) # plot data
    # N.B.: keep only first 1000 entries; play around with this
