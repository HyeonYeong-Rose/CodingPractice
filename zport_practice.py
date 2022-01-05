from selenium import webdriver
#크롭웹드라이버 다운로드하고 경로 복붙행 근데 역슬래쉬 두개씩!
driver = webdriver.Chrome('C:\\Users\\Seo\\Downloads\\chromedriver_win32\\chromedriver')
#이건 슥삭 url준거
driver.get('http://admin.ssgsag.kr/posters/9922')
#힘들수도 있으니까 2초 쉬게 한거야 여러개 할때 너무빠르면 가끔 멈춰
driver.implicitly_wait(time_to_wait=2)
#요소 우클릭해서 copyXpath해서 넣었어
#get_property라는 함수로 property안에있는 것중에 뭐가져올지 고른거야
element1 = driver.find_element_by_xpath('//*[@id="input-47"]').get_property('_value')
#드라이버 다쓰고 닫으라길래 넣었어 구글이 그랬고등
driver.quit()
#결과값 짜잔
print(element1)

