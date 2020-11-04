import pytesseract
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/marco/AppData/Local/Tesseract-OCR/tesseract.exe'
img = cv2.imread('C:/Users/marco/Desktop/drawn.png')
text = pytesseract.image_to_string(img)

print(text)
