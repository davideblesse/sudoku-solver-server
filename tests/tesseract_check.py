import pytesseract

def check_tesseract():
    try:
        version = pytesseract.get_tesseract_version()
        return f"Tesseract is installed: {version}"
    except pytesseract.TesseractNotFoundError:
        return "Tesseract is not installed or not found."

if __name__ == "__main__":
    print(check_tesseract())