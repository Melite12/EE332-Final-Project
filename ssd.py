import cv2
import numpy as np
import pyvista as pv


filepath = "C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/humeral_jpg/hum0064.jpg"

slices = []

# segmentation - divide image from background + edge detection - use only edges as inputs

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

def volume(slices):

    # create 3D volume from set of images
    volume = np.stack(slices, axis=0)

    # turn into mesh 

    verts, faces, normals, values = measure.marching_cubes(
    volume, 
    level=127, 
    spacing=(1.0, 1.0, 1.0)  # Change first value (Z) if slices are spaced further apart
)

    # 4. Format faces for PyVista (PyVista expects a leading '3' before each triangle's vertex indices)
    faces_pv = np.hstack([np.full((faces.shape[0], 1), 3), faces]).astype(np.int64)
    mesh = pv.PolyData(verts, faces_pv)
    # reformat 
    # render


#preprocessing function (method, img)
    #return processed slice


# create volume function (slices list, )

# volume = np.stack(slices, axis=0)




# add light source 

# 3d render 