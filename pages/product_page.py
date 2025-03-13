import allure
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
    # Locators
    PRODUCT_NAME = ("xpath", "//h1[@class='title']")
    PRODUCT_PRICE = ("xpath", "//div[@class='price price--pdp-emphasized-personal-price ng-star-inserted']")
    ADD_TO_CART_BUTTON = ("xpath", "//button[@size='large' and @title='Добавить в корзину']")
    BUBBLE_ON_CART = ("xpath", "//mvid-bubble[@class='bubble ng-star-inserted']")
    CART_BUTTON = ("xpath", "//a[@href='https://www.mvideo.ru/cart' and @class='link']")

    # Actions

    def click_add_to_cart_button(self):
        with allure.step('Clicked "Add to cart" button'):
            self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()
            print('Clicked "Add to cart" button')

    def click_cart_button(self):
        self.wait.until(EC.presence_of_element_located(self.BUBBLE_ON_CART))
        with allure.step("Clicked cart button"):
            self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON)).click()
            print("Clicked cart button")

    # Methods

    @allure.title("Testing Product page")
    def add_product_to_cart(self):
        # Logger.add_start_step(method='add_product_to_cart')
        self.get_current_url()
        self.check_title(self.get_locator_text(self.PRODUCT_NAME), 'Телевизор LG 55QNED806QA')
        self.check_title(self.get_product_price(self.PRODUCT_PRICE), '98 890')
        self.click_add_to_cart_button()
        self.click_cart_button()
        # Logger.add_end_step(self.driver.current_url, method='add_product_to_cart')
