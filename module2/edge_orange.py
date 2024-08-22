from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path = "C:\drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service = service)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(3)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"oxd-button").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"span.oxd-text").click()
time.sleep(10)

#driver.find_element(By.CSS_SELECTOR,"header[class='oxd-topbar'] li:nth-child(1) a:nth-child(1)").click()






