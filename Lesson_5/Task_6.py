from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открытие сайта
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Ждем появления окна рекламы и кнопки закрытия
wait = WebDriverWait(driver, 10)
close_button = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "modal-footer")) # Используйте подходящий класс или ID
)

# Нажатие на кнопку "Закрыть"
close_button.click()

# Задержка на 10 секунд
sleep(10)


