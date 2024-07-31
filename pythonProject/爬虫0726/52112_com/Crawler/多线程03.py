import time
import threading
import requests
from bs4 import BeautifulSoup


# 网站的第三部分 ‘系列’
# 8线程：线程1跑0-2500 线程2跑 2501-5000，，，， 实测（观测 1min < 600张 效率提了差不多5-6倍
# 加个文件夹数量检测

def crawl(startPAGE, endPAGE):
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
                with open('../imgGot9/' + imgName, mode='wb') as f: # 这里手动换吧
                    f.write(imgResponse.content)
                lock.release()
                print(imgName, ':completed,num:', i)
                time.sleep(0.5)
            print('page {}-{} completed!'.format(pageNum1, pageNum2))
            # time.sleep(5)
        print('page {} completed!'.format(pageNum1))
        # time.sleep(5)
    print('PAGE IN {}--{} completed!'.format(startPAGE,endPAGE))


if __name__ == '__main__':
    lock = threading.Lock()
    thread1 = threading.Thread(target=crawl, args=(416, 1250))451 11:43
    thread2 = threading.Thread(target=crawl, args=(1292, 2500))1316
    thread3 = threading.Thread(target=crawl, args=(2720, 3750))2734
    thread4 = threading.Thread(target=crawl, args=(3784, 5000))3798
    thread5 = threading.Thread(target=crawl, args=(5277, 6250))5304
    thread6 = threading.Thread(target=crawl, args=(6308, 7500))6342
    thread7 = threading.Thread(target=crawl, args=(7821, 8750))7864
    thread8 = threading.Thread(target=crawl, args=(8820, 10000))8855
    thread9 = threading.Thread(target=crawl, args=(10183, 11250))10202
    thread10 = threading.Thread(target=crawl, args=(11263, 12500))11284
    thread11 = threading.Thread(target=crawl, args=(12712, 13750))12734
    thread12 = threading.Thread(target=crawl, args=(13822, 15000))13845
    thread13 = threading.Thread(target=crawl, args=(15340, 16250))15369
    thread14 = threading.Thread(target=crawl, args=(16331, 17500))16394
    thread15 = threading.Thread(target=crawl, args=(17663, 18750))17689
    thread16 = threading.Thread(target=crawl, args=(18795, 20000))18827

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread12.start()
    thread13.start()
    thread14.start()
    thread15.start()
    thread16.start()
