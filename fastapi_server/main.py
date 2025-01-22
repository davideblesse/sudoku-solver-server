import io
from fastapi import FastAPI, File, UploadFile
from preprocessing.recognize_digits import recognize_digits
from preprocessing.sudoku_preprocessing import process_sudoku_image

app = FastAPI()

@app.post("/process-image")
async def process_image(file: UploadFile = File(...)):
    # Read the file into memory
    file_bytes = await file.read()
    
    # Generate a fake Sudoku solution with 81 numbers
    processed_cells = process_sudoku_image(file_bytes)
    recognized_digits = recognize_digits(processed_cells)
    solution_str = ",".join(map(str, recognized_digits))

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