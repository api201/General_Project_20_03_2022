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

class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    NAME_PRODUCT_TO_MESSAGE = (By.CSS_SELECTOR, '#messages strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    PRICE_PRODUCT_TO_MESSAGE = (By.CSS_SELECTOR, '.alert-info p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner>p')
