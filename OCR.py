from PIL import Image
import pytesseract

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with the correct path to your Tesseract executable

# Load an image
image = Image.open(r'C:\Users\pc\Desktop\WhatsApp Image 2024-07-03 at 14.06.33.jpeg')

# Perform OCR
text = pytesseract.image_to_string(image, lang='eng')

print(text)


