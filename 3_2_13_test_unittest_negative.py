from selenium import webdriver
import time
import unittest


browser = webdriver.Chrome()
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class test_reg(unittest.TestCase):
    def test_reg1(self):
        browser.get(link1)

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

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_reg2(self):
        browser.get(link2)

        element_name = browser.find_element_by_css_selector(".first_block input.form-control.first")
        element_name.send_keys("Ivan")
        element_last_name = browser.find_element_by_css_selector(".first_block input.form-control.second")
        element_last_name.send_keys( "Petrov" )
        element_email = browser.find_element_by_css_selector(".first_block input.form-control.third")
        element_email.send_keys("e@mail")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",)

if __name__ == "__main__":
    unittest.main()
