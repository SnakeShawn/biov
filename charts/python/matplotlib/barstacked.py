"""
Author: Masijia QIU 
Date: 2016/08/19
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import random

def barstacked(data, parameters, output):

    # data
    x = []
    y = []
    legend = ()
    item_num = 0
    with open(data) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        item_num = len(headers)-1
        for row in f_csv:
            x.append(row[0])
            y.append(map(int, row[1:item_num+1]))


    # parameters
    colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', '#E8E098', '#898A82',
             '#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', '#F29653', '#7C976A', '#FFE983',
             '#70B879', '#AAD9A5', '#8AC2BF']
    color = random.sample(colors, item_num)
    if 'xlabel' in parameters.keys():
        plt.xlabel(parameters['xlabel'])
    if 'title' in parameters.keys():
        plt.title(parameters['title'])
    if 'ylabel' in parameters.keys():
        plt.ylabel(parameters['ylabel'])
    
    param = ''
    if 'align' in parameters.keys():
        param = param + ',align="' + parameters['align']+'"'

    # draw
    x_pos = [ float(t)+0.2 for t in np.arange(item_num)]
    bottom = [0.]* item_num
    for i in range(len(x)):
        cbar = plt.bar(x_pos, y[i], width=0.5, bottom=bottom, color=color[i], edgecolor='')
        legend = legend + (cbar[0],)
        bottom = [a+b for a, b in zip(y[i], bottom)]

    plt.xticks(x_pos, headers[1:])

    savefig(output)