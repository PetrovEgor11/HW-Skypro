import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages_task_1.Page_data_types import data_types

def test_task_1():
    # Создаем драйвер и открываем страницу
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Создаем экземпляр класса data_types
    page_data_types = data_types(driver)
    # Вызываем методы без передачи драйвера в аргументах
    page_data_types.open_service()
    page_data_types.data_types()

    page_data_types.color()

    page_data_types.close_driver()

