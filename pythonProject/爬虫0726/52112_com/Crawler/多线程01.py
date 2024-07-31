import time
import threading
import requests
from bs4 import BeautifulSoup

# 网站的第三部分 ‘系列’
# 2线程 demo：线程1跑0-10000 线程2跑 10000+

# page 140-10 completed! page 10056-1 completed! 14:54

# 1
def crawl1():
    for pageNum1 in range(99, 10000):
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
                with open('../imgGot3/' + imgName, mode='wb') as f:
                    f.write(imgResponse.content)
                lock.release()
                print(imgName, ':completed,num:', i)
                time.sleep(0.5)
            print('page {}-{} completed!'.format(pageNum1, pageNum2))
            time.sleep(5)
        print('page {} completed!'.format(pageNum1))
        time.sleep(5)
    print('PAGE IN 10000--20000 completed!', time.time())


# 2
def crawl2():
    for pageNum1 in range(10008, 21400):
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
                with open('../imgGot3/' + imgName, mode='wb') as f:
                    f.write(imgResponse.content)
                lock.release()
                print(imgName, ':completed,num:', i)
                time.sleep(0.5)
            print('page {}-{} completed!'.format(pageNum1, pageNum2))
            time.sleep(5)
        print('page {} completed!'.format(pageNum1))
        time.sleep(5)
    print('PAGE IN 0--10000 completed!', time.time())


if __name__ == '__main__':
    lock = threading.Lock()
    thread1 = threading.Thread(target=crawl1)
    thread1.start()
    thread2 = threading.Thread(target=crawl2)
    thread2.start()
