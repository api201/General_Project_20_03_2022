from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #old LOGIN_LINK = (By.ID, "registration_link")
    #LOGIN_LINK = (By.ID, "login_link")
    #LOGIN_LINK = (By.XPATH, "//*[@class='icon-signin']")
    #LOGIN_LINK = (By.XPATH, "//*[@href='/en-gb/accounts/login/']")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
