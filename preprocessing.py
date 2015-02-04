import numpy as np
import cv2
import os
import pylab as pl
import scipy.ndimage.filters as sc
from itertools import izip
import scipy.interpolate as inte;
import interp;
SEG_DIM = 100.0;


def preprocessing(x,y,filenames):
    #plot the points
    k=0
    directory = filenames;
    det = "Details//"+ filenames;
    siz= "size//size_"+ filenames;
    Details = np.genfromtxt(det);
    Size    = np.genfromtxt(siz);
    print type(Details);
    i=0;
    index=0;
    head=0;
    print filenames  
    for num in Size :
        k=k+1;
        print type(num);
        print "num",num
        dx=x[head:(head+(num/2))]
        dy=y[head:(head+(num/2))]
        head = head+(num/2);
        dx=sc.gaussian_filter(dx,1);
        dy=sc.gaussian_filter(dy,1);
        pl.figure();
        print (dx);
        print (dy);
        pl.plot(dx,dy);
        ax = pl.gca();
        ax.set_ylim(ax.get_ylim()[::-1]) 
        #pl.show();
        bin_mat=xy_to_cv(dx,dy);
           
    #print np.shape(bin_mat);
##        for i in bin_mat:
##            print i;
        cv2.imwrite('one.png',bin_mat);
    #print "end"
#        sssssss;
        vis_2 = cv2.cvtColor(bin_mat,cv2.COLOR_GRAY2BGR)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        cv2.imwrite(directory+"//"+str(k)+".png",vis_2)

        #cv2.namedWindow("main", cv2.CV_WINDOW_NORMAL)
        #cv2.imshow("main",img);
        
    #pl.scatter(x,y);
    #pl.show();
    #im=cv.GaussianBlur(img,(5,5),0);
    #cv2.imshow('im',im);

## convert the mat -data into an image
def xy_to_cv(x,y):
    #"""
   # Converts xy pairs to a openCV formatted matrix.
    #"""
    max_x = max(x)
    max_y = max(y)
    max_xy = max([max_x,max_y])
    #print max_xy;
    dim_stretch = SEG_DIM / max_xy
    data_arr = [ x,y];
    #print "original data"
    #print data_arr
    #print dim_stretch
    #print np.shape(data_arr);
    #####################to revert olug in data_arr instead of inter_pol##
    inter_pol = interp.lin_interp_stroke(data_arr);
##    print np.shape(inter_pol);
##    print type(inter_pol);
    inter_pol =[i*dim_stretch for i in inter_pol];
    #print "shape of interpolated_Set", np.shape(inter_pol);
    
    inter_pol=np.asarray(inter_pol);
    inter_pol= inter_pol.flatten();
    print "INterpolated set :  "  , inter_pol
    data_arr_st =[i*dim_stretch for i in data_arr];
##    print "inter_pol",data_arr
##    print np.shape(data_arr);

    #print "updated data"
    #print data_arr;
    
    
    vis = 255 * np.ones((SEG_DIM+1, SEG_DIM+1),np.uint8)
    #print np.shape(vis);
    # place all values in binary image
    #ctr=0;
    #print inter_pol;
    
#    print np.shape(inter_pol);
    inter_pol_x = inter_pol[::2];
    inter_pol_y =inter_pol[1::2];
    inter_pol = [inter_pol_x,inter_pol_y];
    print np.shape(inter_pol);
    for i in range(np.shape(inter_pol)[1]):
        
        vis[round(inter_pol[1][i]),round(inter_pol[0][i])] = 0
        
    return vis


