"""
本地筛选 通用
"""
# 8/2 坏掉的图片也要删除然后统计

import os
from PIL import Image

path=r'F:/爬虫202407/ZC_爬虫_0726/alphacoders_com/imgGot/'

fileList=os.listdir(path)

count1=0 # 符合要求的

count2=0 # 不符合要求的

count3=0 # 损坏的图片



for file in fileList:
    # print(file)
    imgSrc=path+'/'+file
    # print(imgSrc)

    try:
        img=Image.open(imgSrc)
        imgSize = img.size

        imgHeight = img.height

        imgWidth = img.width

        img.close()

        # 删除 不符合
        if img.width < 4000 or img.height < 4000:
            os.remove(imgSrc)
            print('图片{}，尺寸为{}，不符合要求，已删除。'.format(imgSrc, imgSize))
            count2 = count2 + 1
        else:
            print('图片{}，尺寸为{}，符合要求。'.format(imgSrc, imgSize))
            count1 = count1 + 1
    except:
        try:
            os.remove(imgSrc) # 删除坏掉的图片
            count3+=1
        except:
            pass

print('统计：\n符合要求的数量：{}，不符合要求的数量：{}，损坏的图片：{}'.format(count1,count2,count3))