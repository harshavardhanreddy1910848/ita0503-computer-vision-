import numpy as np
import cv2
import os

# Experiment 34: Create Circle Shape using OpenCV
def create_circle_image(image_size=(400, 500)):
    height, width = image_size
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    center = (width // 2, height // 2)
    radius = min(width, height) // 4
    cv2.circle(image, center, radius, (0, 0, 255), 2)
    
    cv2.imshow("Circle Image", image)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp34_output.png")
    cv2.imwrite(out_path, image)
    print(f"Exp 34 output saved to {out_path}")
    
    cv2.waitKey(500)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_circle_image((400, 500))
