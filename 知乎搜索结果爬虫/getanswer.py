import requests
import csv
import time
from bs4 import BeautifulSoup
headers={
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '_zap=763f15cf-6e47-4c7a-8a8f-376ae1c73228; _xsrf=Kzy4vblezVql4tlJHkdT3xymZNNVi1s5; d_c0="ADCtoxxcng-PTiIXwNbDSzGKelCV5Q0OjWg=|1561105384"; capsion_ticket="2|1:0|10:1561105384|14:capsion_ticket|44:YWRkNGFiMzMzODQ4NDNjMjkxNzcwNDRlZjcxYjNhZDU=|e35c1387ce220738208e93e301c07ffc8e38ad28457890b747c9d2d2615ebb76"; z_c0="2|1:0|10:1561105440|4:z_c0|92:Mi4xODhadUVBQUFBQUFBTUsyakhGeWVEeVlBQUFCZ0FsVk5JT0w1WFFCWVlpVjFJTG9LbTd5VUh6Z1JuRXNRaDhFT2ZR|57f72862516d37b24928c7f8f00147e2a99802dd485a2a0bf5a2d3a96d56f870"; tst=r; q_c1=bb8f379a7499486b84efb55123fdff9f|1561105441000|1561105441000; __gads=ID=a48be963af0707e1:T=1561105443:S=ALNI_Ma3CDg_sA_QKk7tCqoxGwx-Hii78g; __utma=51854390.711828916.1561105447.1561105447.1561105447.1; __utmb=51854390.0.10.1561105447; __utmc=51854390; __utmz=51854390.1561105447.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20190621=1^3=entry_date=20190621=1; tgw_l7_route=060f637cd101836814f6c53316f73463',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'x-requested-with': 'fetch'
    }
def fenxi(data,f):
    for i in data:
        list = []
        list.append(i['author']['name'])
        list.append(i['author']['type'])
        list.append(i['author']['headline'])
        list.append(i['author']['gender'])
        time1 = i['created_time']
        time_stamp = int(time1)
        time_struct = time.localtime(time_stamp)
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
        list.append(time_str)
        list.append(i['voteup_count'])
        list.append(i['comment_count'])
        soup = BeautifulSoup(i["content"], 'html.parser')
        list.append(soup.text)
        writer = csv.writer(f)
        writer.writerow(list)

def get_answer(url,f):
    while True:
        respond = requests.get(url,headers=headers)
        dict1=respond.json()
        fenxi(dict1['data'],f)
        print(dict1)
        if dict1["paging"]["is_end"] == False:
            url = dict1["paging"]["next"]
        else:
            break
