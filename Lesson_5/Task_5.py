from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



def click_blue_button(driver):
    driver.get("http://uitestingplayground.com/classattr")
    sleep(3)
    bleu_button = 'button.btn-primary'
    serch_blue_button = driver.find_element(By.CSS_SELECTOR, bleu_button)
    serch_blue_button.click()
    sleep(3)
    driver.quit()

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
print("началась первая итерация")
click_blue_button(chrome)
click_blue_button(firefox)
print("закончисла первая итерация")

print("началась вторая итерация")
click_blue_button(chrome)
click_blue_button(firefox)
print("закончислась вторая итерация")

print("началась третья итерация")
click_blue_button(chrome)
click_blue_button(firefox)
print("закончилась третья итерация")