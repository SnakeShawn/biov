"""
Author: Yu Liujun
Date: 2016/08/23
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig

def hist_unequalBins(data, parameters, output):

    # data
    x = []
    """
    mu = 200
    sigma = 25
    x = mu + sigma*np.random.randn(10000)
    """
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        #input array
        for row in f_csv:
            x.append(float(row[0]))
    
    # total of inputs
    count = len(x)

    # a mean of distribution
    mu = sum(i for i in x)/count

    # parameters
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        # besides the title, also print the mu and sigma value
        plt.title(parameters['title']+' - Unequal Bins')
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

    # defining normed, facecolor, alpha
    
    param = ''
    bins = []
    """
    if 'align' in parameters.keys():
        param = param + ',align="' + str(parameters['align'])+'"'
    """
    if 'normed' in parameters.keys():
        param = param + ', normed='+ str(parameters['normed'])+''
    if 'facecolor' in parameters.keys():
        param = param + ', facecolor="'+str(parameters['facecolor'])+'"'
    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + parameters['alpha']
    if 'rwidth' in parameters.keys():
        param = param + ',rwidth=' + parameters['rwidth']
    if 'bins' in parameters.keys():
        exec("bins ="+parameters['bins'])

    exec("fig = plt.hist(x, bins"+param+", histtype='bar')")

    savefig(output, format='svg')



def hist_stepfilled(data, parameters, output):
    # data
    x = []
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)   
        #input array
        for row in f_csv:
            x.append(float(row[0]))
  
    # total of inputs
    count = len(x)

    # a mean of distribution
    mu = sum(i for i in x)/count

    # parameters
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        # besides the title, also print the mu and sigma value
        plt.title(parameters['title']+' - Stepfilled')
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])

        # defining num_bin, normed, facecolor, alpha
    if 'num_bin' in parameters.keys():
        num_bin = int(parameters['num_bin'])
    
    param = ''
    """
    if 'align' in parameters.keys():
        param = param + ',align="' + str(parameters['align'])+'"'
    """

    if 'normed' in parameters.keys():
        param = param + ', normed='+ str(parameters['normed'])+''
    if 'facecolor' in parameters.keys():
        param = param + ', facecolor="'+str(parameters['facecolor'])+'"'
    if 'alpha' in parameters.keys():
        param = param + ',alpha=' + parameters['alpha']

    exec('fig = plt.hist(x, num_bin'+ param +', histtype="stepfilled")')

    savefig(output, format='svg')
    #end