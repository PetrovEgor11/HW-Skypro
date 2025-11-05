from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Импорт для явных ожиданий
from selenium.webdriver.support import expected_conditions as EC # Импорт для условий ожидания
from selenium.common.exceptions import TimeoutException # Для обработки исключения по таймауту
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def click_blue_button(driver):
    
    driver.get("http://uitestingplayground.com/dynamicid")
    
    blue_button = ".btn-primary"
    
    serch_blue_button = driver.find_element(By.CSS_SELECTOR, blue_button)
    
    serch_blue_button.click()
    
    sleep(2)
    
    driver.quit()

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

click_blue_button(chrome)
click_blue_button(firefox)