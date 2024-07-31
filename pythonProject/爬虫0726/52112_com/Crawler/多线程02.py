import time
import threading
import requests
from bs4 import BeautifulSoup


# 网站的第三部分 ‘系列’
# 8线程：线程1跑0-2500 线程2跑 2501-5000，，，， 实测（观测 1min < 600张 效率提了差不多5-6倍
# 7/30 17：50 {10157 2684 7782 17620 12657 15284 373 5203}

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
                with open('../imgGot7/' + imgName, mode='wb') as f: # 这里手动换吧
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
    thread1 = threading.Thread(target=crawl, args=(373, 1250))
    thread2 = threading.Thread(target=crawl, args=(1250, 2500))
    thread3 = threading.Thread(target=crawl, args=(2684, 3750))
    thread4 = threading.Thread(target=crawl, args=(3750, 5000))
    thread5 = threading.Thread(target=crawl, args=(5203, 6250))
    thread6 = threading.Thread(target=crawl, args=(6250, 7500))
    thread7 = threading.Thread(target=crawl, args=(7782, 8750))
    thread8 = threading.Thread(target=crawl, args=(8750, 10000))
    thread9 = threading.Thread(target=crawl, args=(10157, 11250))
    thread10 = threading.Thread(target=crawl, args=(11250, 12500))
    thread11 = threading.Thread(target=crawl, args=(12657, 13750))
    thread12 = threading.Thread(target=crawl, args=(13750, 15000))
    thread13 = threading.Thread(target=crawl, args=(15284, 16250))
    thread14 = threading.Thread(target=crawl, args=(16250, 17500))
    thread15 = threading.Thread(target=crawl, args=(17620, 18750))
    thread16 = threading.Thread(target=crawl, args=(18750, 20000))

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
