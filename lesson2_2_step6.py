"""
execute_script
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = None
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти элемент
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    # заполнить поле с id="answer"
    input1 = browser.find_element(By.ID, "answer")
    # скроллинг
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    # отметить checkbox "I'm the robot"
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    # скроллинг
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    # выбрать radiobutton "Robots rule!"
    option2 = browser.find_element(By.ID, 'robotsRule')
    # скроллинг
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    # нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # скроллинг
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    if browser:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()
