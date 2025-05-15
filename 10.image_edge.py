import cv2

def edge_detection(input_path, output_path, threshold1, threshold2):
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Unable to open image file.")
        return
    edges = cv2.Canny(image, threshold1, threshold2)
    if cv2.imwrite(output_path, edges):
        print(f"Image saved to {output_path}")
        cv2.imshow('Image Preview', cv2.imread(output_path))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to save image file.")

edge_detection('/home/jetson/opencv/images/yahboom_logo.png', \
               '/home/jetson/opencv/images/yahboom_logo_edge.png', \
               100, 200)