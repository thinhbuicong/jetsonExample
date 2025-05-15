import cv2

def draw_circle(input_path, output_path, center, radius, color, thickness):
    image = cv2.imread(input_path)
    if image is None:
        print("Error: Unable to open image file.")
        return
    cv2.circle(image, center, radius, color, thickness)
    if cv2.imwrite(output_path, image):
        print(f"Image saved to {output_path}")
        cv2.imshow('Image Preview', cv2.imread(output_path))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to save image file.")

draw_circle('/home/jetson/opencv/images/yahboom_logo.png', \
           '/home/jetson/opencv/images/yahboom_logo_circle.png', \
           (88, 50), 30, (0, 0, 255), 2)