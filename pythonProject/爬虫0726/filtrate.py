# 本地筛选 通用
#

import os
from PIL import Image

path=r'F:/爬虫202407/ZC_爬虫_0726/magdeleine_co/imgGot1/'

fileList=os.listdir(path)

count1=0 # 符合要求的

count2=0 # 不符合要求的

for file in fileList:
    # print(file)
    imgSrc=path+'/'+file
    # print(imgSrc)
    img=Image.open(imgSrc)

    imgSize=img.size

    imgHeight=img.height

    imgWidth=img.width

    img.close()

    # 删除 不符合
    if img.width<4000 or img.height<4000:
        os.remove(imgSrc)
        print('图片{}，尺寸为{}，已删除。'.format(imgSrc,imgSize) )

    # 统计
    if img.width<4000 or img.height<4000:
        print('图片{}，尺寸为{}，不符合要求。'.format(imgSrc,imgSize) )
        count2=count2+1
    else:
        print('图片{}，尺寸为{}，符合要求。'.format(imgSrc, imgSize))
        count1=count1+1

print('统计：\n符合要求的数量：{}，不符合要求的数量：{}'.format(count1,count2))