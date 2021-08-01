import time


def test_add_to_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(3)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert button.is_displayed(), "Button is not visible"
