from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="C:\drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.iplt20.com/")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"POINTS TABLE").click()
links_wins = driver.find_elements(By.XPATH,"//tr[@CLASS = 'team0 ng-scope']/td[12]/div[1]")

"""this for loop is to append the match results in he form of list"""
result = []
for i in links_wins:
    result.append(i.text)

"""collect numbers of 5 consecutive wins"""
count = []
for j in range(len(result)):
    if result[j] == "W\nW\nW\nW\nW":
        count.append(j)

""" this for loop is for to print the final result """
for num in count:
    hello_1 = driver.find_elements(By.XPATH,"//tr[@class = 'team0 ng-scope']/td[3]//h2[1]")
    print("This is the Team Five Consecutive wins:",hello_1[num].text)
