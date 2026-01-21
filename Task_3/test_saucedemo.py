import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages_task_3.Page_auth import auth
from pages_task_3.Page_add_basket import add_basket
from pages_task_3.Page_basket import page_basket
from pages_task_3.Page_Your_Information import Your_information


def test_task_3():
    #Открытие браузера и прохождении авторизации
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    auth_page = auth(driver)  #Экземпляр класса
    auth_page.open_service(driver)
    auth_page.auth(driver, "standard_user", "secret_sauce")

    #Добавление в корзину
    add_basket_product = add_basket(driver) #Экземпляр класса
    add_basket_product.put_products()

    #Переход в карзину
    page_basket_product = page_basket(driver) #Экземпляр класса
    page_basket_product.open_basket()
 
    #Переход на страницу Your_information
    page_your_information = Your_information(driver) #Экземпляр класса
    page_your_information.page_your_information(driver, "Egor", "Petrov", "Moscow")
    sleep (10)
    page_your_information.result()
    page_your_information.close_driver()
