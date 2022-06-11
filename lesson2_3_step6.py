"""
переход на новую вкладку
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(n):
    return str(math.log(abs(12 * math.sin(int(n)))))


browser = None
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нажать на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # переключиться на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # считать значение для переменной x
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    # заполнить поле с id="answer"
    browser.find_element(By.ID, "answer").send_keys(y)

    # нажать на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # принять confirm в окне alert
    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1:])
    alert.accept()


finally:
    if browser:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        # time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()
