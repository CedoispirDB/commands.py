import pytesseract
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd ="/tesseract.exe"
text = pytesseract.image_to_string("/Users/imgs/text.png")

print(text)
