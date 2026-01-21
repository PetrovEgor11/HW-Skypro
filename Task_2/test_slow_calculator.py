import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages_task_2.Slow_calculator import slow_calculator


def test_task_2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator = slow_calculator(driver)
    calculator.open_service()
    calculator.close_driver()