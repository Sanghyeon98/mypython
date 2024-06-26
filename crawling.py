from bs4 import BeautifulSoup
import urllib.request
import re
import openpyxl
import json

hdr ={'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

# 2. Workbook 생성
wb = openpyxl.Workbook()

# 3. Sheet 활성
sheet = wb.active

# 4. 데이터프레임 내 header(변수명)생성
sheet.append(["제목"])

for n in range(0,10):
    #클리앙의 중고장터 주소
    data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
    req = urllib.request.Request(data, headers = hdr)
    data = urllib.request.urlopen(req).read()
    page = data.decode('utf-8', 'ignore')
    soup = BeautifulSoup(page, 'html.parser')
    list = soup.find_all('span', 
                attrs={'data-role':'list-title-text'})
    
    for item in list:
                try:
                        title = item.text.strip()
                        #print(title) # 클리앙 글 출력
                        if (re.search('아이패드', title)): # 아이패드에 관련된 글만 출력
                                print(title.strip())
                except:
                        pass