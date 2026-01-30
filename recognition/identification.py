from PIL import Image
import numpy as np
from deepface import DeepFace

def verification(frame):

    # Open the image
    image1 = Image.open('./images/chandler/selfie1.jpg')

    # Convert the image to a NumPy array
    data1 = np.asarray(image1)

    try:

        a=DeepFace.verify(
            img1_path=data1,
            img2_path=frame,
            model_name="SFace",
            detector_backend="opencv"
            )
        
        print(a["verified"])

    except ValueError:

        print("Face not detected")

def find(frame):
    result = DeepFace.find(
        img_path=frame,
        db_path="./images",
        model_name="Facenet",
        distance_metric="cosine",
        enforce_detection=False,
        detector_backend="opencv",
    )

    if not result or result[0].empty:
        return

    df = result[0]
    best = df.iloc[0]

    # if best["distance"] < best["threshold"]:
    #     print("MATCH")
    #     print(best["identity"], best["confidence"])


