from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>.in:nth-child(1)>.alertinner>strong")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    BASKET_TOTAL_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>.in>.alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasketPageLocators:
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
    ITEMS_IN_CART = (By.CSS_SELECTOR, "#basket_totals")
