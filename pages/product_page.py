from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page_with_add_to_basket_button(self):
        self.should_be_promo_url()
        self.should_be_add_to_basket_button()

    def should_be_the_same_product_name_and_price_in_message(self):
        self.should_be_correct_product_name_in_message()
        self.should_be_correct_product_price_in_message()

    def should_be_promo_url(self):
        assert "?promo=offer" in self.browser.current_url, \
            "'?promo=offer' string in url is missing"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_product_name_in_message(self):
        item_name_in_message = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_MESSAGE)
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        assert item_name.text == item_name_in_message.text, \
            "Wrong item name in message"

    def should_be_correct_product_price_in_message(self):
        basket_total_price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE_IN_MESSAGE)
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        assert item_price.text == basket_total_price_in_message.text, \
            "Wrong item price in message"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappear"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
