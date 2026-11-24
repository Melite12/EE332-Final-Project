import cv2
import numpy as np


filepath = "C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/humeral_jpg/hum0064.jpg"

img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

# segmentation - divide image from background


# edge detection - use only edges as inputs

edges = cv2.Canny(img, 240, 160)

def preprocessing(filepath, method):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if method == 'c':

        edges = cv2.Canny(img, 240, 160)
        slice = edges

    elif method  == 's':
        # apply blurring filter 
        img_blur = cv2.GaussianBlur(img, (11, 11), 0)

        # sobel edge detection

        sobel_edgesx = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0, 5)
        sobel_edgesy = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1, 5)

        magnitude = cv2.magnitude(sobel_edgesx, sobel_edgesy)
        m_scaled = cv2.convertScaleAbs(magnitude)

        # thresholding
        threshold = 100

        edges_map = img_blur > threshold 

        edges =cv2.convertScaleAbs(edges_map * 255)

        # close the gaps 
        kernel = np.ones([5,5])

        edges_closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
        slice = edges_closed

    return slice

# thresholding - if above certain value, count as edge, if not, make background. use opening/closing to clean it up 

# try blurring image first 
img_blur = cv2.GaussianBlur(img, (5, 5), 0)

# try using sobel edge detection first

sobel_edgesx = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0, 5)
sobel_edgesy = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1, 5)

magnitude = cv2.magnitude(sobel_edgesx, sobel_edgesy)
m_scaled = cv2.convertScaleAbs(magnitude)


# try roberts cross 
roberts_window_x = np.array([[1,0], [0,-1]])
roberts_window_y = np.array([[0,1], [-1,0]])
gradx = cv2.filter2D(img_blur, cv2.CV_32F, roberts_window_x)
grady = cv2.filter2D(img_blur, cv2.CV_32F, roberts_window_y)

gradx = gradx.astype(np.float32)
grady = grady.astype(np.float32)

mag = cv2.magnitude(gradx, grady)
mag_norm = cv2.convertScaleAbs(mag)


cv2.imshow('roberts', mag_norm)
cv2.waitKey(0) 
cv2.destroyAllWindows()

#try other edge finding algorithms = sobel, roberts cross etc

threshold = 75

edges_map = img_blur > threshold 

edges =cv2.convertScaleAbs(edges_map * 255)

# close the gaps 
kernel = np.ones([5,5])
edges_closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

cv2.imshow('edges', edges)
cv2.waitKey(0) 
cv2.destroyAllWindows()

#if img > thresh = 255, else if < thresh = 0 
#opening and closing 


#preprocessing function (method, img)
    #return processed slice


# create volume function (slices list, )

# volume = np.stack(slices, axis=0)
#turn into mesh 
# reformat 
# render



# add light source 

# 3d render 