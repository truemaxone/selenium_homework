import allure
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    url = 'https://www.mvideo.ru/'

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.wait = wait

    # Locators
    city_button_locator = ("xpath", "//button[contains(@class, 'location-confirm')]")
    main_button_locator = ("xpath", "(//button[contains(@class, 'mv-main-button--large')])[1]")
    menu_section_locator = ("xpath", "//a[@href='https://www.mvideo.ru/televizory-i-video']")
    product_type_button_locator = ("xpath", "(//a[@class='fl-category'])[1]")
    product_type_title_locator = ("xpath", "//h1[@class='fl-h1']")
    tv_type_button_locator = ("xpath", "(//div[@class='fl-category__title'])[2]")
    tv_type_title_locator = ("xpath", "//h1[@class='title ng-star-inserted']")

    # Getters

    def get_city_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.city_button_locator))

    def get_main_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.main_button_locator))

    def get_menu_section(self):
        return self.wait.until(EC.element_to_be_clickable(self.menu_section_locator))

    def get_product_type_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.product_type_button_locator))

    def get_product_type_title(self):
        return self.wait.until(EC.element_to_be_clickable(self.product_type_title_locator))

    def get_tv_type_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.tv_type_button_locator))

    def get_tv_type_title(self):
        return self.wait.until(EC.element_to_be_clickable(self.tv_type_title_locator))

    # Actions
    def click_city_button(self):
        with allure.step("Clicked city button"):
            self.get_city_button().click()
            print("Clicked city button")

    def click_main_button(self):
        with allure.step("Clicked main button"):
            self.get_main_button().click()
            print("Clicked main button")

    def click_menu_section(self):
        with allure.step("Clicked menu section"):
            self.get_menu_section().click()
            print("Clicked menu section")

    def click_product_type_button(self):
        with allure.step("Clicked product type button"):
            self.get_product_type_button().click()
            print("Clicked product type button")

    def click_tv_type_button(self):
        with allure.step("Clicked TV type button"):
            self.get_tv_type_button().click()
            print("Clicked TV type button")

    # Methods

    @allure.feature("Testing Main page")
    def find_product(self):
        Logger.add_start_step(method='find_product')
        self.driver.get(self.url)
        self.get_current_url()
        self.click_city_button()
        self.click_main_button()
        self.click_menu_section()
        self.click_product_type_button()
        self.check_title(self.get_product_type_title(), 'Телевизоры и цифровое ТВ')
        self.click_tv_type_button()
        self.check_title(self.get_tv_type_title(), 'Смарт телевизоры')
        Logger.add_end_step(self.driver.current_url, method='find_product')
