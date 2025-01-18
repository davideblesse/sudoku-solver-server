from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io

app = FastAPI()

@app.post("/process-image")
async def process_image(file: UploadFile = File(...)):
    # Read the file into memory
    file_bytes = await file.read()

    # Use Pillow to open the image
    image = Image.open(io.BytesIO(file_bytes))

    # Perform some Pillow operations (example: get size)
    width, height = image.size

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "width": width,
        "height": height,
        "message": "Image processed successfully"
    }

