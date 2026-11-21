
# import os
# import numpy as np
# import pydicom
# from PIL import Image

# INPUT_DIR = "C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/head"
# OUTPUT_DIR = "C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/head_jpg"

# os.makedirs(OUTPUT_DIR, exist_ok=True)

# for f in os.listdir(INPUT_DIR):
#     if not f.lower().endswith(".dcm"):
#         continue

#     try:
#         path = os.path.join(INPUT_DIR, f)
#         ds = pydicom.dcmread(path, force=True)

#         img = np.frombuffer(ds.PixelData, dtype=np.uint16)
#         img = img.reshape(ds.Rows, ds.Columns)

#         img = img.astype(np.float32)
#         img = img * float(ds.RescaleSlope) + float(ds.RescaleIntercept)

#         wc = float(ds.WindowCenter)
#         ww = float(ds.WindowWidth)

#         img = np.clip(img, wc - ww/2, wc + ww/2)
#         img = (img - (wc - ww/2)) / ww
#         img = (img * 255).astype(np.uint8)

#         out = os.path.join(
#             OUTPUT_DIR,
#             os.path.splitext(f)[0] + ".jpg"
#         )

#         Image.fromarray(img).save(out, quality=95)

#         print(f"Converted {f}")

#     except Exception as e:
#         print(f"Failed {f}: {e}")

import os
import numpy as np
import pydicom
from PIL import Image

INPUT_DIR = "C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/head"
OUTPUT_DIR = "C:/Users/kgpar/OneDrive/Documents/ee332/EE332-Final-Project/head_jpg"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for f in os.listdir(INPUT_DIR):
    if not f.lower().endswith(".dcm"):
        continue

    try:
        path = os.path.join(INPUT_DIR, f)
        ds = pydicom.dcmread(path, force=True)

        img = np.frombuffer(ds.PixelData, dtype=np.uint16)
        img = img.reshape(ds.Rows, ds.Columns)

        img = img.astype(np.float32)

        slope = float(ds.get("RescaleSlope", 1))
        intercept = float(ds.get("RescaleIntercept", 0))

        img = img * slope + intercept

        p1 = np.percentile(img, 1)
        p99 = np.percentile(img, 99)

        img = np.clip(img, p1, p99)
        img = ((img - p1) / (p99 - p1) * 255).astype(np.uint8)

        outfile = os.path.join(
            OUTPUT_DIR,
            os.path.splitext(f)[0] + ".jpg"
        )

        Image.fromarray(img).save(outfile, quality=95)

        print(f"Converted {f}")

    except Exception as e:
        print(f"Failed {f}: {e}")