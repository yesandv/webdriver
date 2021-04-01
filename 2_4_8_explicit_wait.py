from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button = browser.find_element_by_id("book").click()

    x_element = browser.find_element_by_css_selector("label #input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_id("solve").click()

finally:
    time.sleep(15)
    browser.quit()
