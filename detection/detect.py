import cv2
from deepface.models.face_detection.YuNet import YuNetClient

# Initialize face detector model
model = YuNetClient()

def detect_face(frame):
    """
    Detect faces in the given frame and draw rectangles around them.

    Args:
        frame (np.array): Image frame from camera.

    Returns:
        np.array: Frame with rectangles drawn on detected faces.
    """
    faces = model.detect_faces(frame)

    if faces:
        for face in faces:
            x1 = face.x
            y1 = face.y
            x2 = x1 + face.w
            y2 = y1 + face.h
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return frame
