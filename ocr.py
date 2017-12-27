# brew install tesseract
# pip3 install Pillow   pytesseract需要通过Pillow加载图片
# pip3 install pytesseract   pytesseract是google的开源文本识别库Tesseract-OCR的python绑定

from PIL import Image
import pytesseract as ocr
import urllib.request as urlreq
from io import BytesIO

#resp = urlreq.urlopen('http://www.wisedream.net/res/img/ocr-test.png')
IMAGE_NAME = "1.png"
img = Image.open("./data_bank/绿新/"+IMAGE_NAME)
print(ocr.image_to_string(img,lang='chi_sim'))