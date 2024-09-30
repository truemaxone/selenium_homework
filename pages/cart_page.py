import allure
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.wait = wait

    # Locators
    cart_product_name_locator = ("xpath", "//div[@class='cart-item__name-container']")
    cart_product_price_locator = ("xpath", "//div[@class='cart-item-price']")
    checkout_button_locator = ("xpath", "//div[text()= ' Перейти к оформлению ']")
    cart_page_title_locator = ("xpath", "//h1[@class='cart__title ng-star-inserted']")

    # Getters

    def get_cart_product_name(self):
        return self.wait.until(EC.element_to_be_clickable(self.cart_product_name_locator)).text

    def get_cart_product_price(self):
        return self.wait.until(EC.element_to_be_clickable(self.cart_product_price_locator)).text.split(' ₽')[0]

    def get_cart_title(self):
        return self.driver.find_element(*self.cart_page_title_locator)

    def get_checkout_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.checkout_button_locator))

    # Actions

    def click_checkout_button(self):
        with allure.step('Clicked "Checkout" button'):
            self.get_checkout_button().click()
            print("Clicked 'Checkout' button")

    # Methods

    @staticmethod
    def check_title(title, check_title):
        clean_title = title.text.split()[0]
        with allure.step(f'Title "{check_title}" successfully verified'):
            assert clean_title == check_title
            print(f'Title "{check_title}" successfully verified')

    @allure.feature("Testing Cart page")
    def finish_purchase(self):
        Logger.add_start_step(method='finish_purchase')
        self.get_current_url()
        self.check_title(self.get_cart_title(), 'Корзина')
        self.click_checkout_button()
        Logger.add_end_step(self.driver.current_url, method='finish_purchase')
