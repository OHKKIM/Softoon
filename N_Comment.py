import time
import sys
import os
import openpyxl #엑셀
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup

######
def extract_date(string):
    return string[:10].replace("-", ".")
######
# headless option
#option = webdriver.ChromeOptions()
#option.add_argument('headless')
#option.add_argument('window-size=1920x1080')
#option.add_argument("disable-gpu")
#

driver = webdriver.Chrome("C:/Users/JeYoung/Downloads/chromedriver.exe")  # , chrome_options=option)
driver.implicitly_wait(5)
# 웹 페이지 5초 대기
sleeptime = 0.5
html = urlopen("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html, "html.parser")
class_title_a_list=soup.select('a.title')
webtoon_list = []

for a in class_title_a_list:
    a_href=a.get('href')
    result=f'https://comic.naver.com{a_href}'
    webtoon_list.append(result) # 웹툰 리스트 저장

for i in range(0,len(webtoon_list)-1):
    check_age = True
    html = urlopen(webtoon_list[i])
    soup = BeautifulSoup(html, "html.parser")
    age = soup.find('span', {'class': 'age'}).text # 이용가 find
    if age == "18세 이용가":
        check_age = False # 18세이용가이면 pass하기 위해

    if check_age:
        # url을 list(리스트)에서 detail(회차)로 수정
        webtoon_list[i] = webtoon_list[i].replace('list', 'detail')
        html = urlopen(webtoon_list[i] + "&no=1")
        soup = BeautifulSoup(html, "html.parser")
        thumb = soup.find('div',{'class':'thumb'})
        detail = thumb.select('img')
        for a in detail:
            title = a.get('title') #웹툰 제목
        remote = soup.find('div',{'class':'pg_area'})
        last = remote.find('span',{'class':'total'}).text #웹툰 마지막회차
        print("웹툰 제목 : "+title+" / "+str(i))

        # 수시로 저장하기 위해 기존 엑셀파일을 불러옴
        sheet = 'sheet' + str({i+1})
        wb = openpyxl.load_workbook('comment.xlsx')
        sheet = wb.create_sheet(title)

        start = int(last)-9 # 최신화 10개
        end = int(last)+1
        if start < 1 : start = 1 # 신작은 10개보다 적을 수 있기에 첫화부터

        for no in range(start, end): # 최신화 10개의 댓글 크롤링
            html = urlopen(webtoon_list[i]  + "&no=" + str(no))
            soup = BeautifulSoup(html, "html.parser")
            upload_date = soup.find('dd',{'class':'date'}).text # 웹툰 게시한 날짜
            print("웹툰 업로드 : "+upload_date)
            sheet.append([title, str(no)]) # 웹툰회차정보 저장

            # url을 회차에서 댓글페이지로 수정
            webtoon_list[i] = webtoon_list[i].replace('webtoon/detail.nhn?', 'comment/comment.nhn?')

            driver.get(webtoon_list[i] + "&no=" + str(no))
            time.sleep(sleeptime)
            comment_contents = driver.find_elements_by_css_selector('.u_cbox_contents') #댓글
            comment_likes = driver.find_elements_by_css_selector('.u_cbox_cnt_recomm') #좋아요
            comment_hates = driver.find_elements_by_css_selector('.u_cbox_cnt_unrecomm') #싫어요

            for m in range(0, len(comment_contents)-1):
                sheet.append([comment_contents[m].text, comment_likes[m].text, comment_hates[m].text])
                #댓글,좋아요,싫어요 저장

            time.sleep(sleeptime)
            # url을 댓글에서 회차페이지로 수정
            webtoon_list[i] = webtoon_list[i].replace('comment/comment.nhn?', 'webtoon/detail.nhn?')
        #
        wb.save('comment.xlsx')
        print("저장 완료")
    #
#
driver.quit()