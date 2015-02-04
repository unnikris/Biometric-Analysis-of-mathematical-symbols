import numpy as np
import cv2
import os
import pylab as pl
import scipy.ndimage.filters as sc
from itertools import izip
import scipy.interpolate as inte;
import interp;
SEG_DIM = 100.0;
INTERP_RES = 1
def lin_interp_stroke(data_arr):
    """
    Takes stroke array as input and returns linearly interpolated
    stroke array. 
    """
    print "data_arr",data_arr[0][0]
    KIND = 'linear'
    interp_data_arr = None
    #data_len = len(data_arr)
    print np.shape(data_arr)[1];
    for ind in range(np.shape(data_arr)[1]-1):  
        print ind;
        #print data_arr[0,ind];
        #print data_arr[ind:ind+2,:]
        x_diff = abs(data_arr[0][ind] - data_arr[0][ind+1])
        y_diff = abs(data_arr[1][ind] - data_arr[1][ind+1])
        
        if x_diff > y_diff: 
            if data_arr[0][ind] < data_arr[0][ind+1]:
                g = inte.interp1d([data_arr[0][ind],data_arr[0][ind+1]] ,[data_arr[1][ind],data_arr[1][ind+1]],kind=KIND)
            else:
                g = inte.interp1d([data_arr[0][ind+1],data_arr[0][ind]] ,[data_arr[1][ind+1],data_arr[1][ind]],kind=KIND)
                     
            #g = interp1d(data_arr[ind:ind+2,0], data_arr[ind:ind+2,1])
            
            x_new = np.arange(min(data_arr[0][ind:ind+2]),max(data_arr[0][ind:ind+2]),INTERP_RES)
            y_new = g(x_new)
        else: 
            if data_arr[1][ind] < data_arr[1][ind+1]:
                g = inte.interp1d([data_arr[1][ind],data_arr[1][ind+1]] ,[data_arr[0][ind],data_arr[0][ind+1]],kind=KIND)
            else:
                g = inte.interp1d([data_arr[1][ind+1],data_arr[1][ind]] ,[data_arr[0][ind+1],data_arr[0][ind]],kind=KIND)
                     
            #g = interp1d(data_arr[ind:ind+2,0], data_arr[ind:ind+2,1])
            
            y_new = np.arange(min(data_arr[1][ind:ind+2]),max(data_arr[1][ind:ind+2]),INTERP_RES)
            x_new = g(y_new)
            
        #new_data_arr = np.vstack((x_new,y_new))
        new_data_arr = np.vstack((x_new,y_new)).T
        
        if interp_data_arr == None: 
            interp_data_arr = new_data_arr
        else:
            interp_data_arr = np.vstack((interp_data_arr,new_data_arr))
            
    return interp_data_arr

