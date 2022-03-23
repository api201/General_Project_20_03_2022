from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        #OLD2 login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK), "#login_link"
        #login_link.click()
        #LOGIN_LINK.click()

    # variant 1
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    #     return LoginPage(browser=self.browser, url=self.browser.current_url)

    # variant 2
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)


        #1 def should_be_login_link(self):
    #1     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

    def should_be_login_link(self):
        #OLD1 assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        #OLD2 assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # "*" is a tuple?


        #assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        #2 changes