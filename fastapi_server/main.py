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

@app.get("/")
async def landing_page():
    return "The server is live!"