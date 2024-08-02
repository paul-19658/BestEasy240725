import os
from PIL import Image
import requests
# 失败
imgSrc='https://initiate.alphacoders.com/download/picfiles/2/jpg'
imgResponse = requests.get(imgSrc)

img=Image.open(imgResponse.url)

imgSize = img.size

imgHeight = img.height

imgWidth = img.width

img.close()
print('图片{}，尺寸为{}。'.format(imgSrc, imgSize))