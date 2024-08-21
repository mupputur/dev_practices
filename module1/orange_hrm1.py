from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time






def setup_driver(browser='chrome'):
    if browser.lower() == 'chrome':
        service = Service(execitable_path="C:\\Users\\DELL\\Downloads\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    elif browser.lower() == 'firefox':
        service = Service(execitable_path="C:\\Users\\DELL\\Downloads\\geckodriver-v0.35.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)
    elif browser.lower() == 'edge':
        service = Service(execitable_path="C:\\Users\\DELL\\Downloads\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError("Unsupported browsers!")
    driver.implicitly_wait(5)
    return driver
def login_to_orangehrm(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    driver.maximize_window()

    username_tf = driver.find_element(By.NAME, "username")
    username_tf.send_keys("Admin")
    time.sleep(5)

    password_tf = driver.find_element(By.NAME, "password")
    password_tf.send_keys("admin123")
    time.sleep(5)

    login_button = driver.find_element(By.CSS_SELECTOR, ".oxd-button")
    login_button.click()
    time.sleep(5)

    admin_menu_tf = driver.find_element(By.CSS_SELECTOR, 'li.oxd-main-menu-item-wrapper:nth-child(1) > a:nth-child(1) > span:nth-child(2)')
    admin_menu_tf.click()
    time.sleep(5)

    job_menu = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
    job_menu.click()
    time.sleep(5)

    job_titles = driver.find_element(By.CSS_SELECTOR, '.oxd-dropdown-menu > li:nth-child(1) > a:nth-child(1)')
    print(job_titles.text)

    time.sleep(5)

def run_test(browser):
    driver=setup_driver(browser)
    login_to_orangehrm(driver)



for browser in ['chrome','firefox','edge']:
    print(f"Testing on {browser}...")
    run_test(browser)




