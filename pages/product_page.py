from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def adding_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_basket.click()

    def should_be_name_product_to_message(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product_to_message = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_TO_MESSAGE)
        assert name_product.text == name_product_to_message.text, 'The message does not contain the name of the ' \
                                                                  'product added to the basket '

    def should_be_price_product_to_message(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_product_to_message = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_TO_MESSAGE)
        assert price_product.text == price_product_to_message.text, 'The cost of the basket does not match the price ' \
                                                                    'of the product '

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappear(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappear"