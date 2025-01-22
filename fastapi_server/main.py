import tempfile
from fastapi import FastAPI, File, UploadFile
from preprocessing.recognize_digits import recognize_digits
from preprocessing.sudoku_preprocessing import process_sudoku_image

app = FastAPI()

@app.post("/process-image")
async def process_image(file: UploadFile = File(...)):
    # Read the file into memory
    file_bytes = await file.read()

    # Write the file bytes to a temporary file
    with tempfile.NamedTemporaryFile(delete=True, suffix=".jpg") as temp_file:
        temp_file.write(file_bytes)
        temp_file.flush()  # Ensure all data is written to disk

        # Pass the temporary file path to the preprocessing function
        processed_cells = process_sudoku_image(temp_file.name)

    # Recognize digits from the processed cells
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
