import numpy as np
import cv2 as cv
from detection.detect import detect_face
from recognition.identification import verification, find
import time

def start_camera(name):

    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    frame_index = 0
    frame_count = 0
    start_time = time.perf_counter()
    VERIFY_EVERY_N_FRAMES = 5
    current_identity = "Unknown"
    last_seen_time = time.time()

    AUTH_DURATION = 3.0  # seconds
    identity_start_time = None
    authenticated = False


    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        frame_index += 1
        start_time = time.time()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        frame=detect_face(frame)

        if frame_index % VERIFY_EVERY_N_FRAMES == 0:
            name = find(frame)

        if name:
            # Identity changed → reset timer
            if name != current_identity:
                current_identity = name
                identity_start_time = time.time()
            last_seen_time = time.time()

        # If identity has been stable long enough → authenticate
        if current_identity != "Unknown" and identity_start_time:
            if time.time() - identity_start_time >= AUTH_DURATION:
                authenticated = True

        if time.time() - last_seen_time > 2:
            current_identity = "Unknown"

        if current_identity:
            cv.putText(
            frame,
            current_identity,
            (30, 40),  # position
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv.LINE_AA
            )

        # print("FPS: ", 1.0 / (time.time() - start_time))

        # Our operations on the frame come here
        # Display the resulting frame

        if authenticated:
            print(f"{current_identity} authenticated")
            break


        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()