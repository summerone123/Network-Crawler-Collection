import requests
from bs4 import BeautifulSoup
import re
import json
def get():
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    url='https://news.sina.cn/zt_d/maoyi0109'
    r = requests.get(url,headers=headers)
    r.encoding = 'utf-8'
    test=re.findall(re.compile(r'window.SM = (.*?)\t\n\tvar', re.S), r.text)[0]
    with open('新浪.json', 'w', encoding='utf-8') as f:
        json.dump(json.loads(test), f, indent=4, ensure_ascii=False)
dict={}
with open('新浪.json','r',encoding='utf-8') as f:
    data=json.load(f)
    for i in data['data']['apiRes']['data']['components'][1]['data']:
        dict[i['name']]=[]
    for i in data['data']['apiRes']['data']['components'][2:5]:
        for j in i['data']:
            dict1={}
            dict1['url']=j['url']
            dict1['title']=j['title']
            dict1['time']=j['date']
            dict[i['meta']['title']].append(dict1)
    for i in data['data']['apiRes']['data']['components'][6:8]:
        for j in i['data']:
            dict1 = {}
            dict1['url'] = j['url']
            dict1['title'] = j['title']
            dict1['time'] = j['date']
            dict[i['meta']['title']].append(dict1)
    for i in data['data']['apiRes']['data']['components'][10:11]:
        for j in i['data']:
            dict1 = {}
            dict1['url'] = j['url']
            dict1['title'] = j['title']
            dict1['time'] = j['date']
            dict[i['meta']['title']].append(dict1)

def get2(url,str1,a):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    s='Zepto1561260046'+str(a)+'('
    test=r.text.lstrip(s).rstrip(')')
    with open('新浪1.json', 'w', encoding='utf-8') as f:
        json.dump(json.loads(test), f, indent=4, ensure_ascii=False)
    with open('新浪1.json', 'r', encoding='utf-8') as f:
        data=json.load(f)
        for i in data['result']['data']['data']:
            dict1 = {}
            dict1['url'] = i['url']
            dict1['title'] = i['title']
            dict1['time'] = i['date']
            dict[str1].append(dict1)
a=585

for i in range(8):
    url = 'https://interface.sina.cn/wap_api/wap_std_subject_feed_list.d.json?component_id=_conf_34|wap_zt_std_theme_feed|http://news.sina.cn/zt_d/maoyi0109&page=2&_=1561260054831&callback=Zepto1561260046'+str(a)
    print(url)
    get2(url,'市场影响',a)
    a = a + 2
for i in range(7):
    url = 'https://interface.sina.cn/wap_api/wap_std_subject_feed_list.d.json?component_id=_conf_34|wap_zt_std_theme_feed|http://news.sina.cn/zt_d/maoyi0109&page=2&_=1561260054831&callback=Zepto1561260046'+str(a)
    print(url)
    get2(url,'分析评论',a)
    a = a + 2
for i in range(4):
    url = 'https://interface.sina.cn/wap_api/wap_std_subject_feed_list.d.json?component_id=_conf_34|wap_zt_std_theme_feed|http://news.sina.cn/zt_d/maoyi0109&page=2&_=1561260054831&callback=Zepto1561260046'+str(a)
    print(url)
    get2(url,'中方回应',a)
    a = a + 2
for i in range(1):
    url = 'https://interface.sina.cn/wap_api/wap_std_subject_feed_list.d.json?component_id=_conf_34|wap_zt_std_theme_feed|http://news.sina.cn/zt_d/maoyi0109&page=2&_=1561260054831&callback=Zepto1561260046'+str(a)
    print(url)
    get2(url,'不可靠实体清单制度',a)
    a = a + 2
for i in range(2):
    url = 'https://interface.sina.cn/wap_api/wap_std_subject_feed_list.d.json?component_id=_conf_34|wap_zt_std_theme_feed|http://news.sina.cn/zt_d/maoyi0109&page=2&_=1561260054831&callback=Zepto1561260046'+str(a)
    print(url)
    get2(url,'赴美提醒',a)
    a = a + 2
for i in range(1):
    url = 'https://interface.sina.cn/wap_api/wap_std_subject_feed_list.d.json?component_id=_conf_34|wap_zt_std_theme_feed|http://news.sina.cn/zt_d/maoyi0109&page=2&_=1561260054831&callback=Zepto1561260046'+str(a)
    print(url)
    get2(url,'中国经济底气',a)
    a = a + 2

with open('新浪最终.json', 'w', encoding='utf-8') as f:
    json.dump(dict, f, indent=4, ensure_ascii=False)
