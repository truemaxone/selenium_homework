from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class ProductPage(Base):

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    # Locators
    product_name_locator = ("xpath", "//h1[@class='title']")
    product_price_locator = ("xpath", "//div[@class='price price--pdp-emphasized-personal-price ng-star-inserted']")
    add_to_cart_button_locator = ("xpath", "//mvideoru-cart-button[@class='cart-btn ng-star-inserted']")
    bubble_on_cart_locator = ("xpath", "//mvid-bubble[@class='bubble ng-star-inserted']")
    cart_button_locator = ("xpath", "//a[@href='https://www.mvideo.ru/cart']")

    # Getters

    def get_product_name(self):
        return self.wait.until(EC.element_to_be_clickable(self.product_name_locator)).text

    def get_product_price(self):
        return self.wait.until(EC.element_to_be_clickable(self.product_price_locator)).text

    def get_add_to_cart_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_to_cart_button_locator))

    def get_cart_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.cart_button_locator))

    # Actions

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Clicked "Add to cart" button')

    def click_cart_button(self):
        self.wait.until(EC.presence_of_element_located(self.bubble_on_cart_locator))
        self.get_cart_button().click()
        print("Clicked cart button")

    # Methods

    def add_product_to_cart(self):
        Logger.add_start_step(method='add_product_to_cart')
        self.get_current_url()
        self.click_add_to_cart_button()
        self.click_cart_button()
        Logger.add_end_step(self.driver.current_url, method='add_product_to_cart')
