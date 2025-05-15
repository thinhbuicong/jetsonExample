import cv2

def draw_ellipse(input_path, output_path, center, axes, angle, start_angle, end_angle, color, thickness):
    image = cv2.imread(input_path)
    if image is None:
        print("Error: Unable to open image file.")
        return
    cv2.ellipse(image, center, axes, angle, start_angle, end_angle, color, thickness)
    if cv2.imwrite(output_path, image):
        print(f"Image saved to {output_path}")
        cv2.imshow('Image Preview', cv2.imread(output_path))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to save image file.")

draw_ellipse('/home/jetson/opencv/images/yahboom_logo.png', \
             '/home/jetson/opencv/images/yahboom_logo_ellipse.png', \
             (400, 85), (375, 75), 0, 0, 360, (0, 255, 0), 2)