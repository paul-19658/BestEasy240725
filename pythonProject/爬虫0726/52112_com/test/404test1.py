import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError


#  '404错误 页面找不到'
url='https://www.52112.com/atlas/1_2.html'

try:

    response=requests.get(url)
    html=response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find('title').text)
    if soup.find('title').text=='404错误 页面找不到':# 这个404怎么也不报，干脆先这样来
        print(11111)

except requests.exceptions.HTTPError as e:
    print(e)

except requests.exceptions.RequestException as e:
    print(f"发生了一个错误: {e.response.status_code}")
