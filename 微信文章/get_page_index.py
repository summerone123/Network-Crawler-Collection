import requests
from bs4 import BeautifulSoup
from urllib import parse
from get_ip_index import get_ip_index

proxies = {}
query=parse.quote('中美贸易战')
def get_page_index(a):
    global proxies
    list=[]
    cookie_list=['SMYUV=1559659915628259; SUV=00B70D22249C1B825D026DB93EC1F836; IPLOC=CN4101; SUID=7A661DDA6119940A000000005D0A26AD; pgv_pvi=7917577216; pgv_si=s9311622144; ABTEST=8|1560946351|v1; SNUID=E0FD86419A9E1036BF57F37C9BAC7614; weixinIndexVisited=1; JSESSIONID=aaa41hCxCNTa0gy8VhqTw; ppinf=5|1560946444|1562156044|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklQkUlOTklRTclODQlQjF8Y3J0OjEwOjE1NjA5NDY0NDR8cmVmbmljazoxODolRTklQkUlOTklRTclODQlQjF8dXNlcmlkOjQ0Om85dDJsdUlKdy1qUnlmTk82aHJ6eEJPNlA0Z0lAd2VpeGluLnNvaHUuY29tfA; pprdig=HwwSrn1DetPNyTmdtQmhB5uldIsSXmkZi5GFzySOxR6SPzTin9h1KTDtNoRZ2kFMwASgfaQTaQDhYEfAvxVJ8UvH5d6MUDhEIckKrTwVeDO_UMn2ySSzzsczNjGRcKO_1THBAFc4vutTPCSZhXsA8k9j3nhUNIDmDHGXjV-xmOQ; sgid=26-39648041-AV0KJwwdaibbg5x7rosMeRgo; ppmdig=1560946444000000c4fbceb18a47dfcdb4c63accd9b1d667; sct=2']
    url='https://weixin.sogou.com/weixin?query='+query+'&type=2&page='+str(a)+'&ie=utf8'
    url0='https://www.baidu.com'
    x=0
    while True:
        cookie='IPLOC=CN4101; SUID=81E1C0011F13940A000000005D0C861F; SUV=1561101795738258; ABTEST=6|1561101858|v1; pgv_pvi=909809664; pgv_si=s7944643584; weixinIndexVisited=1; sct=1; JSESSIONID=aaaEXlpAQQM16et0p5hRw; ppinf=5|1561102210|1562311810|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklQkUlOTklRTclODQlQjF8Y3J0OjEwOjE1NjExMDIyMTB8cmVmbmljazoxODolRTklQkUlOTklRTclODQlQjF8dXNlcmlkOjQ0Om85dDJsdUlKdy1qUnlmTk82aHJ6eEJPNlA0Z0lAd2VpeGluLnNvaHUuY29tfA; pprdig=Z7pgUlt3mKAVzm_pdLiZp8EDu-wBFiax288cIEkV0De2DMzGKT39K0eByCqZlWuQvaDbSiKX2ag2UTkPGw7hTtHfQgwpFp3q7R-PaFbQuzUJf8QefgVQ5cBJwfMJGJ2qAPT-iMzhDNrpMoJJQh-cjI3iGvOmLZlo6Up2914Ke_U; sgid=26-39648041-AV0Mh4Kz9IbRzLS8yBnFd7Y; ppmdig=1561102210000000dea8f209275a29a48c9197f1ed5b9325; PHPSESSID=j8qt5oju1fra9320ceipqg2167; SNUID=22344F8B5257DA81B2490CB5520D6C54'
        # cookie = 'CXID=D3C82EBD52CAD3CD37661CE6CB43323D; SUID=9D896FDF3965860A5C79DA8A000706A5; SUV=00F625CFDA1D66725C7A93E4454D8038; weixinIndexVisited=1; sw_uuid=4589143954; sg_uuid=5149051536; ssuid=9694528675; wuid=AAFhI/uHJgAAAAqLK0ZP7wIAGwY=; ld=ekllllllll2tWI56lllllVh85u6lllllLPCutkllll9lllllRklll5@@@@@@@@@@; LSTMV=183%2C331; LCLKINT=3324; pgv_pvi=7916063744; ABTEST=0|1556631348|v1; sct=17; IPLOC=CN3211; SNUID=1A0EE85787820FB416CBEFF388A910CB; JSESSIONID=aaaWAE9UzFLzZ7EmlmzPw; ppinf=5|1557147508|1558357108|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTklQkUlOTklRTclODQlQjF8Y3J0OjEwOjE1NTcxNDc1MDh8cmVmbmljazoxODolRTklQkUlOTklRTclODQlQjF8dXNlcmlkOjQ0Om85dDJsdUlKdy1qUnlmTk82aHJ6eEJPNlA0Z0lAd2VpeGluLnNvaHUuY29tfA; pprdig=pzuomrbWX3oWkx3G9VNVk7g6lMVUgG77RxK3xO7XZw7t0uRs0Y1zmKEiNInViih7VaffgyqTo0SA5p6xKL8FsbW0UHgavV5MZFsyZxs0gaP4myFloYwg6ClaVktt4GhAQ84_ZmRsdM_Pl3dEcZrU3PyZxWjuxjeLjyNeMPABCME; sgid=26-39648041-AVzQL3SstqpiaE9mAPPniaXPQ; ppmdig=1557147509000000b0b491b95cb97482ae76d3eb22651866'
        Referer='https://weixin.sogou.com/weixin?oq=&query=%E4%B8%AD%E7%BE%8E%E8%B4%B8%E6%98%93%E6%88%98&_sug_type_=1&sut=0&lkt=0%2C0%2C0&s_from=input&ri=0&_sug_=n&type=2&sst0=1561031760503&page=1&ie=utf8&p=40040108&dp=1&w=01015002&dr=1'
        agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        headers={'Accept': 'application/json, text/javascript, */*; q=0.01',
                 'Accept - Encoding': 'gzip, deflate, br',
                 'Accept - Language': 'zh - CN, zh;q = 0.9',
                 'Connection': 'keep-alive',
                 'Host':'weixin.sogou.com',
                 'Referer':Referer,
                 'Cookie':cookie,
                 'User-Agent':agent,
                 'X-Requested-With': 'XMLHttpRequest'}
        if proxies:
                print('当前使用的代理ip:',proxies['https'],'当前正在获取第'+str(a)+'页')
                try:
                    s=requests.get(url0,proxies=proxies)
                    x=x+1
                    if s.status_code == 200:
                        r = requests.get(url,headers=headers,allow_redirects=False,proxies=proxies,timeout=(3,7))
                        if r.status_code==200:
                            break
                        else:
                            print('遭遇', r.status_code)
                            proxies = get_ip_index()
                            if x==3:
                                print('遭遇', r.status_code, 'cookie被封')
                                cookie_list.pop(0)
                except:
                    print('当前ip无法使用：',proxies['https'])
                    proxies = get_ip_index()
                    x=0
        else:
            print('不使用代理IP开始爬取')
            r = requests.get(url, headers=headers, allow_redirects=False, timeout=(3, 7))
            if r.status_code == 200:
                break
            else:
                print('遭遇', r.status_code,'开始启用代理IP')
                proxies = get_ip_index()
    r.encoding = 'utf-8'
    soup=BeautifulSoup(r.text, 'html.parser')
    # print(soup.prettify())
    tag=soup.find_all(class_='txt-box')
    for tag1 in tag:
        list.append(tag1.a.get('data-share'))
    print('成功获取第'+str(a)+'页')
    print(list)
    return list