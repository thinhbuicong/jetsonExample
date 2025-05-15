import cv2
from jetcam.csi_camera import CSICamera

def preview_usb_camera():
    cap = CSICamera(capture_device=0, width=640, height=480)
    while True:
        frame = cap.read()
        if frame is not None:
            cv2.imshow('CSI Camera Preview', cv2.resize(frame, (640, 480)))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error: Could not open CSI camera.")
            break

    cap.release()
    cv2.destroyAllWindows()

preview_usb_camera()