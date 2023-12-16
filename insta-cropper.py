import cv2
import numpy as np
import os

# Specify the directory containing the images
directory_path = "/Users/bri.wyatt/Desktop/insta-cropper/screenshots-dir/"

# List all files in the directory
for filename in os.listdir(directory_path):
    if (
        filename.endswith(".png")
        or filename.endswith(".jpg")
        or filename.endswith(".jpeg")
    ):
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)

        # Read the image
        img = cv2.imread(file_path)

        # Apply your image processing steps (as in the previous script)
        white_lower = np.array([230, 230, 230])
        white_upper = np.array([255, 255, 255])

        mask = cv2.inRange(img, white_lower, white_upper)
        mask = cv2.bitwise_not(mask)

        contours, _ = cv2.findContours(
            mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )
        if contours:
            largest_contour = max(contours, key=lambda x: cv2.contourArea(x))
            x, y, w, h = cv2.boundingRect(largest_contour)

            cropped_image = img[y : y + h, x : x + w]

            # Save the cropped image as the original file name in the same directory
            output_path = os.path.join(directory_path, filename)
            cv2.imwrite(output_path, cropped_image)

            # Delete the original image
            # os.remove(file_path)

            # Optionally, display the cropped image
            # cv2.imshow("Cropped Image", cropped_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
