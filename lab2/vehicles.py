# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



if __name__ == "__main__":
    vh = pd.read_csv('./vehicles.csv') #Read the .csh file
    
    #Create the scaterplot
    sns_plot = sns.lmplot(vh.columns[0],
                          vh.columns[1],
                          data = vh,
                          fit_reg = False)
    
    sns_plot.axes[0,0].set_ylim(0,) #Set the axes
    sns_plot.axes[0,0].set_xlim(0,)
    
    
    #Save image of the scaterplot
    sns_plot.savefig("vehiclesScaterplot.png",bbox_inches='tight')
    sns_plot.savefig("vehiclesScaterplot.pdf",bbox_inches='tight')
    
    data = vh.values.T[0] #Select the column
    
    plt.clf() #Clean the first figure to show only the second
    
    #Create the histogram
    sns_plot2 = sns.distplot(data,
                             bins=20,
                             kde=False,
                             rug=True).get_figure()
    
    axes = plt.gca() #Set the axes labels
    axes.set_xlabel('Current fleet per each') 
    axes.set_ylabel('New fleet')
    
    
    #Save image of the histogram
    sns_plot2.savefig("vehiclesHistogram.png",bbox_inches='tight')
    sns_plot2.savefig("vehiclesHistogram.pdf",bbox_inches='tight')