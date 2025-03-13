import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class SettingProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.move = ActionChains(self.driver)

    # Locators

    TV_TYPE_TITLE = ("xpath", "//h1[@class='title ng-star-inserted']")
    BRAND_CHECKBOX = ("xpath", "(//div[@class='checkbox'])[2]")
    LEFT_SLIDER = ("xpath", "//button[@class='slider__knob ng-star-inserted']")
    RIGHT_SLIDER = ("xpath", "//button[@class='slider__knob']")
    SHOW_MORE_BUTTON = ("xpath", "(//p[@class='show-all ng-star-inserted'])[2]")
    DIAGONAL_CHECKBOX = ("xpath", "//a[text()=' 55\" - 64\" ']")

    RESOLUTION_DIV = ("xpath", "//div[@class='accordion__option ng-tns-c3416668012-11']/div")
    SHOW_MORE_RESOLUTION = ("xpath", "//label[@class='accordion__title ng-tns-c3416668012-11']")
    RESOLUTION_CHECKBOX = ("xpath", "//a[text()=' 4K Ultra HD (3840x2160 Пикс) ']")

    FREQUENCY_DIV = ("xpath", "//div[@class='accordion__option ng-tns-c3416668012-12']/div[@class]")
    SHOW_MORE_FREQUENCY = ("xpath", "//label[@class='accordion__title ng-tns-c3416668012-12']")
    FREQUENCY_CHECKBOX = ("xpath", "//a[text()=' 120 Гц ']")

    PRODUCT_LINK = ("xpath", "//a[@class='product-title__text']")

    # Sliders

    def get_left_slider(self):
        return self.wait.until(EC.element_to_be_clickable(self.LEFT_SLIDER))

    def get_right_slider(self):
        return self.wait.until(EC.element_to_be_clickable(self.RIGHT_SLIDER))

    # Actions

    def click_brand_checkbox(self):
        with allure.step("Clicked brand checkbox"):
            self.wait.until(EC.element_to_be_clickable(self.BRAND_CHECKBOX)).click()
            print("Clicked brand checkbox")

    def move_left_slider(self):
        with allure.step("Left slider moved"):
            self.move.click_and_hold(self.get_left_slider()).move_by_offset(20, 0).release().perform()
            print("Left slider moved")

    def move_right_slider(self):
        with allure.step("Right slider moved"):
            self.move.click_and_hold(self.get_right_slider()).move_by_offset(-50, 0).release().perform()
            print("Right slider moved")

    def click_show_more_button(self):
        with allure.step('Clicked "Show more" button'):
            self.wait.until(EC.element_to_be_clickable(self.SHOW_MORE_BUTTON)).click()
            print('Clicked "Show more" button')

    def click_diagonal_checkbox(self):
        with allure.step("Clicked screen diagonal checkbox"):
            self.wait.until(EC.element_to_be_clickable(self.DIAGONAL_CHECKBOX)).click()
            print("Clicked screen diagonal checkbox")

    def click_show_more_resolution_button(self):
        with allure.step('Clicked "Show more resolution" button'):
            try:
                self.driver.find_element(*self.RESOLUTION_DIV)
            except:
                self.wait.until(EC.element_to_be_clickable(self.SHOW_MORE_RESOLUTION)).click()
                print('Clicked "Show more resolution" button')

    def click_resolution_checkbox(self):
        with allure.step("Clicked screen resolution checkbox"):
            self.wait.until(EC.element_to_be_clickable(self.RESOLUTION_CHECKBOX)).click()
            print("Clicked screen resolution checkbox")

    def click_show_more_frequency_button(self):
        with allure.step('Clicked "Show more screen frequency" button'):
            try:
                self.driver.find_element(*self.FREQUENCY_DIV)
            except:
                self.wait.until(EC.element_to_be_clickable(self.SHOW_MORE_FREQUENCY)).click()
                print('Clicked "Show more screen frequency" button')

    def click_frequency_checkbox(self):
        with allure.step("Clicked screen frequency checkbox"):
            self.wait.until(EC.element_to_be_clickable(self.FREQUENCY_CHECKBOX)).click()
            print("Clicked screen frequency checkbox")

    def click_product_link(self):
        with allure.step("Clicked product link"):
            self.wait.until(EC.element_to_be_clickable(self.PRODUCT_LINK)).click()
            print("Clicked product link")

    # Methods

    @allure.title("Testing Setting product page")
    def set_product_settings(self):
        # Logger.add_start_step(method='set_product_settings')
        self.get_current_url()
        self.check_title(self.get_locator_text(self.TV_TYPE_TITLE), 'Смарт телевизоры')
        self.click_brand_checkbox()
        self.move_left_slider()
        self.move_right_slider()
        self.driver.execute_script("window.scrollTo(0, 1200)")
        self.click_show_more_button()
        self.click_diagonal_checkbox()
        self.click_show_more_resolution_button()
        self.click_resolution_checkbox()
        self.driver.execute_script("window.scrollTo(0, 1800)")
        self.click_show_more_frequency_button()
        self.click_frequency_checkbox()
        self.driver.execute_script("window.scrollTo(0, 0)")
        self.click_product_link()
        # Logger.add_end_step(self.driver.current_url, method='set_product_settings')
