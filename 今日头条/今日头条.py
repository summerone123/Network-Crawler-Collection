import requests
import json
import re
import time
from bs4 import BeautifulSoup
headers={
'accept': 'application/json, text/javascript',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'tt_webid=6705141215840847367; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16b7c865cbc1cd-03c4c04bb30471-3f385804-1fa400-16b7c865cbd87f; CNZZDATA1259612802=1689490705-1561161529-https%253A%252F%252Fwww.baidu.com%252F%7C1561161529; tt_webid=6705141215840847367; __tasessionId=rsqfm9kam1561162309554; csrftoken=7a31b45c7231b3c34e468381e89ecdec; s_v_web_id=729f00b0ea5f35d831ac760da8210174',
'referer': 'https://www.toutiao.com/search/?keyword=%E4%B8%AD%E7%BE%8E%E8%B4%B8%E6%98%93%E6%88%98',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'
}
id=[]
a=0
def paser_page_index(a):
    while True:
        url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=' + str(a) + '&format=json&keyword=%E4%B8%AD%E7%BE%8E%E8%B4%B8%E6%98%93%E6%88%98&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis'
        respond = requests.get(url,headers=headers)
        dict1=respond.json()
        with open('今日头条.json', 'w', encoding='utf-8')as f:
            json.dump(dict1, f, indent=4, ensure_ascii=False)
        id1 = re.findall(re.compile(r"'group_id': '(.*?)',", re.S), str(dict1))
        id.extend(id1)
        a=a+20
        if dict1['has_more']!=1:
            break
paser_page_index(a)
def get_page_detail(url,super):
    r = requests.get(url)
    r.encoding = 'utf-8'
    article = {}
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup.prettify())
    str = soup.text
    tag = r'chineseTag: \'(.*?)\''
    p = re.compile(tag, re.S)
    if re.findall(p, str)==[] or re.findall(p, str)==['']:
        return 0
    if re.findall(p, str)[0] == '问答':
        return 1
    if re.findall(p, str)[0] == '图片':
        return 2
    article['type'] = re.findall(p, str)[0]
    title = r'title: \'(.*?)\''
    time = r'time: \'(.*?)\''
    content = r'content: \'(.*?)\''
    luan = r'&.*?gt;|&.*?quot;'
    p1 = re.compile(title, re.S)
    article['title'] = re.findall(p1, str)[0]
    p2 = re.compile(time, re.S)
    article['time'] = re.findall(p2, str)[0]
    p3 = re.compile(content, re.S)
    str1 = re.findall(p3, str)[0]
    p4 = re.compile(luan, re.S)
    str2 = ''
    article['news'] = re.sub(p4, str2, str1)
    super.append(article)
super=[]
with open('今日头条.json', 'a', encoding='utf-8') as f:
    for i in id:
        url = 'https://www.toutiao.com/a' + i
        print(url)
        a = get_page_detail(url,super)
        if a == 0:
            print('这是一条广告或者无法解析该网页')
        if a == 1:
            print('这篇文章是个问答')
        if a == 2:
            print('这是一个图片类文章')
    json.dump(super, f, indent=4, ensure_ascii=False)