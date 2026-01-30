import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from capture.camera import start_camera
from deepface import DeepFace
from gui.gui import create_gui

name=create_gui()
print(name)
start_camera(name)