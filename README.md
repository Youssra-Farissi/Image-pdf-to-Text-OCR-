Optical Character Recognition (OCR)
OCR (Optical Character Recognition) is a technology used to convert different types of documents, such as scanned paper documents, PDF files, or images captured by a digital camera into editable and searchable data.

Introduction
This project utilizes Tesseract, a widely-used OCR engine, to extract text from images and PDFs. Tesseract is open-source and supports multiple languages and file formats, making it a versatile choice for OCR tasks.

Getting Started
Installing Tesseract
To install Tesseract on Windows:

Download Tesseract:

Visit the Tesseract GitHub page or Tesseract OCR website to download the installer for Windows.
Install Tesseract:

Follow the installation instructions provided with the installer.
Set Environment Variables (if needed):

Add Tesseract to your system's PATH environment variable.
Using Tesseract with Python

comds after installing Tesseract :
for images :
pip install pytesseract Pillow
for pdf:
pip install pytesseract Pillow PyMuPDF

Example
This project includes simple Python scripts (OCR.py and OCRforPDF.py) that demonstrate how to use Tesseract to extract text from images and PDFs.
