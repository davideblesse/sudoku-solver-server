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
    solution_str = ",".join(map(str, solution))

    # Return solution in the response body
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "solution": solution_str,
        "message": "Image processed successfully"
    }

@app.get("/")
async def landing_page():
    return "The server is live!"