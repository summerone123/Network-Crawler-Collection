import requests
from bs4 import BeautifulSoup
import re
import os
from get_page_index import get_page_index
import random
import time
import json

def get_page_detail():
    x = 1
    for a in range(1,101):
        url = get_page_index(a)
        for i in url:
            cookie = 'CXID=D3C82EBD52CAD3CD37661CE6CB43323D; SUID=9D896FDF3965860A5C79DA8A000706A5;' \
                     ' ad=Wlllllllll2tWN$3lllllVeii5UlllllTLMJXyllllGllllllklll5@@@@@@@@@@; ' \
                     'SUV=00F625CFDA1D66725C7A93E4454D8038; IPLOC=CN3211; ld=5kllllllll2tWI56lllllVe@' \
                     'ej9lllllLPCutkllllwlllllxklll5@@@@@@@@@@; LSTMV=181%2C182; LCLKINT=1799; ' \
                     'SNUID=8F9B7DCE111491D796C5A710126DE258; ABTEST=0|1552263620|v1; weixinIndexVisited=1; ' \
                     'JSESSIONID=aaa79YWY2nTYwaVwkyZKw; sct=2; ppinf=5|1552265953|1553475553|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1' \
                     'bmlxbmFtZToxODolRTklQkUlOTklRTclODQlQjF8Y3J0OjEwOjE1NTIyNjU5NTN8cmVmbmljazoxODolRTklQkUlOTklRTclODQlQ' \
                     'jF8dXNlcmlkOjQ0Om85dDJsdUlKdy1qUnlmTk82aHJ6eEJPNlA0Z0lAd2VpeGluLnNvaHUuY29tfA; ' \
                     'pprdig=FhVHVDJ1voQNQAHOrpoHxdcSK0RtPht2eeRQX5St1LFciZBZIbBsmrI_mbOmfjEw_8y74UNVxbPP2' \
                     'o5EaEFTSeexya-CyF9C4w3PGU5YBPCtI8RBJjzy3eGs7P0Oy9YFjwHpZ56Txsu7zzSP5le7iNWX1L_B7FG3KIvVid3hSPE; ' \
                     'sgid=26-39648041-AVyFsuGuyZvqHco3dM47gb0; ppmdig=1552265954000000620fe5efccdbba904a7bdb36299404a7'
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
            headers = {'Cookie': cookie, 'user-agent': user_agent, 'x-requested-with': 'XMLHttpRequest'}
            respond = requests.get(i, headers=headers)
            respond.encoding = 'utf-8'
            if respond.status_code == 200:
                soup = BeautifulSoup(respond.text, 'html.parser')
                str = soup.text
                # print(soup.prettify())
            list = []
            dict={}
            try:
                title = (soup.find(id='activity-name').text).strip()
            except:
                print('这个网页是一个视频或者无法解析的网页')
                continue
            title = re.sub(r'[\\/:*?"<>|]', '', title)
            writer = '作者 ：' + (soup.find(class_='rich_media_meta rich_media_meta_text').text).strip()
            wpa = '公众号：' + (soup.find(id='js_name').text).strip()
            time1 = '发布时间：' + re.findall(re.compile(r',s="(.*?)";', re.S), str)[0]
            number = '微信号：' + soup.find_all(class_='profile_meta_value')[0].text
            power = '功能介绍：' + soup.find_all(class_='profile_meta_value')[1].text
            dict['title']=title
            dict['writer'] = writer
            dict['wpa'] = wpa
            dict['time1'] = time1
            dict['number'] = number
            dict['power'] = power
            list.extend([title, writer, wpa, time1, number, power])
            tag = soup.find(id='js_content')
            tag1 = tag.find_all({'span', 'h2', 'h3', 'p'})
            str = ''
            for i in tag1:
                if str.find(i.text) != -1:
                    continue
                else:
                    str = str + i.text
            list.append(str)
            dict['content']=str
            with open('中美贸易战.json', 'a', encoding='utf-8', newline='') as f:
                json.dump(dict, f, indent=4, ensure_ascii=False)
            with open(os.getcwd() + '\\中美贸易战\\' + title + '.txt', 'w', encoding='utf-8') as l:
                for i in list:
                    l.write(i)
                    l.write('\n')
            print('成功%d次' % x)
            x = x + 1
        time.sleep(random.randint(10,20))