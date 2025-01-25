import tempfile
from fastapi import FastAPI, File, UploadFile
from preprocessing.recognize_digits import recognize_digits
from preprocessing.sudoku_preprocessing import process_sudoku_image
from pydantic import BaseModel
from sudoku_solver.sudoku_solver import Sudoku
from sudoku_solver.search import depth_first_graph_search

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
async def solve_sudoku(data: TextModel):
    """
    This endpoint expects data.message to be a single string of digits
    representing each row of the Sudoku puzzle back-to-back.

    For a standard 9x9 Sudoku, it should be exactly 81 digits long:
      - Digits 1-9 = Row 1
      - Digits 10-18 = Row 2
      ...
      - Digits 73-81 = Row 9

    Example of a (nonsensical) 9x9 with 81 digits:
      "530070000600195000098000060800060003400803001700020006006000280000419005000080079"
    """

    puzzle_string = data.message.strip()  # Remove extra spaces/newlines if present
    length = len(puzzle_string)

    # Validate puzzle length (36 if you expect a 4x9, 81 for a 9x9, etc.)
    # If your test uses 36, you'll either handle it or show an error.
    if length % 9 != 0:
        return {"error": f"Invalid length {length}. Length must be a multiple of 9."}

    row_count = length // 9
    # If you specifically want a 9x9 Sudoku, enforce row_count == 9:
    # if row_count != 9:
    #     return {"error": f"Invalid row count {row_count}. Expected 9 rows for a 9x9 Sudoku."}

    # Convert the string into a list of rows (each row is a list of int)
    parsed_rows = []
    for i in range(row_count):
        row_str = puzzle_string[i*9 : (i+1)*9]  # chunk of 9 digits
        row = [int(ch) for ch in row_str]
        parsed_rows.append(row)

    # Turn the list of lists into a tuple of tuples
    initial_state = tuple(tuple(r) for r in parsed_rows)

    # Solve the Sudoku
    problem = Sudoku(initial_state)
    solution_node = depth_first_graph_search(problem)
    
    if not solution_node:
        return {"error": "No solution found for the given puzzle."}

    final_state = solution_node.path()[-1].state  # tuple of tuples

    # Convert final_state back to a single string of digits
    # (row 1's digits, then row 2's digits, etc.)
    solution_str = ""
    for row in final_state:
        solution_str += "".join(str(n) for n in row)

    return {"solution": solution_str}

@app.get("/")
async def landing_page():
    return "The server is live!"