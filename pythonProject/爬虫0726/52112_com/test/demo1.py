import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

# div class='itemWra'->a href √

url='https://www.52112.com/list/0-0-0-0-0-0-0-0-0-0-0-0--900.html'

status_forcelist = [429, 500, 502, 503, 504]  # 需要强制重试的HTTP状态码列表

response=requests.get(url)

html=response.text

soup=BeautifulSoup(html,'html.parser')

img_src=soup.find('div', class_='itemWra').find('img').get('data-original')

try:
    img_response = requests.get(img_src)
except HTTPError as e: # 如果发生HTTPError异常（HTTP错误状态码），则进行重试或跳过当前请求（根据具体情况而定）
    if e.response.status_code in status_forcelist:  # 如果HTTP状态码在需要强制重试的列表中，则进行重试（根据重试策略）
        pass  # 进行重试或跳过当前请求（根据具体情况而定
    else:
        print('结束这次循环')



img_name=img_src.split('/')[-1]

with open('imgGot/'+img_name,mode='wb') as f:
    f.write(img_response.content)

print('okkkkkkkkkkkkkkkkkkkkkkkk')