import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from capture.camera import start_camera
from deepface import DeepFace

from PIL import Image
import numpy as np

# Open the image
image1 = Image.open('./images/selfie1.jpg')
image2 = Image.open('./images/selfie2.jpg')

# Convert the image to a NumPy array
data1 = np.asarray(image1)
data2 = np.asarray(image2)

a=DeepFace.verify(img1_path=data1,img2_path=data2,model_name="VGG-Face")

print(a["verified"])