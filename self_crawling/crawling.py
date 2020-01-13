# 크롤링(crawling) 이란?
# Web상에 존재하는 Contents를 수집하는 작업 (프로그래밍으로 자동화 가능)
# 1. HTML 페이지를 가져와서, HTML/CSS 등을 파싱하고, 필요한 데이터만 추출하는 기법
# 2. Open API(Rest API)를 제공하는 서비스에 Open API를 호출해서, 받은 데이터 중 필요한 데이터만 추출하는 기법
# 3. Selenium 등 브라우저를 프로그래밍으로 조작해서, 필요한 데이터만 추출하는 기법

import requests
from bs4 import BeautifulSoup

# BeautifulSoup : HTML의 태그를 파싱해서 필요한 데이터만 추출하는 함수를 제공하는 라이브러리
# 설치 방법 : pip install bs4

# 1) requests 라이브러리를 활용한 HTML 페이지 요청
# 1-1) res 객체에 HTNL 데이터가 저장되고, res.content로 데이터를 추출할 수 있음datetime A combination of a date and a time. Attributes: ()
res = requests.get('https://www.naver.com/')

# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
soup = BeautifulSoup(res.content, 'html.parser') # html.parser : 데이터를 html 관점에서 추출

# 3) 필요한 데이터 검색
title = soup.find('title')

# 4) 필요한 데이터 추출
#(1) 태그로 검색 방법
print(title.get_text())

# find() : 가장 먼저 검색되는 태그 반환
# find_all() : 전체 태그 반환, 관련된 모든 데이터를 리스트 형태로 추출하는 함수

#(2) id로 검색 방법
title_data = soup.find(id='whale_promotion_banner')
print(title_data)

#(3) HTML 태그와 태그에 있는 속성값을 활용해서 필요한 데이터를 추출하는 방법
name = soup.find("div",{"class":"banner_area type_chrome"})
name_detail = name.find("span",{"class":"blind"})
print(name_detail.text)
# .get_text()
# .text
