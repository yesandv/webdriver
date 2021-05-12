from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"] )
class TestLinks():
    def test_answer(self, browser, url):
        answer = (math.log(int(time.time())))
        link = f"https://stepik.org/lesson/{url}/step/1"
        browser.get(link)
        browser.find_element_by_class_name("textarea.string-quiz__textarea.ember-text-area.ember-view").send_keys(str(answer))
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
        message = browser.find_element_by_class_name("smart-hints__hint")
        assert message.text == "Correct!"
