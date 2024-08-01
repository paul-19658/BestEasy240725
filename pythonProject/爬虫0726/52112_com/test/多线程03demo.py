import os
import time
import threading
import requests
from bs4 import BeautifulSoup

# 网站的第三部分 ‘系列’
# 2024/7/31 自动切换写入目录 100% 52112_com 90%

# 加个文件夹数量检测
gl_dirNum: int = 90

# 获取目录下文件数量
def getfileNum() -> int:
    global gl_dirNum
    fileList = os.listdir(f'../imgGot{gl_dirNum}/')
    # print(len(fileList))
    return len(fileList)

# 这两个函数已合并在下方 countAndChange
# def fileNumCount(maxFileNum):
#     global gl_dirNum
#     while True:
#         print('\n\n当前文件夹内图片数：{}/{}\n\n'.format(getfileNum(), maxFileNum))
#
#
# # count change 可以合在一起
# def changeDir(maxFileNum):
#     global gl_dirNum
#
#     while True:
#         if getfileNum() >= maxFileNum:
#             lock.acquire()
#             gl_dirNum += 1
#             lock.release()
#             print('更改存储目录为：{}'.format(f'../imgGot{gl_dirNum}/'))
#         time.sleep(2)


# 记录文件数量并自动创建和切换目录
def countAndChange(maxFileNum):
    global gl_dirNum
    while True:
        print('\n\n当前文件夹({})内图片数：{}/{}\n\n'.format(f'../imgGot{gl_dirNum}/',getfileNum(), maxFileNum))
        if getfileNum() >= maxFileNum:

            if not os.path.exists(f'../imgGot{gl_dirNum+1}/'):
                os.makedirs(f'../imgGot{gl_dirNum + 1}/')
                print('已创建新目录:{}'.format(f'../imgGot{gl_dirNum + 1}/'))

            lock.acquire()
            gl_dirNum += 1
            lock.release()
            print('\n\n更改存储目录为：{}\n\n'.format(f'../imgGot{gl_dirNum}/'))
        time.sleep(10) # 这个时间要改

# 爬虫
def crawl(startPAGE, endPAGE):
    global gl_dirNum
    print('\n\nT H R E A D    S T A R T !\n P A G E {}-{}\n\n'.format(startPAGE, endPAGE))
    time.sleep(3)
    for pageNum1 in range(startPAGE, endPAGE):
        for pageNum2 in range(1, 50):

            url = f'https://www.52112.com/atlas/{pageNum1}_{pageNum2}.html'
            # print(url)

            response = requests.get(url)
            # 一二层循环异常在这里
            print('下面执行：', url)

            html = response.text
            savedDir=f'../imgGot{gl_dirNum}/'
            soup = BeautifulSoup(html, 'html.parser')
            if soup.find('title').text == '404错误 页面找不到':  # 这个404异常怎么也不报，干脆先这样来
                print('404 not found')
                break
            liList = soup.findAll('li', class_='lis-item')
            i = 0  # 记录每页的图片数量
            for li in liList:
                i += 1
                imgSrc = li.find('img').get('src')
                # print(imgSrc)
                imgResponse = requests.get(imgSrc)

                imgName = imgSrc.split('/')[-1]

                lock.acquire()
                with open(savedDir + imgName, mode='wb') as f:  # 这里手动换吧
                    f.write(imgResponse.content)
                lock.release()
                print(savedDir, imgName, ':completed,num:', i)
                time.sleep(0.5)
            print('page {}-{} completed!'.format(pageNum1, pageNum2))
            # time.sleep(5)
        print('page {} completed!'.format(pageNum1))
        # time.sleep(5)
    print('PAGE IN {}--{} completed!'.format(startPAGE, endPAGE))


if __name__ == '__main__':


    lock = threading.Lock()
    thread_countAndChange = threading.Thread(target=countAndChange, args=(50,))

    thread1 = threading.Thread(target=crawl, args=(401, 1250))

    thread2 = threading.Thread(target=crawl, args=(1265, 2500))

    thread_countAndChange.start()
    thread1.start()
    thread2.start()




    # thread1 = threading.Thread(target=crawl, args=(396, 1250))416
    # thread2 = threading.Thread(target=crawl, args=(1264, 2500))1292
    # thread3 = threading.Thread(target=crawl, args=(2700, 3750))2720
    # thread4 = threading.Thread(target=crawl, args=(3764, 5000))3784
    # thread5 = threading.Thread(target=crawl, args=(5236, 6250))5277
    # thread6 = threading.Thread(target=crawl, args=(6277, 7500))6308
    # thread7 = threading.Thread(target=crawl, args=(7805, 8750))7821
    # thread8 = threading.Thread(target=crawl, args=(8778, 10000))8820
    # thread9 = threading.Thread(target=crawl, args=(10158, 11250))10183
    # thread10 = threading.Thread(target=crawl, args=(11262, 12500))11263
    # thread11 = threading.Thread(target=crawl, args=(12676, 13750))12712
    # thread12 = threading.Thread(target=crawl, args=(13787, 15000))13822
    # thread13 = threading.Thread(target=crawl, args=(15302, 16250))15340
    # thread14 = threading.Thread(target=crawl, args=(16281, 17500))16331
    # thread15 = threading.Thread(target=crawl, args=(17629, 18750))17663
    # thread16 = threading.Thread(target=crawl, args=(18769, 20000))18795
    #
    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
    # thread5.start()
    # thread6.start()
    # thread7.start()
    # thread8.start()
    # thread9.start()
    # thread10.start()
    # thread11.start()
    # thread12.start()
    # thread13.start()
    # thread14.start()
    # thread15.start()
    # thread16.start()
