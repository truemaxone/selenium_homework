import allure

from base.base_test import BaseTest


@allure.feature("Mvideo shot testing")
class TestMvideo(BaseTest):

    @allure.title('Test search, setup and buy product')
    def test_buy_product(self, set_module):

        self.main_page.find_product()
        self.setting_product_page.set_product_settings()

        check_product_name = self.product_page.get_locator_text(self.product_page.PRODUCT_NAME)
        check_product_price = self.product_page.get_product_price(self.product_page.PRODUCT_PRICE)
        self.product_page.add_product_to_cart()

        cart_product_name = self.cart_page.get_locator_text(self.cart_page.CART_PRODUCT_NAME)
        cart_product_price = self.cart_page.get_product_price(self.cart_page.CART_PRODUCT_PRICE)
        self.cart_page.finish_purchase()

        with allure.step('Check product name matches cart product name'):
            assert check_product_name == cart_product_name
            print("Product name in cart check successful")
        with allure.step('Check product price matches cart product price'):
            assert check_product_price == cart_product_price
            print("Product price in cart check successful")
