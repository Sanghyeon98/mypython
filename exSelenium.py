from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver 경로 설정
driver = webdriver.Chrome(executable_path='YOUR_CHROMEDRIVER_PATH')

# 네이버 쇼핑 아이패드 검색 결과 페이지로 이동
driver.get("https://search.shopping.naver.com/search/all?query=아이패드")

# 페이지 로딩 대기
time.sleep(2)

# 상품 정보를 담을 리스트
products = []

# 상품 목록을 찾고, 각 상품 정보를 추출
items = driver.find_elements(By.CSS_SELECTOR, 'li.basicList_item__2XT81')
for item in items:
    title = item.find_element(By.CSS_SELECTOR, 'div.basicList_title__3P9Q7 > a').text
    link = item.find_element(By.CSS_SELECTOR, 'div.basicList_title__3P9Q7 > a').get_attribute('href')
    image = item.find_element(By.CSS_SELECTOR, 'div.basicList_img_area__a3NRA > a > img').get_attribute('src')
    seller = item.find_element(By.CSS_SELECTOR, 'div.basicList_mall_title__3MWFY > a').text

    products.append({
        'title': title,
        'link': link,
        'image': image,
        'seller': seller
    })

# 결과 출력
for product in products:
    print(product)

# WebDriver 종료
driver.quit()
