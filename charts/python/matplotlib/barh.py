"""
Author: Xu Zhang
Date: 2016/08/16
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig


def barh(data, parameters, output):
    # data
    x = []
    y = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            y.append(row[0])
            x.append(int(row[1]))

    # parameters
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        plt.title(parameters['title'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

    param = ''
    if 'align' in parameters.keys():
        param = param + ',align="' + parameters['align']+'"'
    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + parameters['alpha']

    # draw
    y_pos = np.arange(len(y))
    exec("plt.barh(y_pos, x "+param+")")

    plt.yticks(y_pos, y)

    savefig(output)


