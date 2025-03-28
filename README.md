# 🚀 Sudoku Solver Server – The Brain Behind the Puzzle

Welcome to the server side of the Sudoku Solver project! This FastAPI-powered service is the backbone of our multi-modular system, processing images, extracting Sudoku grids, recognizing digits via Tesseract OCR and OpenCV, and solving puzzles with a custom DFS algorithm. Containerized with Docker, it’s built for reliability, scalability, and ease-of-deployment.

---

## 🔍 What It Does

- **Image Processing & OCR**  
  The `/process-image` endpoint accepts a Sudoku image, pre-processes it to extract the grid, and uses Tesseract OCR to recognize the digits. It returns a JSON payload with the recognized puzzle as a string.

- **Sudoku Solving**  
  The `/solve-sudoku` endpoint takes an 81-character string (with zeros for empty cells), runs a DFS-based solver, and returns the completed puzzle.

- **Testing Endpoints**  
  Dummy endpoints such as `/process-image-test` and `/solve-sudoku-test` help in verifying the server's functionality.

---

## 🛠️ Tech Stack

- **FastAPI** – The web framework powering our API.
- **Uvicorn** – ASGI server for high-performance asynchronous serving.
- **Tesseract OCR & OpenCV** – For image pre-processing and digit recognition.
- **Python** – The primary programming language.
- **Docker** – Containerization for consistent deployment across environments.

---

## 📁 Project Structure

```
server
├── .git
├── .gitignore
├── Dockerfile
├── __init__.py
├── docker_tests/
│   ├── docker_webservice_live.py
│   ├── post_test_docker.py
│   ├── solve_sudoku_docker_test.py
│   ├── solve_sudoku_test.py
│   └── test_images/
│       ├── sudoku_test_image_0.png
│       └── sudoku_test_image_1.png
├── fastapi_server/
│   ├── __init__.py
│   ├── main.py
│   └── timeout.py
├── preprocessing/
│   ├── __init__.py
│   ├── recognize_digits.py
│   └── sudoku_preprocessing.py
├── pyproject.toml
├── requirements.txt
├── sudoku_solver/
│   ├── __init__.py
│   ├── search.py
│   ├── sudoku_solver.py
│   └── utils.py
├── tests/
```


---

## 🚀 Running the Server

### Locally

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/davideblesse/sudoku-solver-server.git
    cd sudoku-solver-server
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Server Using Uvicorn:**

    ```bash
    uvicorn fastapi_server.main:app --reload
    ```

   The server will start on [http://127.0.0.1:8000](http://127.0.0.1:8000).

### With Docker

1. **Build the Docker Image:**

    ```bash
    docker build -t sudoku-solver-server .
    ```

2. **Run the Docker Container:**

    ```bash
    docker run -d -p 8000:8000 sudoku-solver-server
    ```

   The server will be accessible on port 8000.

---

## 🔁 Testing

The repository includes several test scripts:

- **Docker Tests:**  
  For example, run the Sudoku solving test via Docker with:
  
    ```bash
    python docker_tests/solve_sudoku_test.py
    ```

- **Local Tests:**  
  Additional tests can be found in the `tests/` directory.

---

## 🤝 Integration with the Overall System

This server is one of four core modules in the Sudoku Solver project:
- **Client:** A Flutter-based mobile app for capturing and sending Sudoku puzzles.
- **Auth:** A secure authentication service using MongoDB and JWT (HS256).
- **Aggregator:** The central repository that ties all submodules together.

For more details on the complete system, please refer to the main aggregator repository.

---

## 🤝 Contributing

Contributions, bug reports, and feature suggestions are welcome! Please open an issue or submit a pull request on [GitHub](https://github.com/davideblesse).

---

## ⚖️ License

This project is open-source under the [MIT License](LICENSE).

