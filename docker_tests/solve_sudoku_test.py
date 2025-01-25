import requests

def test_solve_sudoku():
    # Define the FastAPI endpoint URL
    url = "https://sudoku-solver-from-image.onrender.com/solve-sudoku"  # Update the URL if your app is hosted elsewhere

    # Define the input payload
    payload = {
        "message": "123456789123456789123456789123456789"
    }

    # Make a POST request to the endpoint
    response = requests.post(url, json=payload)

    # Print the status code
    print(f"Status Code: {response.status_code}")

    # Print the response JSON
    if response.status_code == 200:
        print(f"Response: {response.json()}")
    else:
        print(f"Error: {response.text}")

# Run the test function
if __name__ == "__main__":
    test_solve_sudoku()
