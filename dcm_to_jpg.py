import dicom2jpg



# Convert all DICOM files in a directory (uses multiprocessing by default)
dicom2jpg.dicom2jpg("path/to/dicom_folder", target_root="path/to/output_folder")