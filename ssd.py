import cv2
import numpy as np


filepath = "C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/humeral_jpg/hum0064.jpg"

img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

# segmentation - divide image from background


# edge detection - use only edges as inputs

edges = cv2.Canny(img, 240, 160)



# thresholding - if above certain value, count as edge, if not, make background. use opening/closing to clean it up 

threshold = 150

edges_map = img > threshold 

edges = edges_display = cv2.convertScaleAbs(edges_map * 255)


cv2.imshow('edges', edges)
cv2.waitKey(0) 
cv2.destroyAllWindows()

#if img > thresh = 255, else if < thresh = 0 
#opening and closing 


# add light source 

# 3d render 