from PIL import Image
import numpy as np
from deepface import DeepFace
from deepface.modules.exceptions import FaceNotDetected

def verification(frame):

    # Open the image
    image1 = Image.open('./images/chandler/1.jpg')

    # Convert the image to a NumPy array
    data1 = np.asarray(image1)

    try:
        a=DeepFace.verify(
            img1_path=data1,
            img2_path=frame,
            model_name="Facenet",
            detector_backend="opencv"
            )
        print(a["verified"])

    except ValueError:
        print("Face not detected")

def find(frame):

    try:
        result = DeepFace.find(
            img_path=frame,
            db_path="./images",
            model_name="Facenet",
            distance_metric="cosine",
            enforce_detection=True,
            detector_backend="opencv",
            refresh_database=True,
            silent=True
        )

        if not result or result[0].empty:
            return

        df = result[0]
        best = df.iloc[0]

        # print(df[["identity","confidence"]])

        if best["distance"] < 0.20 and best["confidence"] > 85:
            # Extract name from path
            identity_path = best["identity"]
            name = identity_path.split("\\")[-2]  # folder name
            return name

        return None
    
    except FaceNotDetected:
        print("Face not detected")

    


