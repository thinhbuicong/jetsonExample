import cv2

def flip_image(input_path, output_path, flip_code):
    image = cv2.imread(input_path)
    if image is None:
        print("Error: Unable to open image file.")
        return
    flipped_image = cv2.flip(image, flip_code)
    if cv2.imwrite(output_path, flipped_image):
        print(f"Image saved to {output_path}")
        cv2.imshow('Image Preview', cv2.imread(output_path))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to save image file.")

flip_image('/home/jetson/opencv/images/yahboom_logo.png', \
           '/home/jetson/opencv/images/yahboom_logo_flip.png', \
            1)