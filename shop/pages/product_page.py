from selenium import webdriver
from selenium.webdriver.support.select import Select
from shop.locators.locators import ProductPageLocators

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def select_colour(self):
        colour_selector = Select(self.driver.find_element_by_id(ProductPageLocators.product_colour_id))
        colour_selector.select_by_index(1)

    def select_size(self):
        size_selector = Select(self.driver.find_element_by_id(ProductPageLocators.product_size_id))
        size_selector.select_by_index(1)

    def add_to_cart_first_product(self):
        add_to_cart_btn = self.driver.find_element_by_xpath(ProductPageLocators.add_to_cart_first_product_xpath)
        webdriver.ActionChains(self.driver).move_to_element(add_to_cart_btn).click(add_to_cart_btn).perform()

    def add_to_cart_second_product(self):
        add_to_cart_btn = self.driver.find_element_by_xpath(ProductPageLocators.add_to_cart_second_product_xpath)
        webdriver.ActionChains(self.driver).move_to_element(add_to_cart_btn).click(add_to_cart_btn).perform()

    def add_to_wishlist(self):
        add_to_wishlist_icon = self.driver.find_element_by_xpath(ProductPageLocators.add_to_wishlist_xpath)
        webdriver.ActionChains(self.driver).move_to_element(add_to_wishlist_icon).click(add_to_wishlist_icon).perform()

    def view_cart(self):
        view_cart_button = self.driver.find_element_by_xpath(ProductPageLocators.view_cart_xpath)
        webdriver.ActionChains(self.driver).move_to_element(view_cart_button).click(view_cart_button).perform()

    def get_product_price(self):
        price = self.driver.find_element_by_xpath(ProductPageLocators.product_price_xpath).text
        return price