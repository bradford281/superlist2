import time
from selenium.webdriver.support.ui import WebDriverWait
from .base import FunctionalTest

TEST_EMAIL = 'tddtester@yahoo.com'
TEST_PASSWORD = 'Sudosu2012!'

class LoginTest(FunctionalTest):
    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
                retries -= 1
                time.sleep(0.5)
                
        self.fail('could not find window')

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id)
            )
    
    def test_login_with_persona(self):
        # Edith goes to the awesome superlists site.
        # and notices the "Sign in" link for the first time.
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('login').click()

        # A Persona login box appears
        self.switch_to_new_window('Mozilla Persona')
        self.browser.find_element_by_id(
            'authentication_email'
            ).send_keys(TEST_EMAIL)
        self.browser.find_element_by_tag_name('button').click()
        
        # We get redirected to the Yahoo Page
        self.wait_for_element_with_id('username')
        self.browser.find_element_by_id(
            'username'
            ).send_keys(TEST_EMAIL)
        self.browser.find_element_by_id(
            'passwd'
            ).send_keys(TEST_PASSWORD)
        self.browser.find_element_by_id('.save').click()
        
        # The Persona window closes
        self.switch_to_new_window('To-Do')
        
        # She can see that she is logged in
        self.wait_for_element_with_id('logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(TEST_EMAIL, navbar.text)
        
