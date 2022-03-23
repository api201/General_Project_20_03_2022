from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'The items in the cart are displayed, but they should not be'

    def should_be_see_text_that_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            'There is no text stating that the basket is empty'
