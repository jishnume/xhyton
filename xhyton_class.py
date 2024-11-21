import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2 as cv
import exifread


# creating an image processing class
class xhyton:

    def __init__(self,filepath:str,image:np.ndarray):
        # validation of the input
        if not isinstance(filepath,str):
            raise TypeError(f"{filepath} is not a str variable")
        if not isinstance(image,np.ndarray):
            raise TypeError("<image> is not a numpy array")
        
        self.img = image
        self.filepath = filepath
    
    # class method to view an image in rgb format
    def imview_rgb(self):
        rgb = cv.cvtColor(self.img,cv.COLOR_BGR2RGB)
        plt.imshow(rgb)
        plt.show()
    
    # class method to view an image in BGR format (default format of OpenCV)
    def imview_bgr(self):
        plt.imshow(self.img)
        plt.show()
    
    # class method to view an image in gray scale format
    def imview_gray(self):
        gray = cv.cvtColor(self.img,cv.COLOR_BGR2GRAY)
        plt.imshow(gray,cmap='gray')
        plt.show()
    
    # class method to get metadata of an image file
    def image_meta(self,is_all_data):
        if not isinstance(is_all_data,bool):
            raise TypeError(f"{is_all_data} is not a boolean variable")
        with open(self.filepath,"rb") as file:
            tags = exifread.process_file(file)
        
        if is_all_data:  
            for tag in tags.keys():
                print(f"{tag}: {tags[tag]}")
        else:
            # printing out specific image features
            specific_tags = ["Image Make","Image Model","Image DateTime","EXIF ExposureTime","EXIF FNumber","EXIF ISOSpeedRatings"]
            for i in specific_tags:
                print(f"{i}: {tags[i]}")

    # # Open the image file in binary mode
    # with open(self.filepath, "rb") as image_file:
    #     # Read the metadata
    #     tags = exifread.process_file(image_file)
    # # Display the metadata
    
    
        
# ----------------------------------------------
#              Implementation                  -
# ----------------------------------------------
filename = "DSC_5618.jpg"
image_file = cv.imread(filename)

img = xhyton(filename,image_file)
meta_data = img.image_meta(False)