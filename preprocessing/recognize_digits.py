from typing import List
import pytesseract
import numpy as np
import cv2  # Make sure you have OpenCV installed

def recognize_digits(cells: List[np.ndarray]) -> List[int]:
    recognized_digits = []
    
    # Configuration for Tesseract:
    # --psm 10: Treat the image as a single character
    # --oem 3 : Default (Neural nets LSTM) engine
    # tessedit_char_whitelist=0123456789 : Only recognize digits 0-9
    tesseract_config = r"--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789"

    for cell in cells:
        # Convert image to grayscale if it isn't already
        if len(cell.shape) == 3 and cell.shape[2] == 3:
            gray = cv2.cvtColor(cell, cv2.COLOR_BGR2GRAY)
        else:
            gray = cell.copy()

        # Threshold the image to make the digit stand out
        # You might need to fine-tune the threshold value below
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

        # Use Tesseract to recognize the digit
        digit_str = pytesseract.image_to_string(thresh, config=tesseract_config).strip()
        
        # Convert recognized digit (string) to an integer if valid
        if digit_str.isdigit():
            recognized_digits.append(int(digit_str))
        else:
            # If Tesseract fails or returns empty/noise, handle accordingly
            recognized_digits.append(0)  # or any placeholder you prefer

    return recognized_digits
