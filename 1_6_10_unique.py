from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_name = browser.find_element_by_css_selector(".first_block input.form-control.first")
    element_name.send_keys("Ivan")
    element_last_name = browser.find_element_by_css_selector(".first_block input.form-control.second")
    element_last_name.send_keys("Petrov")
    element_email = browser.find_element_by_css_selector(".first_block input.form-control.third")
    element_email.send_keys("e@mail")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
