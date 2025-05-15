import cv2

def crop_image(input_path, output_path, start_row, start_col, end_row, end_col):
    image = cv2.imread(input_path)
    if image is None:
        print("Error: Unable to open image file.")
        return
    cropped_image = image[start_row:end_row, start_col:end_col]
    if cv2.imwrite(output_path, cropped_image):
        print(f"Image saved to {output_path}")
        cv2.imshow('Image Preview', cv2.imread(output_path))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to save image file.")

crop_image('/home/jetson/opencv/images/yahboom_logo.png', \
           '/home/jetson/opencv/images/yahboom_logo_crop.png', \
            50, 50, 200, 500)