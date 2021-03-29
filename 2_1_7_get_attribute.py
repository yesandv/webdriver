from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    robot = browser.find_element_by_id("robotCheckbox").click()

    robotRule = browser.find_element_by_id("robotsRule").click()

    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(15)
    browser.quit()
