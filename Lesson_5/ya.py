from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")

#driver.get("https://vkvideo.ru")

# for x in range (1,10):
#     driver.back() #воврат назад
#     driver.forward() #переход вперед

# driver.set_window_size(640,460) #установить разрешение экрана

#driver.fullscreen_window #во весь экран

driver.save_screenshot('./ya.png')


sleep(10)





