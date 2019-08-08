import requests
from bs4 import BeautifulSoup
import os
import re
def get(url):
    list=[]
    r = requests.get(url)
    r.encoding = 'utf-8'
    test=re.findall(re.compile(r'<!--(.*?)-->', re.S), r.text)[1]
    print(test)
    if test!='pc和手机适配代码开始':
        r.encoding='gb2312'
    soup = BeautifulSoup(r.text, 'html.parser')
    list.append('标题：'+soup.find('h1').text.strip())
    x=soup.find(class_='left-t').text.split(u'\u3000')
    list.append('发布时间：'+x[0])
    list.append('来源：中新网')
    tag=soup.find(class_='left_zw')
    wz=''
    for i in tag.find_all('p'):
        try:
            s=i.script.text
            wz = wz + i.text.replace(s, '').strip()
        except:
            wz=wz+i.text.strip()
    list.append('正文：'+wz)
    with open(os.getcwd() + '\\中新网\\' + soup.find('h1').text.strip() + '.txt', 'w', encoding='utf-8') as l:
        for i in list:
            l.write(i)
            l.write('\n')

with open('中新网.txt','r') as f:
    list=f.readlines()
for i in list:
    print(i)
    try:
        get(i.replace('\n',''))
    except:
        print('error')