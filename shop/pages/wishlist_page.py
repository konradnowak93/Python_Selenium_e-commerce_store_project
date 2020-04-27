from selenium import webdriver

from shop.locators.locators import WishlistLocators


class WishlistPage:

    def __init__(self, driver):
        self.driver = driver

    def remove_product_from_wishlist(self):
        remove_button = self.driver.find_element_by_xpath(WishlistLocators.remove_from_wishlist_button_xpath)
        webdriver.ActionChains(self.driver).move_to_element(remove_button).click(remove_button).perform()

    def select_product_options(self):
        select_options = self.driver.find_element_by_xpath(WishlistLocators.select_options_xpath)
        webdriver.ActionChains(self.driver).move_to_element(select_options).click(select_options).perform()