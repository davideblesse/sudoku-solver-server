# Use an official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /sudoku_server

# Install system-level dependencies for Tesseract, OpenGL, and Python
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project into the container
COPY . .

# Install the project as a package
RUN pip install --no-cache-dir .

# Expose the port your app runs on
EXPOSE 8000

# Default command to run your FastAPI app
CMD ["uvicorn", "fastapi_server.main:app", "--host", "0.0.0.0", "--port", "8000"]

