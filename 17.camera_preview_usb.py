import cv2

def preview_usb_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open USB camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('USB Camera Preview', cv2.resize(frame, (640, 480)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

preview_usb_camera()