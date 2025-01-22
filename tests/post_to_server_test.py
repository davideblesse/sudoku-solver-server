import os
import requests

# Server URL
url = "https://sudoku-solver-app-v0gc.onrender.com/process-image"

# Resolve the image path
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, "test_images", "sudoku_test_image_0.png")

# Check if the file exists
if not os.path.exists(image_path):
    print(f"Error: File not found at {image_path}")
else:
    # Open the image file and send a POST request
    with open(image_path, "rb") as file:
        response = requests.post(url, files={"file": file})

    # Print the server response
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print(f"Failed with status {response.status_code}: {response.text}")
