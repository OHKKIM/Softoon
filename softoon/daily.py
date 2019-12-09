#!/usr/bin/env python3
import time
import sys
import os
import json
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
from bs4 import BeautifulSoup

######
def extract_date(string):
    return string[:10].replace("-", ".")
######

def webtoon_list_crawling(soup):
    tmp_list = []
    daily = soup.find('div', {'class':'list_area daily_img'})
    tit = daily.findAll('div',{'class':'thumb'})

    for t in tit:
        class_title_a_list=t.select('a')

        for a in class_title_a_list:
            a_href=a.get('href')
            result=f'https://comic.naver.com{a_href}'
            tmp_list.append(result) # 웹툰 리스트 저장

    return tmp_list

def comment_crawling(webtoon_list):
    tmp_list = []
    tmp_dict = {}

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/ubuntu/softoon/chromedriver")
    driver.implicitly_wait(5)
    # 웹 페이지 5초 대기
    driver.maximize_window()
    cnt = 0
    for i in range(0,len(webtoon_list)):
        check_age = True
        html = urlopen(webtoon_list[i])
        soup = BeautifulSoup(html, "html.parser")
        try:
            age = soup.find('span', {'class': 'age'}).text # 이용가 find
            if age == "18세 이용가":
                check_age = False # 18세이용가이면 다음영화로하기 위해
        except:
             pass # 브랜드웹툰은 연령이 안뜬다!

        td = soup.find('td', {'class': 'title'})
        newlink = td.select('a')
        for a in newlink:
            href = a.get('href')  # 최신화 링크
        new = f'https://comic.naver.com{href}' # 최신화

        if check_age:
            # url을 list(리스트)에서 detail(회차)로 수
            html = urlopen(webtoon_list[i])
            soup = BeautifulSoup(html, "html.parser")
            thumb = soup.find('div',{'class':'thumb'})
            detail = thumb.select('img')
            for a in detail:
                title = a.get('title')  # 웹툰 제목
                img_src = a.get('src')
            print("웹툰 제목 : "+title+" / "+str(i))

            html = urlopen(new)
            soup = BeautifulSoup(html, "html.parser")
            star = soup.find('span',{'id':'topPointTotalNumber'}).text
            upload_date = soup.find('dd',{'class':'date'}).text # 웹툰 게시한 날짜
            print("웹툰 업로드 : "+upload_date+", 별점 : "+star)
            #print('[\''+title+'\', \''+upload_date+'\']') # 웹툰회차정보 저장

            late_url = new
            # url을 회차에서 댓글페이지로 수정
            new = new.replace('webtoon/detail.nhn?', 'comment/comment.nhn?')

            driver.get(new)
            time.sleep(sleeptime)
            comment_contents = driver.find_elements_by_css_selector('.u_cbox_contents') #댓글
            comment_likes = driver.find_elements_by_css_selector('.u_cbox_cnt_recomm') #좋아요
            comment_hates = driver.find_elements_by_css_selector('.u_cbox_cnt_unrecomm') #싫어요

            for m in range(0, len(comment_contents)):
                #print('[\'' + comment_contents[m].text + '\', \''+ comment_likes[m].text + '\', \'' + comment_hates[m].text + '\']')
                #tmp_list.append([str(i), title, upload_date, str(m), comment_contents[m].text, comment_likes[m].text, comment_hates[m].text])
                cnt += 1
                tmp_dict[str(cnt)] = {'title':title, 'upload':upload_date, 'star':star, 'content':comment_contents[m].text,
                                'like':comment_likes[m].text, 'hate':comment_hates[m].text, 'url':late_url, 'img':img_src}
                #댓글,좋아요,싫어요 저장

            time.sleep(sleeptime)
            # url을 댓글에서 회차페이지로 수정
            new = new.replace('comment/comment.nhn?', 'webtoon/detail.nhn?')
        #
    #
    return tmp_list, tmp_dict
    driver.quit()
#==================================================================End Crawling()====================================================================#
def toJson(comment_dict):
    with open('comment.json', 'w', encoding='utf-8') as file:
        json.dump(comment_dict, file, ensure_ascii=False, indent='\t')
#===================================================================End toFile()=====================================================================#
sleeptime = 0.5

html = urlopen("https://comic.naver.com/webtoon/weekdayList.nhn?week=")
soup = BeautifulSoup(html, "html.parser")

def Idle():
    timer = threading.Timer(240, Idle) #4분 마다 크롤링
    
    webtoon_list = []
    comment_list = []
    comment_dict = {}
    webtoon_list = webtoon_list_crawling(soup)
    temp = comment_crawling(webtoon_list)
    comment_list = temp[0]
    comment_dict = dict(comment_dict, **temp[1])

    #for list in comment_list:
    #    print(list)

    #for dict in comment_dict:
    #    print(dict, comment_dict[dict]['title'], comment_dict[dict]['upload'],
    #          comment_dict[dict]['content'], comment_dict[dict]['like'], comment_dict[dict]['hate'])

    toJson(comment_dict)
    timer.start()

Idle()
