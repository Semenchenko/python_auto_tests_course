"""
загрузка файла
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = None
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполнить поле с name="firstname"
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('12')

    # заполнить поле с name="lastname"
    input1 = browser.find_element(By.NAME, "lastname")
    input1.send_keys('23')

    # заполнить поле с name="email"
    input1 = browser.find_element(By.NAME, "email")
    input1.send_keys('34')

    # определить кнопку для загрузки файла
    element = browser.find_element(By.ID, 'file')

    # загрузить файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '45.txt')
    element.send_keys(file_path)

    # нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    if browser:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()
