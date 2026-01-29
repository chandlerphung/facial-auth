from PIL import Image
import numpy as np
from deepface import DeepFace

def verification(frame):

    # Open the image
    image1 = Image.open('./images/selfie1.jpg')

    # Convert the image to a NumPy array
    data1 = np.asarray(image1)

    try:

        a=DeepFace.verify(img1_path=data1,img2_path=frame,model_name="SFace",detector_backend="opencv")
        print(a["verified"])

    except ValueError:

        print("Face not detected")
