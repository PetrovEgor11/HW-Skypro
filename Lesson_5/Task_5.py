from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def script_task5():
    """
    Функция выполняет следующие действия для Задания 5:
    1. Инициализирует Chrome WebDriver.
    2. Открывает страницу http://uitestingplayground.com/classattr.
    3. Использует явное ожидание для поиска и клика по "синей кнопке" (Primary Button).
    4. Закрывает браузер.
    """
    driver = None # Инициализируем driver как None для безопасного использования в блоке finally
    try:
        print(" -> Инициализация WebDriver...")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window() # Максимизируем окно для лучшей видимости и надежности

        target_url = "http://uitestingplayground.com/classattr"
        print(f" -> Открытие страницы: {target_url}")
        driver.get(target_url)
        
        # Локатор для "синей кнопки" (Primary Button)
        # На странице http://uitestingplayground.com/classattr синяя кнопка имеет класс "btn btn-primary"
        blue_button_locator = '.btn.btn-primary'
        
        print(f" -> Ожидание элемента по CSS-селектору: '{blue_button_locator}'")
        # Используем явное ожидание, чтобы дождаться, пока кнопка станет кликабельной.
        # Это обеспечивает, что скрипт будет ждать, пока элемент появится и будет готов к взаимодействию.
        wait = WebDriverWait(driver, 10) # Максимальное время ожидания 10 секунд
        primary_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, blue_button_locator))
        )
        
        print(" -> Элемент 'Primary Button' найден. Клик по кнопке.")
        primary_button.click()
        print(" -> Кнопка 'Primary Button' успешно нажата.")

        # Добавим небольшую паузу, чтобы вы могли визуально убедиться в клике, перед закрытием браузера
        sleep(2) 

    except TimeoutException:
        print(f" !!! ОШИБКА: Элемент '{blue_button_locator}' не был найден на странице в течение заданного времени ожидания (10 секунд).")
    except NoSuchElementException:
        print(f" !!! ОШИБКА: Элемент '{blue_button_locator}' не найден в DOM.")
    except Exception as e:
        print(f" !!! ПРОИЗОШЛА НЕПРЕДВИДЕННАЯ ОШИБКА: {e}")
    finally:
        if driver: # Убеждаемся, что драйвер был успешно инициализирован
            print(" -> Закрытие браузера.")
            driver.quit() # Гарантированно закрываем браузер

# Запуск скрипта 3 раза подряд
num_runs = 3
for n in range(num_runs):
    print(f"\n--- Запуск скрипта Задания {n+1} из {num_runs} ---")
    script_task5()
    print(f"--- Завершение скрипта Задания {n+1} ---")
    if n < num_runs - 1: # Добавим небольшую паузу между запусками для лучшей изоляции и читаемости логов
        sleep(1)

