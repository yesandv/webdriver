from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects2.html")

try:
    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    x = x_element.text
    y = y_element.text
    x = int(x)
    y = int(y)
    z = x + y
    z = str(str(int(x) + int(y)))

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z)

    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(15)
    browser.quit()
