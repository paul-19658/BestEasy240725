import time

import requests
from bs4 import BeautifulSoup

from requests.exceptions import HTTPError

# 网站的第三部分 ‘系列’
# https://www.52112.com/atlas/21001_1.html
# li class=lis-item -> a -> img.src √

# status_forcelist = [429, 500, 502, 503, 504]  # 需要强制重试的HTTP状态码列表

# page 86 completed! 7/30 14:04
for pageNum1 in range(91,21400):
    for pageNum2 in range(1,50):

        url=f'https://www.52112.com/atlas/{pageNum1}_{pageNum2}.html'
        # print(url)

        response = requests.get(url)
        # 一二层循环异常在这里
        print('下面执行：', url)

        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        if soup.find('title').text == '404错误 页面找不到':  # 这个404异常怎么也不报，干脆先这样来
            print('404 not found')
            break
        liList=soup.findAll('li',class_='lis-item')
        i = 0 # 记录每页的图片数量
        for li in liList:
            i+=1
            imgSrc=li.find('img').get('src')
            # print(imgSrc)
            imgResponse = requests.get(imgSrc)

            imgName = imgSrc.split('/')[-1]

            with open('../imgGot3/' + imgName, mode='wb') as f:
                f.write(imgResponse.content)

            print(imgName, ':completed,num:', i)
            time.sleep(0.5)
        print('page {}-{} completed!'.format(pageNum1,pageNum2))
        time.sleep(5)
    print('page {} completed!'.format(pageNum1))
    time.sleep(5)
print('all completed!',time.time())




        # session = requests.Session()  # 创建Session对象
        # session.mount('http://', adapter)  # 将适配器挂载到Session对象上
        # session.mount('https://', adapter)  # 将适配器挂载到Session对象上
        # try:
        #     requests.get(url)  # 发送GET请求
        #     # print(response.text)
        #     time.sleep(10) # 页面的确404 但捕获不到异常
        # # except requests.exceptions.Timeout as e:
        # #     print(e)
        # # except requests.exceptions.HTTPError as e:
        # #     print(e.)
        # except requests.exceptions.RequestException as e:
        #     print(f"发生了一个错误: {e.response.status_code}")
        #




        # except HTTPError as e:  # 如果发生HTTPError异常（HTTP错误状态码），则进行重试或跳过当前请求（根据具体情况而定）
        #     print(e.response.status_code)
        #     if e.response.status_code in status_forcelist:  # 如果HTTP状态码在需要强制重试的列表中，则进行重试（根据重试策略）
        #         pass  # 进行重试或跳过当前请求（根据具体情况而定
        #     else:
        #         print(11111)
