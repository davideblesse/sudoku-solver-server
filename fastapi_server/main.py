import tempfile
from fastapi import FastAPI, File, HTTPException, UploadFile
from preprocessing.recognize_digits import recognize_digits
from preprocessing.sudoku_preprocessing import process_sudoku_image
from pydantic import BaseModel
from sudoku_solver.sudoku_solver import Sudoku
from sudoku_solver.search import depth_first_graph_search
from fastapi_server.timeout import timeout

app = FastAPI()

# Pydantic model to receive a text/string field
class TextModel(BaseModel):
    message: str

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

@app.post("/solve-sudoku")
@timeout(60)
async def solve_sudoku(data: TextModel):
    puzzle_string = data.message.strip()  # Ensure no extra spaces/newlines

    # Step 1: Validate the input
    if len(puzzle_string) != 81:
        raise HTTPException(status_code=400, detail="Invalid input length. Must be exactly 81 characters.")
    
    if not puzzle_string.isdigit():
        raise HTTPException(status_code=400, detail="Invalid input. Must contain only numeric characters (0-9).")

    # Step 2: Convert the string into a tuple of tuples
    initial_state = tuple(
        tuple(int(puzzle_string[i * 9 + j]) for j in range(9)) for i in range(9)
    )

    # Step 3: Solve the Sudoku
    problem = Sudoku(initial_state)
    solution_node = depth_first_graph_search(problem)

    if not solution_node:
        raise HTTPException(status_code=400, detail="No solution found for the given puzzle.")

    # Step 4: Convert the solution to a single string
    final_state = solution_node.path()[-1].state
    solution_string = "".join(str(num) for row in final_state for num in row)

    return {"solution": solution_string}

@app.get("/")
async def landing_page():
    return "The server is live!"