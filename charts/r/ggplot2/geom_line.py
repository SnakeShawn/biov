"""
Author: Xu Zhang
Date: 2016/09/22
Version: 1.0
Description:
"""
import json
import os
from config.config import rscript_cmd
from config.config import r_tmp_file


def geom_vline(data, parameters, output):
    # parameters
    ## aes's parameters
    aes_param = ''
    aes = None
    if 'aes' in parameters.keys():
        aes = parameters['aes']
    if aes is not None:
        aes_param = aes_param+",aes("
        aes_param_tmp = ''
        if 'x' in aes.keys():
            aes_param_tmp = aes_param_tmp + ',x=' + str(aes['x'])
        if 'y' in aes.keys():
            aes_param_tmp = aes_param_tmp + ',y=' + str(aes['y'])
        if aes_param_tmp.strip().startswith(','):
            aes_param_tmp = aes_param_tmp[1:]

        aes_param = aes_param+aes_param_tmp+")"

    ## geom's parameters
    geom_param = ''
    if 'xintercept' in parameters.keys():
        geom_param = geom_param + ',xintercept=' + str(parameters['xintercept'])
    if 'binwidth' in parameters.keys():
        geom_param = geom_param + ',binwidth=' + str(parameters['binwidth'])
    if 'dotsize' in parameters.keys():
        geom_param = geom_param + ',dotsize=' + str(parameters['dotsize'])
    if 'method' in parameters.keys():
        geom_param = geom_param + ',method=\'' + str(parameters['method'])+'\''
    if 'stackdir' in parameters.keys():
        geom_param = geom_param + ',stackdir=\'' + str(parameters['stackdir'])+'\''
    if 'binaxis' in parameters.keys():
        geom_param = geom_param + ',binaxis=\'' + str(parameters['binaxis'])+'\''
    if geom_param.strip().startswith(','):
        geom_param = geom_param[1:]

    try:
        os.system('touch ./charts/tmp.r')
        os.system('echo \'library("ggplot2")\' >> '+r_tmp_file)
        os.system('echo "input_data=read.csv(\''+ data +'\',header = T)" >>'+r_tmp_file)
#        os.system('echo "setEPS()" >>'+r_tmp_file)
#        os.system('echo "postscript(\''+output+'\')" >>'+r_tmp_file)
        os.system('echo "p = ggplot(input_data'+aes_param+')+ geom_point()" >> '+r_tmp_file)
        os.system('echo "image = p+geom_vline('+geom_param+')" >> '+r_tmp_file)
        os.system('echo "ggsave(file=\''+output+'\', plot=image)" >> '+r_tmp_file)
#        os.system('echo "dev.off()" >>'+r_tmp_file)
        os.system(rscript_cmd+' '+r_tmp_file)
    finally:
#        os.system('cat '+r_tmp_file)
        os.system('rm '+r_tmp_file)


def geom_hline(data, parameters, output):
    # parameters
    ## aes's parameters
    aes_param = ''
    aes = None
    if 'aes' in parameters.keys():
        aes = parameters['aes']
    if aes is not None:
        aes_param = aes_param+",aes("
        aes_param_tmp = ''
        if 'x' in aes.keys():
            aes_param_tmp = aes_param_tmp + ',x=' + str(aes['x'])
        if 'y' in aes.keys():
            aes_param_tmp = aes_param_tmp + ',y=' + str(aes['y'])
        if aes_param_tmp.strip().startswith(','):
            aes_param_tmp = aes_param_tmp[1:]

        aes_param = aes_param+aes_param_tmp+")"

    ## geom's parameters
    geom_param = ''
    if 'yintercept' in parameters.keys():
        geom_param = geom_param + ',yintercept=' + str(parameters['yintercept'])
    if 'binwidth' in parameters.keys():
        geom_param = geom_param + ',binwidth=' + str(parameters['binwidth'])
    if 'dotsize' in parameters.keys():
        geom_param = geom_param + ',dotsize=' + str(parameters['dotsize'])
    if 'method' in parameters.keys():
        geom_param = geom_param + ',method=\'' + str(parameters['method'])+'\''
    if 'stackdir' in parameters.keys():
        geom_param = geom_param + ',stackdir=\'' + str(parameters['stackdir'])+'\''
    if 'binaxis' in parameters.keys():
        geom_param = geom_param + ',binaxis=\'' + str(parameters['binaxis'])+'\''
    if geom_param.strip().startswith(','):
        geom_param = geom_param[1:]

    try:
        os.system('touch ./charts/tmp.r')
        os.system('echo \'library("ggplot2")\' >> '+r_tmp_file)
        os.system('echo "input_data=read.csv(\''+ data +'\',header = T)" >>'+r_tmp_file)
#        os.system('echo "setEPS()" >>'+r_tmp_file)
#        os.system('echo "postscript(\''+output+'\')" >>'+r_tmp_file)
        os.system('echo "p = ggplot(input_data'+aes_param+')+ geom_point()" >> '+r_tmp_file)
        os.system('echo "image = p+geom_hline('+geom_param+')" >> '+r_tmp_file)
        os.system('echo "ggsave(file=\''+output+'\', plot=image)" >> '+r_tmp_file)
#        os.system('echo "dev.off()" >>'+r_tmp_file)
        os.system(rscript_cmd+' '+r_tmp_file)
    finally:
#        os.system('cat '+r_tmp_file)
        os.system('rm '+r_tmp_file)


def geom_abline(data, parameters, output):
    # parameters
    ## aes's parameters
    aes_param = ''
    aes = None
    if 'aes' in parameters.keys():
        aes = parameters['aes']
    if aes is not None:
        aes_param = aes_param+",aes("
        aes_param_tmp = ''
        if 'x' in aes.keys():
            aes_param_tmp = aes_param_tmp + ',x=' + str(aes['x'])
        if 'y' in aes.keys():
            aes_param_tmp = aes_param_tmp + ',y=' + str(aes['y'])
        if aes_param_tmp.strip().startswith(','):
            aes_param_tmp = aes_param_tmp[1:]

        aes_param = aes_param+aes_param_tmp+")"

    ## geom's parameters
    geom_param = ''
    if 'intercept' in parameters.keys():
        geom_param = geom_param + ',intercept=' + str(parameters['intercept'])
    if 'slope' in parameters.keys():
        geom_param = geom_param + ',slope=' + str(parameters['slope'])
    if 'binwidth' in parameters.keys():
        geom_param = geom_param + ',binwidth=' + str(parameters['binwidth'])
    if 'dotsize' in parameters.keys():
        geom_param = geom_param + ',dotsize=' + str(parameters['dotsize'])
    if 'method' in parameters.keys():
        geom_param = geom_param + ',method=\'' + str(parameters['method'])+'\''
    if 'stackdir' in parameters.keys():
        geom_param = geom_param + ',stackdir=\'' + str(parameters['stackdir'])+'\''
    if 'binaxis' in parameters.keys():
        geom_param = geom_param + ',binaxis=\'' + str(parameters['binaxis'])+'\''
    if geom_param.strip().startswith(','):
        geom_param = geom_param[1:]

    try:
        os.system('touch ./charts/tmp.r')
        os.system('echo \'library("ggplot2")\' >> '+r_tmp_file)
        os.system('echo "input_data=read.csv(\''+ data +'\',header = T)" >>'+r_tmp_file)
#        os.system('echo "setEPS()" >>'+r_tmp_file)
#        os.system('echo "postscript(\''+output+'\')" >>'+r_tmp_file)
        os.system('echo "p = ggplot(input_data'+aes_param+')+ geom_point()" >> '+r_tmp_file)
        os.system('echo "image = p+geom_abline('+geom_param+')" >> '+r_tmp_file)
        os.system('echo "ggsave(file=\''+output+'\', plot=image)" >> '+r_tmp_file)
#        os.system('echo "dev.off()" >>'+r_tmp_file)
        os.system(rscript_cmd+' '+r_tmp_file)
    finally:
#        os.system('cat '+r_tmp_file)
        os.system('rm '+r_tmp_file)

