from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="C:\drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://www.iplt20.com/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"POINTS TABLE").click()
time.sleep(3)
#links_team_names=driver.find_elements(By.CSS_SELECTOR,"tr.team0")
links_wins = driver.find_elements(By.XPATH,"//tr[@CLASS = 'team0 ng-scope']/td[12]/div[1]")

#print(len(links_wins))

result = []
for i in links_wins:

#    print(i.text)
    result .append(i.text)
#print("result:" , result)

num = 0
for j in range(len(result)):
    if result[j] == "W\nW\nW\nW\nW":
        num = j
        break

#print(num)

hello_1 = driver.find_elements(By.XPATH,"//tr[@class = 'team0 ng-scope']/td[3]//h2[1]")
print(hello_1[num].text)
