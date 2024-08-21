from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    service = Service(executable_path="C:\drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    return driver
def edge_setup():
    from selenium.webdriver.edge.service import Service
    service = Service(executable_path="C:\drivers\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    service = Service(executable_path="C:\drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
    driver = webdriver.Firefox(service = service)

    return driver

ch = chrome_setup()
ed = edge_setup()
ff = firefox_setup()

browsers = [ch, ed, ff]
for i in browsers:
    driver = i
    driver.implicitly_wait(10)f
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(3)

    obj_username_tf = driver.find_element(By.NAME,"username")
    obj_username_tf.send_keys("Admin")
    time.sleep(1)

    driver.find_element(By.NAME,"password").send_keys("admin123")
    #obj_password_tf.send_keys("admin123")
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR,".oxd-button").click()
    time.sleep(3)

    driver.find_element(By.CLASS_NAME,"oxd-main-menu-item-wrapper").click()
    time.sleep(2)


    driver.find_element(By.CSS_SELECTOR,"header[class='oxd-topbar'] li:nth-child(2) span:nth-child(1)").click()
    time.sleep(2)

    job_title = driver.find_element(By.LINK_TEXT,"Job Titles")
    print(job_title.text)
    driver.quit()