from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class SettingProductPage(Base):

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait
        self.move = ActionChains(self.driver)

    # Locators

    brand_checkbox_locator = ("xpath", "(//div[@class='checkbox'])[2]")
    left_slider_locator = ("xpath", "//button[@class='slider__knob ng-star-inserted']")
    right_slider_locator = ("xpath", "//button[@class='slider__knob']")
    show_more_button_locator = ("xpath", "(//p[@class='show-all ng-star-inserted'])[2]")
    diagonal_checkbox_locator = ("xpath", "//a[text()=' 65\" - 74\" ']")
    resolution_checkbox_locator = ("xpath", "//a[text()=' 4K Ultra HD (3840x2160 Пикс) ']")
    frequency_button_locator = ("xpath", "//div[text()=' Частота обновления ']")
    frequency_checkbox_locator = ("xpath", "//a[text()=' 120 Гц ']")
    screen_technology_button_locator = ("xpath", "//div[text()=' Технология экрана ']")
    screen_technology_checkbox_locator = ("xpath", "//a[text()=' 4K QLED ']")
    product_link_locator = ("xpath", "//a[@class='product-title__text']")
    product_name_locator = ("xpath", "//div[@class='product-title product-title--list']")
    product_price_locator = ("xpath", "//div[@class='price price--list ng-star-inserted']")

    # Getters

    def get_brand_checkbox(self):
        return self.wait.until(EC.element_to_be_clickable(self.brand_checkbox_locator))

    def get_left_slider(self):
        return self.wait.until(EC.element_to_be_clickable(self.left_slider_locator))

    def get_right_slider(self):
        return self.wait.until(EC.element_to_be_clickable(self.right_slider_locator))

    def get_show_more_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.show_more_button_locator))

    def get_diagonal_checkbox(self):
        return self.wait.until(EC.element_to_be_clickable(self.diagonal_checkbox_locator))

    def get_resolution_checkbox(self):
        return self.wait.until(EC.element_to_be_clickable(self.resolution_checkbox_locator))

    def get_frequency_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.frequency_button_locator))

    def get_frequency_checkbox(self):
        return self.wait.until(EC.element_to_be_clickable(self.frequency_checkbox_locator))

    def get_screen_technology_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.screen_technology_button_locator))

    def get_screen_technology_checkbox(self):
        return self.wait.until(EC.element_to_be_clickable(self.screen_technology_checkbox_locator))

    def get_product_link(self):
        return self.wait.until(EC.element_to_be_clickable(self.product_link_locator))

    def get_product_name(self):
        return self.wait.until(EC.presence_of_element_located(self.product_link_locator)).text

    def get_product_price(self):
        return self.wait.until(EC.presence_of_element_located(self.product_price_locator)).text

    # Actions

    def click_brand_checkbox(self):
        self.get_brand_checkbox().click()
        print("Clicked brand checkbox")

    def move_left_slider(self):
        self.move.click_and_hold(self.get_left_slider()).move_by_offset(20, 0).release().perform()
        print("Left slider moved")

    def move_right_slider(self):
        self.move.click_and_hold(self.get_right_slider()).move_by_offset(-50, 0).release().perform()
        print("Right slider moved")

    def click_show_more_button(self):
        self.get_show_more_button().click()
        print('Clicked "Show more" button')

    def click_diagonal_checkbox(self):
        self.get_diagonal_checkbox().click()
        print("Clicked screen diagonal checkbox")

    def click_resolution_checkbox(self):
        self.get_resolution_checkbox().click()
        print("Clicked screen resolution checkbox")

    def click_frequency_button(self):
        self.get_frequency_button().click()
        print("Clicked screen frequency button")

    def click_frequency_checkbox(self):
        self.get_frequency_checkbox().click()
        print("Clicked screen frequency checkbox")

    def click_screen_technology_button(self):
        self.get_screen_technology_button().click()
        print('Clicked "Screen technology" button')

    def click_screen_technology_checkbox(self):
        self.get_screen_technology_checkbox().click()
        print('Clicked "Screen technology" checkbox')

    def click_product_link(self):
        self.get_product_link().click()
        print("Clicked product link")

    # Methods

    def set_product_settings(self):
        Logger.add_start_step(method='set_product_settings')
        self.get_current_url()
        self.click_brand_checkbox()
        self.move_left_slider()
        self.move_right_slider()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.click_show_more_button()
        self.click_diagonal_checkbox()
        self.click_resolution_checkbox()
        self.click_frequency_button()
        self.click_frequency_checkbox()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.click_screen_technology_button()
        self.click_screen_technology_checkbox()
        self.driver.execute_script("window.scrollTo(0, 0)")
        self.click_product_link()
        Logger.add_end_step(self.driver.current_url, method='set_product_settings')
