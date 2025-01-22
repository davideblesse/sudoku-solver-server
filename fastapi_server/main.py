import io
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np
import cv2

app = FastAPI()

@app.post("/process-image")
async def process_image(file: UploadFile = File(...)):
    # Read the file into memory
    file_bytes = await file.read()

    solution = []
    # Generate a fake Sudoku solution with 81 numbers
    solution = list(range(1, 82))

    # Convert the solution to a string to include in headers
    solution_str = ",".join(map(str, solution))

    # Return the actual solution as a string and update the message
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "solution": solution_str,
        "message": "Image processed and fake Sudoku solution generated successfully",
    }, {"X-Sudoku-Solution": solution_str}

    # Return the number of boxes and dimensions for confirmation
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "solution": len(solution),
        "message": "Image processed and divided into 81 boxes successfully",
    }

def make_square(image):
    """
    Ensure the image is square by cropping or resizing.
    """
    height, width = image.shape[:2]
    if height != width:
        # Crop to square by taking the center
        min_side = min(height, width)
        start_x = (width - min_side) // 2
        start_y = (height - min_side) // 2
        image = image[start_y:start_y + min_side, start_x:start_x + min_side]
    return cv2.resize(image, (450, 450))  # Resize to a fixed size (e.g., 450x450)

def divide_into_grid(image, rows, cols):
    """
    Divide the image into a grid with the specified rows and columns.
    """
    height, width = image.shape[:2]
    grid = []
    box_height = height // rows
    box_width = width // cols

    for r in range(rows):
        for c in range(cols):
            x_start = c * box_width
            y_start = r * box_height
            x_end = x_start + box_width
            y_end = y_start + box_height
            grid.append(image[y_start:y_end, x_start:x_end])
    return grid


@app.get("/")
async def landing_page():
    return "The server is live!"