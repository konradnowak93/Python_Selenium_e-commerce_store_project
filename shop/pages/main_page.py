from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from shop.locators.locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def close_information_banner(self):
        try:
            information_banner = self.driver.find_element_by_class_name(MainPageLocators.information_banner_class)
            information_banner.click()
        except NoSuchElementException:
            print("Element is not displayed")

    def click_on_my_wishlist(self):
        self.driver.find_element_by_xpath(MainPageLocators.my_wish_list_xpath).click()

    def click_on_my_account(self):
        self.driver.find_element_by_css_selector(MainPageLocators.my_account_css).click()

    def click_on_checkout(self):
        self.driver.find_element_by_xpath(MainPageLocators.checkout_xpath).click()

    def click_on_search_field(self):
        self.driver.find_element_by_class_name(MainPageLocators.search_field_class).click()

    def fill_search_field(self, product):
        self.driver.find_element_by_class_name(MainPageLocators.search_field_input_class).send_keys(product)
        self.driver.find_element_by_class_name(MainPageLocators.search_field_input_class).send_keys(Keys.ENTER)

    def click_on_shopping_cart(self):
        self.driver.find_element_by_xpath(MainPageLocators.shopping_cart_xpath).click()

    def click_on_main_logo(self):
        self.driver.find_element_by_class_name(MainPageLocators.main_logo_class).click()