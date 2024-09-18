from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


s = Service(execitable_path="C:\\Users\\DELL\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.iplt20.com/points-table/men/2023")
time.sleep(10)

driver.find_elements(By.XPATH,"//table/tbody/tr")


table_wins = driver.find_elements(By.XPATH, "//tr[@class='team0 ng-scope']/td[12]/div[1]")

result = []


for row in table_wins:
    result.append(row.text)


count = []
for i in range(len(result)):
    if result[i] == "W\nW\nW\nW\nW":
        count.append(i)
if count:
    for j in count:
        wins = driver.find_elements(By.XPATH, "//tr[@class='team0 ng-scope']/td[3]")
        print("This is the team with five consecutive wins:", wins[j].text)
else:
    print("No team with five consecutive wins found.")
driver.quit()



