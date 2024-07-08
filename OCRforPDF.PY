import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import io

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with the correct path

def pdf_to_text(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""
    
    for page_num in range(len(document)):
        # Get the page
        page = document.load_page(page_num)
        
        # Get the pixmap (image)
        pix = page.get_pixmap()
        
        # Convert the pixmap to a PIL image
        img = Image.open(io.BytesIO(pix.tobytes()))
        
        # Perform OCR
        page_text = pytesseract.image_to_string(img, lang='eng')
        text += page_text
    
    return text

# Example usage
pdf_path = r'C:\Users\pc\Desktop\OR-6505950BC8E13.pdf'
text = pdf_to_text(pdf_path)
print(text)
