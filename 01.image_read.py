import cv2

def read_image(file_path):
    image = cv2.imread(file_path)
    if image is None:
        print("Error: Unable to open image file.")
    else:
        cv2.imshow('Image Preview', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

read_image('/home/jetson/opencv/images/yahboom_logo.png')