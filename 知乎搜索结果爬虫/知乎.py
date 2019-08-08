import requests
import json
import time
from bs4 import BeautifulSoup
headers={
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '_zap=763f15cf-6e47-4c7a-8a8f-376ae1c73228; _xsrf=Kzy4vblezVql4tlJHkdT3xymZNNVi1s5; d_c0="ADCtoxxcng-PTiIXwNbDSzGKelCV5Q0OjWg=|1561105384"; capsion_ticket="2|1:0|10:1561105384|14:capsion_ticket|44:YWRkNGFiMzMzODQ4NDNjMjkxNzcwNDRlZjcxYjNhZDU=|e35c1387ce220738208e93e301c07ffc8e38ad28457890b747c9d2d2615ebb76"; z_c0="2|1:0|10:1561105440|4:z_c0|92:Mi4xODhadUVBQUFBQUFBTUsyakhGeWVEeVlBQUFCZ0FsVk5JT0w1WFFCWVlpVjFJTG9LbTd5VUh6Z1JuRXNRaDhFT2ZR|57f72862516d37b24928c7f8f00147e2a99802dd485a2a0bf5a2d3a96d56f870"; tst=r; q_c1=bb8f379a7499486b84efb55123fdff9f|1561105441000|1561105441000; __gads=ID=a48be963af0707e1:T=1561105443:S=ALNI_Ma3CDg_sA_QKk7tCqoxGwx-Hii78g; __utma=51854390.711828916.1561105447.1561105447.1561105447.1; __utmb=51854390.0.10.1561105447; __utmc=51854390; __utmz=51854390.1561105447.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20190621=1^3=entry_date=20190621=1; tgw_l7_route=060f637cd101836814f6c53316f73463',
    'referer': 'https://www.zhihu.com/topic/20177825/hot',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'x-ab-param': 'top_hotcommerce=1;top_recall_exp_v2=10;se_limit=0;se_timebox_num=3;se_payconsult_click=0;se_pyc_click2=1;tp_header_style=1;ug_follow_answerer=0;li_auif_ab=0;li_mceb=1;se_college_cm=1;se_km_ad_locate=1;zr_album_chapter_exp=0;zr_es_update=0;zr_km_slot_style=event_card;se_site_onebox=0;zr_album_exp=0;se_agency= 0;se_waterfall=0;se_zu_recommend=0;se_topicdirect=2;se_whitelist=1;top_gr_ab=6;top_rank=9;li_ebook_detail=2;ls_new_upload=0;pf_foltopic_usernum=50;se_mobileweb=0;tp_sft_v2= a;ug_goodcomment=0;li_price_test=3;pf_creator_card=1;se_likebutton=0;se_ltr_v002=1;tsp_childbillboard=2;se_famous=1;se_webtimebox=1;top_root=0;top_v_album=1;se_terminate=0;li_tjys_ec_ab=0;se_ltr_v008=0;se_pay_score=0;se_p_slideshow=0;tp_sticky_android=2;ug_follow_topic_1=2;li_album_liutongab=0;pf_feed=1;se_ad_index=10;se_ri=0;zr_video_recall=current_recall;li_qa_new_cover=0;se_auto_syn=0;tp_qa_metacard=1;ug_follow_answerer_0=0;tp_meta_card=0;tp_qa_toast=1;ug_fw_answ_aut_1=0;se_featured=1;se_topic_express=0;se_webmajorob=0;top_ydyq=A;tp_sft=a;li_se_ebook_chapter=1;se_college=default;se_ios_spb309=1;se_lottery=0;top_new_feed=5;top_universalebook=1;zr_infinity_xgb=close;li_ts_sample=old;se_colorfultab=0;se_time_threshold=0;se_webrs=1;soc_special=0;top_test_4_liguangyi=1;ls_videoad=0;pf_newguide_vertical=0;se_page_limit_20=1;se_topic_pu=0;li_album3_ab=0;se_websearch=3;top_quality=0;top_recall_deep_user=1;tp_time_information=1;tp_top_sticky=1;zr_se_footer=1;se_amovietab=1;se_billboardsearch=0;se_zu_onebox=0;soc_bignew=1;pf_noti_entry_num=0;se_backsearch=1;soc_update=1;tsp_hotctr=1;zr_ans_rec=gbrank;zr_km_xgb_model=old;top_ebook=0;top_recall_exp_v1=9;tp_qa_metacard_top=top;se_expired_ob=0;tp_m_intro_re_topic=1;ug_goodcomment_0=1;se_title_only=0;se_wannasearch=0;zr_art_rec=base;zr_km_style=mixed;li_filter_ttl=2;se_rr=1;se_time_score=1;zr_ebook_chapter=1;pf_fuceng=1;se_new_topic=0;se_spb309=0;tp_discussion_feed_type_android=2;li_qa_cover=old;se_preset_tech=0;ug_newtag=0;li_lt_tp_score=1;ls_fmp4=0;se_subtext=0;qa_test=0;top_native_answer=4;tsp_lastread=0;se_hot_query=0;se_search_feed=N;top_vipconsume=2;se_movietab=1;top_user_cluster=0;li_hot_score_ab=0;qa_answerlist_ad=0;soc_bigone=1;top_reason=1;zr_km_answer=open_cvr;zr_rel_search=base;se_payconsult=5;ug_zero_follow=0;ug_zero_follow_0=0',
    'x-requested-with': 'fetch'
}
a=1
url='https://www.zhihu.com/api/v4/topics/20177825/feeds/top_activity?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=5&after_id=5521.74984'
def fenxi(list,f,super):
    for dict in list:
        try:
            text={}
            text['title']=dict["target"]["title"]
            time1=dict["target"]["created"]
            time_stamp = int(time1)
            time_struct = time.localtime(time_stamp)
            time_str = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
            text['time'] = time_str
            text['author']=dict["target"]["author"]["name"]
            text['gender'] = dict["target"]["author"]["gender"]
            soup = BeautifulSoup(dict["target"]["content"], 'html.parser')
            text['content']=soup.text
            text['vote']=dict["target"]["voteup_count"]
            super.append(text)
        except:
            None
            # text = {}
            # text['title'] = dict["target"]["question"]["title"]
            # time1 = dict["target"]["created_time"]
            # time_stamp = int(time1)
            # time_struct = time.localtime(time_stamp)
            # time_str = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)
            # text['time'] = time_str
            # text['author'] = dict["target"]["author"]["name"]
            # text['gender'] = dict["target"]["author"]["gender"]
            # soup = BeautifulSoup(dict["target"]["content"], 'html.parser')
            # text['content'] = soup.text
            # text['vote'] = dict["target"]["comment_count"]
            # super.append(text)

super=[]
with open('知乎文章.json', 'a', encoding='utf-8') as f:
    while True:
        respond = requests.get(url,headers=headers)
        dict1=respond.json()
        print(a)
        fenxi(dict1["data"],f,super)
        if dict1["paging"]["is_end"]==False:
            url=dict1["paging"]["next"]
            a=a+1
        else:
            break
    json.dump(super,f,indent=4,ensure_ascii=False)