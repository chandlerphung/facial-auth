import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from capture.camera import start_camera
from gui.gui import create_gui

def main():
    """
    Entry point of the facial authentication application.
    Launches the GUI to select a user and starts the camera for recognition.
    """
    # Open GUI to select account
    name = create_gui()
    print(f"Selected account: {name}")

    # Start camera with selected account
    start_camera(name)


if __name__ == "__main__":
    main()
