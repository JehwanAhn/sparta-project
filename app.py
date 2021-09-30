import requests

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://www.youtube.com/channel/UCtwxuughKbSAV0e4bnz4ORg/videos',headers=headers)
# #
# soup = BeautifulSoup(data.text, 'html.parser')
# # 코딩 시작

driver = webdriver.Chrome()
url = 'https://www.youtube.com/channel/UC3DNe5b3NYZ5ojre8YE1_xw/videos'
driver.get(url)
page=driver.page_source

movies=driver.find_elements_by_id("details") # 영화 내용 및 조회수


# for movie in movies:
#     print(movie.text)


for i in range(len(movies)): # 타이틀 리스트 만듬 계속 조회수랑 업데이트 딸려옴 ㅠㅠ -> 알고보니 같은 인덱스에 전부 포함. 각각 크롤링 해야할 듯...타이틀, 조회수, 업데이트 날짜...
    title = []
    title.append(movies[i].text)
    print(i,title)

play_time=driver.find_elements_by_id("text") # 재생 시간 근데 리스트 값에 공란 존재함 어떻게 공란은 제거하는지
# for time in play_time:
#     if time is not None:
#         print(time.text)


# for i in range(len(play_time)): #재생 시간 리스트 만듬 [''] 제거 예정. 반복문 돌려야 하나?
#     video_time=[]
#
#     video_time.append(play_time[i].text)
#
#     print(i, video_time)
#



# for i in range(len(play_time)): #재생 시간 리스트 만듬 [''] 제거 예정. 반복문 돌려야 하나? remove 함수 사용???
#     video_time=[]
#
#     video_time.append(play_time[i].text)
#
# while '['']' in video_time:
#     video_time.remove('['']')



# hong_contents=driver.find_elements_by_id("contents") # 영화 제목 조회수 및 재생 시간...근데 전부 하나에
# for content in hong_contents:
#     print(content.text)










