import numpy as np
import cv2
import os

# Experiment 35: Text String appeared on image using OpenCV
def add_text_to_image(image_size=(400, 500), text="OpenCV Rocks!"):
    height, width = image_size
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2
    font_thickness = 2
    text_color = (0, 0, 255)
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2
    cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)
    
    cv2.imshow("Image with Text", image)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp35_output.png")
    cv2.imwrite(out_path, image)
    print(f"Exp 35 output saved to {out_path}")
    
    cv2.waitKey(500)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    add_text_to_image((400, 500), "OpenCV Rocks!")
