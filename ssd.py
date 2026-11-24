import cv2
import numpy as np
from skimage import measure
import pyvista as pv


humeral_path = "C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/humeral_jpg/"
c1_path = "C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/c1_jpg/"
slices = []

# segmentation - divide image from background + edge detection - use only edges as inputs

def preprocessing(filepath, method):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if method == 'c':
        img_blur = cv2.GaussianBlur(img, (3, 3), 0)
        edges = cv2.Canny(img, 96, 48)
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
        threshold = 40
    

        edges_map = m_scaled > threshold 

        edges =cv2.convertScaleAbs(edges_map * 255)

        # close the gaps 
        kernel = np.ones([5,5])

        edges_closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
        slice = edges_closed

    return slice

def volume(slices):

    # create 3D volume from set of images
    volume = np.stack(slices, axis=0)

    # turn into mesh, adjust first value in spacing for Z scaling 

    verts, faces, normals, values = measure.marching_cubes(volume, level=127, spacing=(1.0, 1.0, 1.0))

    # reformat mesh for renderer 
    faces_pv = np.hstack([np.full((faces.shape[0], 1), 3), faces]).astype(np.int64)
    mesh = pv.PolyData(verts, faces_pv)
    
    # render
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, color="ivory", smooth_shading=True)
    plotter.add_axes()
    plotter.show()




#preprocessing function (method, img)
    #return processed slice


# create volume function (slices list, )

# volume = np.stack(slices, axis=0)



def main():
    slices = []
    for ii in range(1, 47):
        filenum = str(ii).zfill(4)
        filepath = str(c1_path)+"c1_"+filenum+".jpg"
        slice = preprocessing(filepath, 'c')
        slices.append(slice)

    volume(slices)

if __name__ == "__main__":
    main()
# add light source 

# 3d render 