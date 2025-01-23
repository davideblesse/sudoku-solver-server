import requests

# Define the URL of your FastAPI endpoint
url = "http://localhost:8000/process-image/"

# Define the path to your test image
image_path = "tests/test_images/sudoku_test_image_0.png"

# Open the image file in binary mode and send the POST request
with open(image_path, "rb") as image_file:
    files = {"file": image_file}
    response = requests.post(url, files=files)

# Print the response from the server
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
