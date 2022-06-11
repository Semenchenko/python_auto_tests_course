"""
капча для роботов
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = None
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считать значение для переменной x
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    # заполнить поле с id="answer"
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # отметить checkbox "I'm the robot"
    option1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    option1.click()

    # выбрать radiobutton "Robots rule!"
    option2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
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
browser.get("http://suninjuly.github.io/math.html")

x = browser.find_element_by_css_selector('[id = "input_value"]').text
browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))

for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
    browser.find_element_by_css_selector(selector).click()
"""