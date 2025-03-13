import allure
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    url = 'https://www.mvideo.ru/'

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    CITY_BUTTON = ("xpath", "//button[contains(@class, 'location-confirm')]")
    MAIN_BUTTON = ("xpath", "//button[@aria-label='Каталог']")
    MENU_SECTION = ("xpath", "//a[@href='https://www.mvideo.ru/televizory-i-video']")
    PRODUCT_TYPE_BUTTON = ("xpath", "(//a[@class='fl-category'])[1]")
    PRODUCT_TYPE_TITLE = ("xpath", "//h1[@class='fl-h1']")
    TV_TYPE_BUTTON = ("xpath", "(//div[@class='fl-category__title'])[2]")

    # Actions
    def click_city_button(self):
        with allure.step("Clicked city button"):
            self.wait.until(EC.element_to_be_clickable(self.CITY_BUTTON)).click()
            print("Clicked city button")

    def click_main_button(self):
        with allure.step("Clicked main button"):
            self.wait.until(EC.element_to_be_clickable(self.MAIN_BUTTON)).click()
            print("Clicked main button")

    def click_menu_section(self):
        with allure.step("Clicked menu section"):
            self.wait.until(EC.element_to_be_clickable(self.MENU_SECTION)).click()
            print("Clicked menu section")

    def click_product_type_button(self):
        with allure.step("Clicked product type button"):
            self.wait.until(EC.element_to_be_clickable(self.PRODUCT_TYPE_BUTTON)).click()
            print("Clicked product type button")

    def click_tv_type_button(self):
        with allure.step("Clicked TV type button"):
            self.wait.until(EC.element_to_be_clickable(self.TV_TYPE_BUTTON)).click()
            print("Clicked TV type button")

    # Methods

    @allure.title("Testing Main page")
    def find_product(self):
        # Logger.add_start_step(method='find_product')
        self.driver.get(self.url)
        self.get_current_url()
        self.click_city_button()
        self.click_main_button()
        self.click_menu_section()
        self.click_product_type_button()
        self.check_title(self.get_locator_text(self.PRODUCT_TYPE_TITLE), 'Телевизоры и цифровое ТВ')
        self.click_tv_type_button()
        # Logger.add_end_step(self.driver.current_url, method='find_product')
