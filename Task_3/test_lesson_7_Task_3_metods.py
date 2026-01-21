import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = None

# webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
def open_service(driver):
    driver.get("https://www.saucedemo.com/")

#Авторизация
def auth (driver, user, password):
    user_name = driver.find_element(By.CSS_SELECTOR, "[id=user-name]").send_keys(user)
    password = driver.find_element(By.CSS_SELECTOR, "[id=password]").send_keys(password)
    button_login = driver.find_element(By.CSS_SELECTOR, "[id=login-button]").click()

#Добавление товаров в корзину
def put_products (driver):
    sauce_labs_backpack = driver.find_element(By.CSS_SELECTOR, "[id=add-to-cart-sauce-labs-backpack]").click()
    sauce_labs_bolt = driver.find_element(By.CSS_SELECTOR, "[id=add-to-cart-sauce-labs-bolt-t-shirt]").click()
    sauce_labs_onesie = driver.find_element(By.CSS_SELECTOR, "[id=add-to-cart-sauce-labs-onesie]").click()

#Переход в корзину
def open_basket (driver):
    basket = driver.find_element(By.CSS_SELECTOR, "[data-test=shopping-cart-link]").click()
    #Нажатие на кнопку Сheckout
    checkout = driver.find_element(By.CSS_SELECTOR, "[id=checkout]").click()

#Заполнение формы Your Information
def page_your_information(driver, first_name, last_name, address):
    first_name = driver.find_element(By.CSS_SELECTOR, "[id=first-name]").send_keys(first_name)
    last_name = driver.find_element(By.CSS_SELECTOR, "[id=last-name]").send_keys(last_name)
    postal_code = driver.find_element(By.CSS_SELECTOR, "[id=postal-code]").send_keys(address)
    button_continue = driver.find_element(By.CSS_SELECTOR, "[id=continue]").click()

#Проверка 
def result (driver):
    total = driver.find_element(By.CSS_SELECTOR, "[data-test=total-label]").text   
    print(total)      
    clean_total = total.replace('$', '')
    assert total == "Total: $58.29"

def close_driver(driver):
    driver.quit()


def test_task_3():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    open_service(driver)
    auth(driver, "standard_user", "secret_sauce")
    sleep(10)
    put_products(driver)
    open_basket(driver)
    page_your_information(driver, "Egor", "Petrov", "Moscow")
    result(driver)
    close_driver(driver)

test_task_3()