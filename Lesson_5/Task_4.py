from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Импорт для явных ожиданий
from selenium.webdriver.support import expected_conditions as EC # Импорт для условий ожидания
from selenium.common.exceptions import TimeoutException # Для обработки исключения по таймауту

def script():
    """
    Функция выполняет следующие действия:
    1. Инициализирует Chrome WebDriver.
    2. Открывает страницу http://uitestingplayground.com/dynamicid.
    3. Использует явное ожидание для поиска и клика по "синей кнопке".
    4. Закрывает браузер.
    """
    driver = None # Инициализируем driver как None для безопасного использования в блоке finally
    try:
        print(" -> Инициализация WebDriver...")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window() # Максимизируем окно для лучшей видимости и надежности

        print(" -> Открытие страницы: http://uitestingplayground.com/dynamicid")
        driver.get("http://uitestingplayground.com/dynamicid")
        
        # Локатор для "синей кнопки"
        Blue_button_locator = '.btn.btn-primary'
        
        print(f" -> Ожидание элемента по CSS-селектору: '{Blue_button_locator}'")
        # Используем явное ожидание, чтобы дождаться, пока кнопка станет кликабельной
        wait = WebDriverWait(driver, 10) # Максимальное время ожидания 10 секунд
        serch_Blue_button_locator = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Blue_button_locator))
        )
        
        print(" -> Элемент найден. Клик по 'синей кнопке'.")
        serch_Blue_button_locator.click()
        print(" -> Кнопка 'Blue button' успешно нажата.")

        # Добавим небольшую паузу, чтобы вы могли визуально убедиться в клике, перед закрытием браузера
        sleep(2) 

    except TimeoutException:
        print(f" !!! ОШИБКА: Элемент '{Blue_button_locator}' не был найден на странице в течение заданного времени ожидания (10 секунд).")
    except Exception as e:
        print(f" !!! ПРОИЗОШЛА НЕПРЕДВИДЕННАЯ ОШИБКА: {e}")
    finally:
        if driver: # Убеждаемся, что драйвер был успешно инициализирован
            print(" -> Закрытие браузера.")
            driver.quit() # Гарантированно закрываем браузер

# Запуск скрипта 3 раза подряд
for n in range(3):
    print(f"\n--- Запуск скрипта №{n+1} из 3 ---")
    script()
    print(f"--- Завершение скрипта №{n+1} ---")
    if n < 2: # Добавим небольшую паузу между запусками для лучшей изоляции и читаемости логов
        sleep(1)




