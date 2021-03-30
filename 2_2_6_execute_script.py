from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element_by_css_selector(".form-group label #input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    robot = browser.find_element_by_css_selector("[for='robotCheckbox']").click()

    robotRule = browser.find_element_by_id("robotsRule").click()

    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(15)
    browser.quit()
