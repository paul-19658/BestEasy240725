import time
import threading
import requests
from bs4 import BeautifulSoup


# 8/2 11:17 planA 碰到异步加载问题 这边先苦苦爬着
# https://initiate.alphacoders.com/download/picfiles/514851/jpg
# 11:26 0--160000 先跑着吧 可能会有404 看看
def crawl(startNUM, endNUM):
    print('\n\nT H R E A D    S T A R T !\n N U M： {}-{}\n\n'.format(startNUM, endNUM))
    time.sleep(3)
    i=0
    for pageNum1 in range(startNUM, endNUM):
        i+=1
        imgSrc = f'https://initiate.alphacoders.com/download/picfiles/{pageNum1}/jpg'

        try:
            imgResponse = requests.get(imgSrc)

            imgName = imgSrc.split('/')[-2] + '.jpg'

            lock.acquire()
            with open('F:/爬虫202407/ZC_爬虫_0726/alphacoders_com/imgGot/' + imgName, mode='wb') as f:  # 这里手动换吧
                f.write(imgResponse.content)
            lock.release()
            print(imgName, ':completed,num:', i)
            time.sleep(0.5)
        except:
            pass

    print('NUM : {}--{} completed!'.format(startNUM, endNUM))


if __name__ == '__main__':
    lock = threading.Lock()
    thread1 = threading.Thread(target=crawl, args=(6500, 10000))
    thread2 = threading.Thread(target=crawl, args=(16500, 20000))
    thread3 = threading.Thread(target=crawl, args=(26500, 30000))
    thread4 = threading.Thread(target=crawl, args=(36500, 40000))
    thread5 = threading.Thread(target=crawl, args=(46500, 50000))
    thread6 = threading.Thread(target=crawl, args=(56500, 60000))
    thread7 = threading.Thread(target=crawl, args=(66500, 70000))
    thread8 = threading.Thread(target=crawl, args=(76500, 80000))
    thread9 = threading.Thread(target=crawl, args=(86500, 90000))
    thread10 = threading.Thread(target=crawl, args=(96500, 100000))
    thread11 = threading.Thread(target=crawl, args=(106500, 110000))
    thread12 = threading.Thread(target=crawl, args=(116500, 120000))
    thread13 = threading.Thread(target=crawl, args=(126500, 130000))
    thread14 = threading.Thread(target=crawl, args=(136500, 140000))
    thread15 = threading.Thread(target=crawl, args=(146500, 150000))
    thread16 = threading.Thread(target=crawl, args=(156500, 160000))

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
