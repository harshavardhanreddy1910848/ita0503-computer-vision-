import numpy as np
import cv2
import os

# Experiment 32: Create 4 colored boxes in corners (Black, Blue, Green, Red)
def create_colored_corners(image_size=(400, 500)):
    height, width = image_size
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    box_h, box_w = height // 10, width // 10
    
    # Define corner regions and their colors (BGR format)
    image[:box_h, :box_w] = [0, 0, 0]        # Top-left (Black)
    image[:box_h, -box_w:] = [255, 0, 0]      # Top-right (Blue)
    image[-box_h:, :box_w] = [0, 255, 0]      # Bottom-left (Green)
    image[-box_h:, -box_w:] = [0, 0, 255]      # Bottom-right (Red)
    
    cv2.imshow("Colored Corners Image", image)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp32_output.png")
    cv2.imwrite(out_path, image)
    print(f"Exp 32 output saved to {out_path}")
    
    cv2.waitKey(500)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_colored_corners((400, 500))
