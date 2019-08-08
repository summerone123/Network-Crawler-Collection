from pyquery import PyQuery as pq
import requests
import time
import re
import pymongo

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, sdch, br',
    'cookie': '_T_WM=48471767489; ALF=1563715720; SCF=AijEvzIXGeu1jnCQ0KPxP2m2eH09-GvBRTN-veHdpEm8rdWNLiAmisP8IZG9yiBCFcXemw5y4ya68w1hK7aQKC0.; SUB=_2A25wCKwPDeRhGeNI6FAR8i_Izj-IHXVT8jRHrDV6PUJbktAKLVfmkW1NSJYh7I4lNCX-u_PIs24eYM_MMvf8Rv31; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW9J4lZkz4Joa3MLIhmgEVT5JpX5K-hUgL.Fo-ce0z7eo2XSKe2dJLoIXeLxKqL1KnLB-qLxK-L12qL1K2LxK-L12qL12BLxK-L1h5L1KzLxKqL1KnLB-qLxK-L12qL1K2LxK-L122LBKykeK-c; SUHB=0k1CUzVPxf6xpI; SSOLoginState=1561123935',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}

client = pymongo.MongoClient(r'mongodb://localhost:27017/')
db = client['weibo']
collection = db['trade3']
# 添加page数（92）
base_url = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%E4%B8%AD%E7%BE%8E%E8%B4%B8%E6%98%93%E6%88%98&advancedfilter=1&starttime=20180101&endtime=20180102&sort=time&page='


# list_time = ['0513', '0514', '0515', '0516', '0517', '0518', '0519', '0520', '0521', '0522', '0523', '0524', '0525',
#              '0526', '0527', '0528', '0529', '2530', '0531', '0601', '0602', '0603', '0604', '0605', '0606', '0607',
#              '0608', '0609', '0610', '0611', '0612', '0613', '0614', '0615', '0616', '0617', '0618', '0619']


def get_text():
    num = 22947
    for i in range(1, 1000000):
        url = base_url + str(i)
        while True:
            try:
                html = requests.get(url, headers=headers)
                doc = pq(html.content, parser='html')
                if '新浪通行证' in doc:
                    print('通行证', i, url)
                break
            except:
                print('wrong ', html.content)
                time.sleep(3)
                None
        list_c = list(doc('body div.c[id]').items())
        if len(list_c) == 0:
            print(doc)
            print(i, url)
            print('break')
            break
        for c in list_c:
            item = {}
            # if len( list(c('div').items()) )>=3:
            # content = c('span.ctt').text()
            # print( len( list(c('div').items()) ) , content)
            # else:
            #     content = c.text()
            #     print( content )
            content = c('span.ctt').text()
            try:
                inf = re.findall('赞\[(.*?)\].*转发\[(.*?)\].*评论\[(.*?)\].*收藏 (.*?) 来自', c.text())[0]
            except:
                inf = re.findall('赞\[(.*?)\].*转发\[(.*?)\].*评论\[(.*?)\].*收藏 (.*)', c.text())[0]
            item['zan'] = inf[0]
            item['zhuanfa'] = inf[1]
            item['pinglun'] = inf[2]
            item['time'] = inf[3]
            item['content'] = content
            item['_id'] = str(inf)
            if collection.find_one({'_id': str(inf)}) == None:
                collection.insert(item)
                num += 1
                print(item)
            with open('C:/Users/l/Desktop/中美2018/' + str(num) + '.txt', 'w', encoding='utf-8') as f:
                f.write(str(item))


get_text()
