# "Softoon - 오늘의 HOT한 웹툰!"

###### http://18.213.183.104/softoon.php

# 1. 프로젝트 주제
<div>
"길가면서, 밥먹으면서, 자기전, 수업시간에도 웹툰을 보는 시대!"<br/>
오늘의 웹툰 중 별점이 높은 6개의 웹툰과 좋아요♥ & 싫어요♡를 가장 많이 받은 댓글과 해당 웹툰을 소개한다.
</div>
# 2. 크롤링 사이트
<div>
<img src=https://user-images.githubusercontent.com/31759437/70472173-ffe7d980-1b11-11ea-8915-5ad5b1580c6d.png width=100 height=100>
월간 사용자가 3,500만명이 넘는 네이버웹툰을 크롤링하여 핫한 웹툰을 소개
</div>

# 3. 환경
+ Ubuntu
+ Python
+ Json
+ PHP

# 4. 설정 (root로 편리하게)
+ ubuntu에서의 설정
  + apt 업데이트
    + apt update / apt-get update
  + Python3 설치
    + apt-get install python3
  + pip3 설치
    + apt-get install python3-pip
  + import(Python) pip3
    + pip3 install bs4
    + pip3 install selenium
    + pip3 install requests
    + pip3 install urllib
    + pip install json
  + PHP 설치
    + apt install php-cli
  + Apache2 설치
    + apt install apache2
  + Chrome 설치
    + apt install python3-selenium
    + wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    + sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" /etc/apt/sources.list.d/google.list'
    + sudo apt-get update
    + sudo apt-get install google-chrome-stable
  + Chrome-driver 설치
    + unzip chromedriver_linux64.zip
  + PHP, Apache2 연동
    + /etc/apache2/apache2.conf
      + Directory /var/www/>
        ===> <Directory /ㅁ/ㅁ/> = softoon.php가 있는 경로
    + /etc/apache2/sites-availalbe/000-default.conf
      + DocumentRoot /var/www/
        ===> ServerName 도메인주소 ServerAlias 도메인주소 DocumentRoot /ㅁ/ㅁ/ = softoon.php가 있는 경로
    + service apache2 restart
    
+ Python에서의 설정
  + daily.py안에서 Chrome driver가 있는 경로 지정
    + driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="경로/chromedriver")
  + Run daily.py
    + Run하게 되면 종료 시까지 4분마다 자동으로 크롤링

