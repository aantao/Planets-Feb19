# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:58:31 2018

@author: aantao
"""

import numpy
import matplotlib.pyplot as plt

def plot_random_walk(n):
    if not isinstance(n,int):
        raise ValueError("Number of steps must be an integer")
    else:
        walk_array=numpy.zeros(n)
        for i in range(1,len(walk_array)):
            walk_array[i] = walk_array[i-1] + numpy.random.choice([-1,1])
        plt.plot(walk_array)