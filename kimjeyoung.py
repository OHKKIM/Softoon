import requests
from bs4 import BeautifulSoup
from pprint import pprint

html = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week=")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

div_link = soup.find('div', {'class':'list_area daily_img'})
#dl_link = div_link.findAll('dl')
#dl_link = div_link.find('dl')

dt_link = div_link.findAll('dt') #제목
dd_link = div_link.find('dd', {'class':'desc'})
a_link = dd_link.findAll('a') #작가
star = div_link.findAll('strong') #별점

print("제목 :", dt_link[0].text, ", 작가 :", a_link[0].text, ", 별점 :", star[0].text)

#txt = dl_link.findAll('a')
#star = dl_link.find('strong')

#face_list = []
#txt_list = [t.text for t in txt]
#face_list.extend(txt_list)

#print("제목 :", face_list[0], ", 작가 :", face_list[1], ", 별점 :", star.text)