"""
Explicit Waits

Чтобы определить момент, когда цена аренды уменьшится до $100,
используйте метод text_to_be_present_in_element
из библиотеки expected_conditions.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(n):
    return str(math.log(abs(12 * math.sin(int(n)))))


browser = None
try:
    # открыть страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # дождаться, когда цена дома уменьшится до $100
    # (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # нажать на кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # считать значение для переменной x
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    # заполнить поле с id="answer"
    browser.find_element(By.ID, "answer").send_keys(y)

    # нажать на кнопку "Submit"
    browser.find_element(By.ID, "solve").click()

    # принять confirm в окне alert
    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1:])
    alert.accept()

finally:
    if browser:
        # закрываем браузер после всех манипуляций
        # time.sleep(10)
        browser.quit()
