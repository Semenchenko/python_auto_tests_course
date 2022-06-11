"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

browser = None
try:
    browser = webdriver.Firefox()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    if browser:
        browser.quit()
