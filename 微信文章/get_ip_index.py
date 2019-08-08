import requests
from bs4 import BeautifulSoup
import random

# def get_ip_index():
#     randomlist=['/nn/','/wn/','/wt/']
#     url='https://www.xicidaili.com'+random.choice(randomlist)+str(random.randint(1,3))
#     print(url)
#     list=[]
#     proxies={}
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
#     r=requests.get(url,headers=headers)
#     soup=BeautifulSoup(r.text,'html.parser')
#     # print(soup.prettify())
#     tag=soup.find_all('tr')
#     for j in tag[1:]:
#         tag1=j.find_all('td')
#         list.append(tag1[1].text+':'+tag1[2].text)
#     for i in list:
#         try:
#             ip="https://" + i
#             proxies['https']=ip
#             r=requests.get('https://www.toutiao.com',headers=headers)
#         except:
#             list.remove(i)
#     print('成功获得代理%d个' % (len(list)))
#     return list
def get_ip_index():
    proxies = {}
    r = requests.get('http://127.0.0.1:5000/get')
    proxy = BeautifulSoup(r.text, "lxml").get_text()
    proxies['https'] = 'https://' + proxy
    return proxies