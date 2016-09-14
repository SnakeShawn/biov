"""
Author: Ziwei JIANG
Date: 2016/09/10
Version: 1.0
Description:
"""
import csv
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
from matplotlib.pyplot import savefig
import random


def stack(data, parameters, output):
	#data
	x=[]
	all_data=[]
	with open(data) as f:
		f_csv=csv.reader(f)
		headers=next(f_csv)
		count =len(headers)
		for a in range(count-1):
			all_data.append([])
		for row in f_csv:
			x.append(int(row[0]))
			for a in range(count-1):
				all_data[a].append(int(row[a+1]))

	#parameters
	figsize=(8,6)
	param=""
	setcolor=[]
	colors = ['#BCD8E3', '#E0A295', '#75625E', '#7F9AA5', '#AFCDD8', '#E9CDA6', '#70B879', 
	'#E8E098', '#898A82','#BDA09C', '#D76475', '#F2C2B8', '#0C5C4F', '#108484', '#F7AF02', 
	'#F29653', '#7C976A', '#FFE983','#70B879', '#AAD9A5', '#8AC2BF']
	color = random.sample(colors, count-1)
	if 'figsize' in parameters.keys():
		figsize = eval(parameters['figsize'])
	fig=plt.figure(figsize=figsize)
	if 'xlabel' in parameters.keys():
		plt.xlabel(parameters['xlabel'])
	if 'title' in parameters.keys():
		plt.title(parameters['title'])
	if 'ylabel' in parameters.keys():
		plt.ylabel(parameters['ylabel'])
	if 'color' in parameters.keys():
		setcolor=eval(parameters['color'])
		for a in range(len(setcolor)/2):
			num=setcolor[2*a]
			color[num-1]=setcolor[2*a+1]

	#draw
	exec("plt.stackplot(x,all_data,colors=color"+param+")")

	# adding horizontal grid lines
	plt.grid(True,linestyle='--',linewidth=0.5)


	savefig(output,format='svg')