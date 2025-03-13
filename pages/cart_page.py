import allure
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    CART_PRODUCT_NAME = ("xpath", "//div[@class='cart-item__name-container']")
    CART_PRODUCT_PRICE = ("xpath", "//div[@class='cart-item-price']")
    CHECKOUT_BUTTON = ("xpath", "//div[text()= ' Перейти к оформлению ']")
    CART_PAGE_TITLE = ("xpath", "//h1[@class='cart__title ng-star-inserted']")

    # Actions

    def click_checkout_button(self):
        with allure.step('Clicked "Checkout" button'):
            self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()
            print("Clicked 'Checkout' button")

    @allure.title("Testing Cart page")
    def finish_purchase(self):
        # Logger.add_start_step(method='finish_purchase')
        self.get_current_url()
        self.check_title(self.get_locator_text(self.CART_PAGE_TITLE).split(' ')[0], 'Корзина')
        self.check_title(self.get_locator_text(self.CART_PRODUCT_NAME), 'Телевизор LG 55QNED806QA')
        self.check_title(self.get_product_price(self.CART_PRODUCT_PRICE), '98 890')
        self.click_checkout_button()
        # Logger.add_end_step(self.driver.current_url, method='finish_purchase')
