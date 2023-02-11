from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>.in:nth-child(1)>.alertinner>strong")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    BASKET_TOTAL_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>.in>.alertinner>p>strong")
