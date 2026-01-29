from deepface.models.face_detection.YuNet import YuNetClient
import cv2

model=YuNetClient()

def detect_face(frame):

    a=model.detect_faces(frame)

    if a:

        for faces in a:

            x1=faces.x
            y1=faces.y
            x2=x1+faces.w
            y2=y1+faces.h
            
            new_frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        
        return new_frame

    else:
        return frame