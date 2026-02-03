from PIL import Image
import numpy as np
from deepface import DeepFace
from deepface.modules.exceptions import FaceNotDetected

def verification(frame):
    """
    Verify if the face in the given frame matches the reference image.

    Args:
        frame (str or np.array): The frame or path to verify.

    Returns:
        None
    """
    try:
        # Load reference image
        reference_image = Image.open("./images/chandler/1.jpg")
        reference_data = np.asarray(reference_image)

        # Verify using DeepFace
        result = DeepFace.verify(
            img1_path=reference_data,
            img2_path=frame,
            model_name="Facenet",
            detector_backend="opencv"
        )
        print(f"Verified: {result['verified']}")

    except ValueError:
        print("Face not detected")


def find(frame):
    """
    Search the database for a match to the face in the given frame.

    Args:
        frame (str or np.array): The frame or image path to search.

    Returns:
        str or None: Name of the matched person or None if no match.
    """
    from deepface.modules.exceptions import FaceNotDetected

    try:
        results = DeepFace.find(
            img_path=frame,
            db_path="./images",
            model_name="Facenet",
            distance_metric="cosine",
            enforce_detection=True,
            detector_backend="opencv",
            refresh_database=True,
            silent=True
        )

        if not results or results[0].empty:
            return None

        df = results[0]
        best_match = df.iloc[0]

        if best_match["distance"] < 0.20 and best_match["confidence"] > 85:
            # Extract name from folder path
            identity_path = best_match["identity"]
            name = identity_path.split("\\")[-2]  # folder name
            return name

        return None

    except FaceNotDetected:
        print("Face not detected")
        return None
