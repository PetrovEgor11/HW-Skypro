from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



def click_button_close(driver):
    button_close = '.modal-footer'
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    serch_button_close = driver.find_element(By.CSS_SELECTOR, button_close)
    sleep(3)
    serch_button_close.click()
    driver.quit()


chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

print("началось выполнение скрипта")
click_button_close(chrome)
click_button_close(firefox)
print("закончилось выполнение скрипта")















