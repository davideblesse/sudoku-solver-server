import requests

def test_server():
    url = "https://sudoku-solver-from-image.onrender.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Server is up and running. Received HTTP 200 OK.")
    else:
        print(f"Failed to reach server. Status code: {response.status_code}")

if __name__ == "__main__":
    test_server()