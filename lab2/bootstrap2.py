# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:03:31 2019

@author: jj18367
"""

import numpy as np
import random

def bootstrap(sample, sample_size, iterations):
    
    #Create empty matrix
    out = np.empty((iterations,sample_size),dtype=float)
    
    #Fill the info matrix
    for i in range(iterations):
        for j in range(sample_size):
            out.item(i,j) = random.choice(sample)
    
    #Calculate the means
    means = np.array(iterations)
    for i in range(iterations):
        means.item(i) =
        