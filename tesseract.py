from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path = r'C:\Users\contr\Desktop\ocr\img.jpg'  # image path
img = Image.open(path)  # opening the images
text = pytesseract.image_to_string(img, lang='eng')
print(text)
