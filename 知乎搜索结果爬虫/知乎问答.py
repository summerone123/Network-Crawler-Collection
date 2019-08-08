import json
import os
from getanswer import get_answer
import csv
import re
rootdir='.\\json\\'
files = os.listdir(rootdir)
question={}
for i in files:
    with open(rootdir+i,'r',encoding='utf-8-sig') as f:
        dict = json.load(f)
        for j in dict['data']:
            try:
                title=j['target']['question']['title']
                question[j['target']['question']['id']]=re.sub(r'[\\/:*?"<>|]', '', title)
            except:
                None
for i in question.keys():
    url='https://www.zhihu.com/api/v4/questions/' + str(
        i) + '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=0&platform=desktop&sort_by=default'
    with open('.\\csv\\'+question[i]+'.csv', 'w', encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'type', 'headline', 'gender', 'created_time', 'vote', 'comment', 'content'])
        get_answer(url,f)
    print(i)