import numpy as np
import cv2
import os
import pylab as pl
import scipy.ndimage.filters as sc
from itertools import izip
import scipy.interpolate as inte;
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, color, exposure

parent = os.walk("Image_dataset")

for root,dirs,files in  os.walk(os.getcwd()):
    if(root == os.getcwd() + "/Image_dataset"):
        for each_dir in dirs:
            current_dir= os.listdir(root+"/"+each_dir)
            for img in current_dir:
                print img
                im = cv2.imread(root+"/"+each_dir+"/"+img)
                gray_im =cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                newarr,hog_image = hog(gray_im,8,(8,8),(10,10),True);
                #print newarr;
                cv2.imwrite("hog.png",hog_image);
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

                ax1.axis('off')
                ax1.imshow(im, cmap=plt.cm.gray)
                ax1.set_title('Input image')

                # Rescale histogram for better display
                hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))

                ax2.axis('off')
                ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
                ax2.set_title('Histogram of Oriented Gradients')
               # plt.show()
                img_1 = img.split('.');
                direc = each_dir.split('.');
                ss = newarr[newarr>0]
                print np.size(ss)
                #ssss
                fp = file("hog//"+direc[0]+"_"+img_1[0]+".txt",'a')
                np.savetxt(fp,newarr,'%5.4e')
                fp.close();
                
