from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Открыть сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#Присвоили локутору "Add_Element" переменную
Add_Element_locator = 'button'

#Поиск локатора "Add_Element" на сайте
serch_Add_Element_locator = driver.find_element(By.CSS_SELECTOR, Add_Element_locator)

#5 раз кликнуть на кнопку "Add Element"
for x in range(5):
    serch_Add_Element_locator.click()

#Присволи локатору "Delete" переменную
delete_locator = '.added-manually'

#Поиск локатора "Delete" на сайте
delete_buttons = driver.find_elements(By.CSS_SELECTOR, delete_locator)

#Вывод размера списка 
print (len(delete_buttons))

#Задержка на 10 сек
sleep(10)