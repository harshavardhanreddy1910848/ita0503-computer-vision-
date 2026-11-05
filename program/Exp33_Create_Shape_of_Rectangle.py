import numpy as np
import cv2
import os

# Experiment 33: Create Rectangle Shape using OpenCV
def create_rectangle_image(image_size=(400, 500)):
    height, width = image_size
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    top_left = (width // 4, height // 4)
    bottom_right = (3 * width // 4, 3 * height // 4)
    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)
    
    cv2.imshow("Rectangle Image", image)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp33_output.png")
    cv2.imwrite(out_path, image)
    print(f"Exp 33 output saved to {out_path}")
    
    cv2.waitKey(500)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_rectangle_image((400, 500))
