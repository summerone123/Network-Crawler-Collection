import requests
from bs4 import BeautifulSoup
import re
import json
headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
with open('新浪最终.json','r',encoding='utf-8') as f:
    data=json.load(f)
for i in data:
    for j in data[i]:
        url=j['url']
        r = requests.get(url,headers=headers)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        content=''
        for i in soup.find_all(class_='art_p'):
            content=content+i.text+' '
        j['content']=content
with open('新浪新闻.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)