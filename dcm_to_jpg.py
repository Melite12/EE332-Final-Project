# NOT WORKING: 

# import dicom2jpg



# # Convert all DICOM files in a directory (uses multiprocessing by default)
# dicom2jpg.dicom2jpg("C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/humeral1", target_root="C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/humeral1jpg", anonymous=True, force=True)


import pydicom
import numpy as np
from PIL import Image
import os

input_folder = "dicom_files"
output_folder = "jpg_files"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".dcm"):
        dcm_path = os.path.join(input_folder, filename)

        ds = pydicom.dcmread(dcm_path)
        pixel_array = ds.pixel_array.astype(float)

        # Normalize to 0-255
        pixel_array = (np.maximum(pixel_array, 0) /
                       pixel_array.max()) * 255.0
        image = Image.fromarray(pixel_array.astype(np.uint8))

        jpg_name = os.path.splitext(filename)[0] + ".jpg"
        image.save(os.path.join(output_folder, jpg_name))

print("Conversion complete.")