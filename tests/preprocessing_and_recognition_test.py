import os
from preprocessing.recognize_digits import recognize_digits
from preprocessing.sudoku_preprocessing import process_sudoku_image
import numpy as np

def main():
    # Path to the test image
    test_image_path = os.path.join(
        os.path.dirname(__file__),
        "test_images",
        "sudoku_test_image_0.png"
    )

    # Step 1: Preprocess the image to extract cells
    print("Processing image...")
    processed_cells = process_sudoku_image(test_image_path)

    if len(processed_cells) != 81:
        print(f"Error: Preprocessing returned {len(processed_cells)} cells instead of 81.")
        return

    print("Preprocessing completed successfully.")

    # Step 2: Recognize digits from the cells
    print("Recognizing digits...")
    recognized_digits = recognize_digits(processed_cells)

    if len(recognized_digits) != 81:
        print(f"Error: Recognition returned {len(recognized_digits)} digits instead of 81.")
        return

    print("Recognition completed successfully.")

    # Step 3: Print recognized digits
    print("Recognized Sudoku digits:")
    print(np.array(recognized_digits).reshape(9, 9))

if __name__ == "__main__":
    main()
