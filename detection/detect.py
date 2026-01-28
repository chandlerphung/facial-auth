from deepface.models.face_detection.YuNet import YuNetClient
import cv2

model=YuNetClient()

def detect_face(frame):

    a=model.detect_faces(frame)

    if a:

        x1=a[0].x
        y1=a[0].y
        x2=x1+a[0].w
        y2=y1+a[0].h
        
        new_frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        return new_frame

    else:
        return frame