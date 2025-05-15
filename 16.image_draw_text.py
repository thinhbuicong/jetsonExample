import cv2

def draw_text(input_path, output_path, text, position, font, font_scale, color, thickness):
    image = cv2.imread(input_path)
    if image is None:
        print("Error: Unable to open image file.")
        return
    cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
    if cv2.imwrite(output_path, image):
        print(f"Image saved to {output_path}")
        cv2.imshow('Image Preview', cv2.imread(output_path))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to save image file.")

draw_text('/home/jetson/opencv/images/yahboom_logo.png', \
          '/home/jetson/opencv/images/yahboom_logo_text.png', \
          'Hello,OpenCV!', \
           (550, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)