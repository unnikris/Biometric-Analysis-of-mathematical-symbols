import numpy as np
import cv2 as cv
import os
import pylab as pl
import scipy.ndimage.filters as sc
from itertools import izip
# SCRIPT.PY ACTS AS THE MAIN FILE FRO \M WHERE THE DATASETS ARE LOADED IN AND IS
#PASSED ON TO THROUGH THE PRE PROCESSING STAGES AND HENCE TO THE FEATURE EXTRACTION STAGE.
#dataset = open("Dataset/data1.txt");
temp=[];
lo = os.listdir("Dataset");
details = os.listdir("Details");
nfiles = np.size(lo);
normz=[];
def normalise(y):
    ##The normalise function nomalizes the value in range 0-1
            
    minim = np.amin(y);
    maxim = np.amax(y);
    #print minim;
    #print maxim;
    norm_dataset = (y- minim) / (maxim -minim);
    #print norm_dataset;
    
    #print norm_dataset;
    return norm_dataset;

def preprocessing(x,y,filenames):
    #plot the points
    det = "Details//"+ filenames;
    Details = np.genfromtxt(det);
    i=0;
    print filenames  
    for num in Details :
        dx=x[i:num+i]
        dy=y[i:num+i]
        i=num+i;
        dx=dx[dx>0];
        dy=dy[dy>0];
        dx=sc.gaussian_filter(dx,1);
        dy=sc.gaussian_filter(dy,1);
        pl.figure();
        print np.shape(dx);
        print np.shape(dy);
        pl.plot(dx,dy);
        ax = pl.gca();
        ax.set_ylim(ax.get_ylim()[::-1]) 
        #pl.show();
    
    #pl.scatter(x,y);
    #pl.show();
    #im=cv.GaussianBlur(img,(5,5),0);
    #cv.imshow('im',im);

for filenames in lo:
    
    params = "Dataset//"+ filenames;
    
    print params;
    
    dataset = np.genfromtxt(params);
     
    dataset_x = dataset[:,::2];
    dataset_y = dataset[:,1:np.size(dataset):2];
    temp=[];
    for eqn in range(len(dataset_x)):
        temp.append([]);
        for i in range (len(dataset_x[eqn])):
            if(dataset_x[eqn][i]>0 or dataset_y[eqn][i]>0):
                temp[eqn].append(dataset_x[eqn][i])
                temp[eqn].append(dataset_y[eqn][i])
    #print temp;
    normz=[];
    det = "Details//"+ filenames;
   # siz= "size//size_"+ filenames;
    Details = np.genfromtxt(det);
    #Size    = np.genfromtxt(siz);
    k=0;
    index=0;
    head=0;
    i=0;    
    for num in Details:
        temp_x=[];
        temp_y=[];
        for j in range(int(num)):
            #index=int(index+Size[k])
            
           #normz.append([]);
##          fp = file("size//size_"+filenames,'a');
##          np.savetxt(fp,np.shape(temp[i]),'%d')
##          fp.close();
            print "k" ,k;
            temp_x.append( temp[k][::2]);
            print "temp_x" ,temp_x
            temp_y.append( temp[k][1:np.size(dataset):2]);
            print "temp_y" , temp_y
            k=k+1;
        temp_x  = [val for sublist in temp_x for val in sublist]
        temp_y  = [val for sublist in temp_y for val in sublist] 
        print "size of temp_x",np.size(temp_x);
        print "size of temp_y", np.size(temp_y);
        print type(Details);
        print filenames  
        print type(num);
        print "num",num
        
        normdataset =np.zeros(2*np.size(temp_x));
        print "size of normdataset " , np.size(normdataset);
##        dx=temp_x[head:(int(index/2))-1]
##        dy=temp_y[head:(int(index/2))-1]
##        head = index/2;
        norm_dataset_x=normalise(temp_x);
        norm_dataset_y=normalise(temp_y);
        print norm_dataset_x
        normdataset[::2] = norm_dataset_x;
        normdataset[1::2] = norm_dataset_y;
        normz.append(normdataset);
        fp = file("size//size_"+filenames,'a');
        np.savetxt(fp,np.shape(normdataset),'%d')
        fp.close();

    #   S
    normz_array=(np.array(normz));
    
   
    
##################ONLY USE IF YOU NEED TO APPEND THE NORMALIZED FILE##########    
##    
    for i in range(len(normz_array)):
        f = file("Normalized//normalized_" + filenames,'a');
        np.savetxt( f, normz_array[i],'%f',' ','\t');
        f.close();
        space = open("Normalized//normalized_" + filenames,'a');
        space.write('\n')
        space.close();


   
    #plot the points , save as an image , pass over a smoothening function
    #preprocessing(norm_dataset_x,norm_dataset_y,filenames);
        

