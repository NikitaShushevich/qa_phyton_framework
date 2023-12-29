import time

from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators

class FormPage(BasePage):

    def fill_fields_and_submit(self):
        first_name = 'name'
        last_name = 'lastname'
        email = 'name@mail.com'
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys('1234567890')
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys('English')
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(r'test_file.txt')
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys('City, 123235, uk')
        self.element_is_visible(Locators.SUBMIT).click()
        time.sleep(5)
