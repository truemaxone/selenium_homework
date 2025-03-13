import pytest

from pages.main_page import MainPage
from pages.setting_product_page import SettingProductPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage


class BaseTest:

    main_page: MainPage
    setting_product_page: SettingProductPage
    cart_page: CartPage
    product_page: ProductPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):

        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
        request.cls.setting_product_page = SettingProductPage(driver)
        request.cls.cart_page = CartPage(driver)
        request.cls.product_page = ProductPage(driver)
