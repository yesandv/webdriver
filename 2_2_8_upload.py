from selenium import webdriver
import os
import time


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

try:
    name = browser.find_element_by_name("firstname")
    name.send_keys("Ivan")

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Petrov")

    email = browser.find_element_by_name("email")
    email.send_keys("e@mail")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_test.txt"
    file_path = os.path.join(current_dir, file_name)

    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    submit = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(15)
    browser.quit()
