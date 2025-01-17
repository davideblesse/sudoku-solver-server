import requests

# URL of your deployed FastAPI server
url = "https://sudoku-solver-app-v0gc.onrender.com"

# Make a GET request
response = requests.get(url)

# Check the status code and response content
if response.status_code == 200:
    print("Server is working!")
    print("Response:", response.json())
else:
    print(f"Failed to connect. Status code: {response.status_code}")
    print("Response:", response.text)
