import cv2

def resize_image(input_path, output_path, size):
    image = cv2.imread(input_path)
    if image is None:
        print("Error: Unable to open image file.")
        return
    resized_image = cv2.resize(image, size)
    if cv2.imwrite(output_path, resized_image):
        print(f"Image saved to {output_path}")
        cv2.imshow('Image Preview', cv2.imread(output_path))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to save image file.")

resize_image('/home/jetson/opencv/images/yahboom_logo.png', \
            '/home/jetson/opencv/images/yahboom_logo_resize.png',\
            (500, 100))