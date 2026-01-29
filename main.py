import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from capture.camera import start_camera
from deepface import DeepFace

start_camera()