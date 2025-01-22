import cv2
import numpy as np
import os
from typing import List

def process_sudoku_image(image_path: str) -> List[np.ndarray]:
    """
    Simple processing of a Sudoku image to cut it into 81 equal squares,
    zoom into each box to remove the frame, and preprocess it.
    
    Args:
        image_path (str): Path to the Sudoku image.

    Returns:
        List[np.ndarray]: List of 81 preprocessed grayscale cells.
    """
    # Create the output folder in tests/boxes_extraction
    output_folder = os.path.join("tests", "boxes_extraction")
    os.makedirs(output_folder, exist_ok=True)

    # Step 1: Load the image and convert to grayscale
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image at {image_path} not found.")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Get the image dimensions and calculate the size of each cell
    height, width = gray.shape
    cell_height = height // 9
    cell_width = width // 9

    # Step 3: Split the image into 81 cells
    cells = []
    for row in range(9):
        for col in range(9):
            # Extract each cell
            cell = gray[row * cell_height:(row + 1) * cell_height,
                        col * cell_width:(col + 1) * cell_width]

            # Step 3.1: Crop a margin to "zoom in" and remove the frame
            margin_h = int(cell_height * 0.1)  # 10% margin of the cell height
            margin_w = int(cell_width * 0.1)  # 10% margin of the cell width
            cell_cropped = cell[margin_h:cell_height - margin_h, margin_w:cell_width - margin_w]

            # Step 3.2: Preprocess the cell
            # Binarize the cell to improve digit contrast
            _, cell_binary = cv2.threshold(cell_cropped, 128, 255, cv2.THRESH_BINARY_INV)

            # Normalize cell size to 28x28 for uniform processing
            cell_resized = cv2.resize(cell_binary, (28, 28), interpolation=cv2.INTER_AREA)

            # Append the preprocessed cell
            cells.append(cell_resized)

            # Save each preprocessed cell as an image
            cell_filename = os.path.join(output_folder, f"box{row * 9 + col + 1}.png")
            cv2.imwrite(cell_filename, cell_resized)

    print(f"Saved {len(cells)} boxes in {output_folder}.")
    return cells
