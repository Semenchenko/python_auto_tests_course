"""
get_attribute
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = None
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти элемент-картинку,
    img_element = browser.find_element(By.ID, 'treasure')
    x = img_element.get_attribute('valuex')
    y = calc(x)

    # заполнить поле с id="answer"
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # отметить checkbox "I'm the robot"
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()

    # выбрать radiobutton "Robots rule!"
    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()

    # нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    if browser:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

"""
from forum

from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()

# Открыть страницу http://suninjuly.github.io/get_attribute.html
browser.get('http://suninjuly.github.io/get_attribute.html')

# Найти на ней элемент-картинку/ Взять у этого элемента значение атрибута valuex
valuex = browser.find_element_by_css_selector('[id = "treasure"]').get_attribute('valuex')

# Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
browser.find_element_by_id('answer').send_keys(str(log(abs(12 * sin(int(valuex))))))

# Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить.
for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
  browser.find_element_by_css_selector(selector).click()
"""