"""

"""
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"
txt = str(math.ceil(math.pow(math.pi, math.e)*10000))

browser = None
try:
    browser = webdriver.Firefox()
    browser.get(link)

    link2 = browser.find_element(By.LINK_TEXT, txt)
    link2.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("I")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("P")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smol")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Kiyev")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    if browser:
        browser.quit()
