# 筛选 短边分辨率>=4096 也可以加一个异常处理，
# 把坏的图片删掉，一般在手动换文件夹的时候停掉的那一张会有问题

import os
from PIL import Image

path=r'../imgGot3'

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

    # # 删除 不符合
    # if img.width<4096 or img.height<4096:
    #     os.remove(imgSrc)
    #     print('图片{}，尺寸为{}，已删除。'.format(imgSrc,imgSize) )

    # 统计
    if img.width<4096 or img.height<4096:
        print('图片{}，尺寸为{}，不符合要求。'.format(imgSrc,imgSize) )
        count2=count2+1
    else:
        print('图片{}，尺寸为{}，符合要求。'.format(imgSrc, imgSize))
        count1=count1+1

print('统计：\n符合要求的数量：{}，不符合要求的数量：{}'.format(count1,count2))