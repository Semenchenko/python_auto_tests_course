"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

browser = None
try:
    browser = webdriver.Firefox()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("12")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("23")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("34")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("45")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    if browser:
        browser.quit()
