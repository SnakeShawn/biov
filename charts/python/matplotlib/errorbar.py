"""
Author: Masijia QIU 
Date: 2016/08/22
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig


def errorbar(data, parameters, output):

    # data
    x = []
    y = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            x.append(float(row[0]))
            y.append(float(row[1]))

    # parameters
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        plt.title(parameters['title'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

    param = ''
    if 'xerr' in parameters.keys():
        param = param + ',xerr=' + parameters['xerr']
	if 'yerr' in parameters.keys():
	    param = param + ',yerr=' + parameters['yerr']
	if 'color' in parameters.keys():
	    param = param + ',color="' + parameters['color']+'"'
	if 'marker' in parameters.keys():
	    param = param + ',marker="' + parameters['marker']+'"'
	if 'ms' in parameters.keys():
	    param = param + ',ms=' + parameters['ms']
	if 'ls' in parameters.keys():
	    param = param + ',ls="' + parameters['ls']+'"'
	if 'lolims' in parameters.keys():
	    param = param + ',lolims="' + parameters['lolims']+'"'
	if 'uplims' in parameters.keys():
	    param = param + ',uplims="' + parameters['uplims']+'"'
	if 'xlolims' in parameters.keys():
	    param = param + ',xlolims="' + parameters['xlolims']+'"'
	if 'xuplims' in parameters.keys():
	    param = param + ',xuplims="' + parameters['xuplims']+'"'
	if 'mec' in parameters.keys():
	    param = param + ',mec="' + parameters['mec']+'"'
	if 'capsize' in parameters.keys():
	    param = param + ',capsize=' + parameters['capsize']
	if 'capthick' in parameters.keys():
	    param = param + ',capthick=' + parameters['capthick']
	if 'barsabove' in parameters.keys():
	    param = param + ',barsabove="' + parameters['barsabove']+'"'
	if 'linewidth' in parameters.keys():
	    param = param + ',linewidth=' + parameters['linewidth']

    # draw
    exec("plt.errorbar(x, y "+param+")")
    
    savefig(output, format='svg')