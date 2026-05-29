#Students will manipulate color channels of a static image in real-time by pressing specific keys to apply different color filters, including color tints and intensity adjustments. The image will be updated instantly with each key press.

import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image"""

    filtered_image = image.copy()
    if filter_type == "Red_tint":

        filtered_image = image.copy()
        if filter_type == "Red_tint":

            filtered_image[:, :, 1] = 0
            filtered_image[:, :, 0] = 0
        elif filter_type =="Blue_Tint":

            filtered_image[:, :, 1] = 0
            filtered_image[:, :, 2] = 0
        elif filter_type == "Green_tint":

            filtered_image[:, :, 0] = 0
            filtered_image[:, :, 2] = 0
        elif filter_type == "Increase_red":

            filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
        
        elif filter_type == "Decrease_blue":
            filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], 50)
        
        return filtered_image
    
    image_path = 'BATMAN.jpg'
    image = cv2.imread(image_path)

if image is None:
    print("Error: Image is not found!")
else:
    filter_type = "original"

    print("Press the following keybinds to activate respective filters")
    print("R - Red Tint")
    print("B - Blue Tint")
    print("G - Green Tint")
    print("I - Increase Red intensity")
    print("D - Increase Blue intensity")
    print("q - quit")

    while True:

        filtered_image = apply_color_filter(image, filter_type)

        cv2.imshow("Filtered_Image", filtered_image)


        key = cv2.waitKey & 0xFF

        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord ('d'):
            filter_type = "Increase Blue"
        elif key == ord ('q'):
            print("exiting...")
            break
        else:
            print("Invalid Key!")








        