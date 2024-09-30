import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage
from pages.setting_product_page import SettingProductPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@allure.feature('Test login and buy product')
def test_buy_product(set_module):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                         "like Gecko) Chrome/128.0.0.0 Safari/537.3")
    prefs = {"profile.default_content_setting_values.notifications": 2}  # Off popups
    options.add_experimental_option("prefs", prefs)
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 15, poll_frequency=1)

    mp = MainPage(driver, wait)
    mp.find_product()

    spp = SettingProductPage(driver, wait)
    spp.set_product_settings()

    product_name = spp.get_product_name()
    product_price = spp.get_product_price()

    pp = ProductPage(driver, wait)
    check_product_name = pp.get_product_name()
    check_product_price = pp.get_product_price()
    pp.add_product_to_cart()

    with allure.step('Check product name matches page product name'):
        assert product_name == check_product_name
        print("Product name check successful")
    with allure.step('Check product price matches page product price'):
        assert product_price == check_product_price
        print("Product price check successful")

    cp = CartPage(driver, wait)
    cart_product_name = cp.get_cart_product_name()
    cart_product_price = cp.get_cart_product_price()
    cp.finish_purchase()

    with allure.step('Check product name matches cart product name'):
        assert product_name == cart_product_name
        print("Product name in cart check successful")
    with allure.step('Check product price matches cart product price'):
        assert product_price == cart_product_price
        print("Product price in cart check successful")
