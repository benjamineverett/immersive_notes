'''
This file contains functions to generate line graphs, histograms, scatterplots (with line of best fit), boxplots, and bar graphs using matplotlib.pyplot.
'''

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams.update({
    'font.size'           : 16.0,
    'axes.titlesize'      : 'large',
    'axes.labelsize'      : 'medium',
    'xtick.labelsize'     : 'small',
    'ytick.labelsize'     : 'small',
    'legend.fontsize'     : 'small',
})

fig = plt.figure()

def plot_function(x, y, axis=111, xlabel='', ylabel='', title='', color=None, label=None):
    '''
    INPUT:
    x = array/list of numerical values to input in function
    y = PDF, PMF, or similar function
    OUTPUT:
    Matplotlib plot of the function
    '''
    ax = fig.add_subplot(axis)
    ax.set_xlim(0, max(x))
    ax.set_ylim(0, max(y))
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    # ax.legend(loc='best')
    ax.plot(x, y, color=color, lw=2)

def plot_histogram(x, axis=111, xlabel='', ylabel='Frequencies', title='', color=None, label=None):
    '''
    INPUT:
    x = array/list of numerical values
    OUTPUT:
    Matplotlib histogram
    '''
    ax = fig.add_subplot(axis)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    # ax.legend(loc='best')
    ax.hist(x, color=color, rwidth=0.95)

def plot_scatterplot(x, y, axis=111, xlabel='', ylabel='', title='', color=None, label=None):
    '''
    INPUT:
    x = array/list of numerical values
    y = array/list of numerical values
    OUTPUT:
    Matplotlib scatterplot with line of best fit
    '''
    ax = fig.add_subplot(axis)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    # ax.legend(loc='best')
    ax.scatter(x, y, color=color)
    slope, intercept = np.polyfit(x, y, 1)
    ax.plot(x, x * slope + intercept, color=color, lw=2)

def plot_boxplot(x, axis=111, xlabel='', ylabel='Observed values', title='', label=None):
    '''
    INPUT:
    x = array/list of numerical values
    OUTPUT:
    Matplotlib boxplot with median labeled
    '''
    ax = fig.add_subplot(axis)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    # ax.legend(loc='best')
    bplot = ax.boxplot(x, medianprops={'color': 'k'}, patch_artist=True)
    # Fills boxes with gray
    [patch.set_facecolor('gray') for patch in bplot['boxes']]
    for line in bplot['medians']:
        (x,y) = line.get_xydata()[1]
        ax.annotate(y, (x,y))

def plot_bar_graph(y, categories, num_groups=0, axis=111, xlabel='', ylabel='', title='', color=None, label=None):
    '''
    INPUT:
    y = array/list of numerical values
    categories = array/list of corresponding category names
    OUTPUT:
    Matplotlib bar graph
    '''
    ax = fig.add_subplot(axis)
    num_groups = range(len(y))
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    # Set labels for each category on the x axis
    ax.set_xticklabels(categories)
    # ax.legend(loc='best')
    ax.bar(num_groups, y, width=0.85, color=color)

def plot_line_graph():
    '''
    INPUT:

    OUTPUT:
    Matplotlib line graph
    '''
    pass

plt.show()
# plt.savefig('_.png', dpi=300)
