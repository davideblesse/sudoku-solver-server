import requests

def test_solve_sudoku():
    # Define the FastAPI endpoint URL
    url = "https://sudoku-solver-from-image.onrender.com/solve-sudoku"

    # Define the input payload: a single string of digits representing the Sudoku puzzle
    # 0 represents empty cells
    payload = {
        "message": "002050006000004070108090000000706080706000204080502000000010308090400000800020400"
    }

    # Make a POST request to the endpoint
    response = requests.post(url, json=payload)

    # Print the status code
    print(f"Status Code: {response.status_code}")

    # Print the response
    if response.status_code == 200:
        print("Solution:")
        print(response.json())
    else:
        print(f"Error: {response.text}")

# Run the test function
if __name__ == "__main__":
    test_solve_sudoku()
