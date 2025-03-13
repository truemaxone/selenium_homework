import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)

    def get_current_url(self):
        print(f"Current URL - {self.driver.current_url}")

    @staticmethod
    def check_title(title, check_title):
        with allure.step(f'Title "{check_title}" successfully verified'):
            assert title == check_title
            print(f'Title "{check_title}" successfully verified')

    def check_url(self, check_url):
        with allure.step(f'URL "{check_url}" successfully verified'):
            assert self.driver.current_url == check_url
            print(f'URL "{check_url}" successfully verified')

    def get_locator_text(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def get_product_price(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text.replace(' ₽', '')
