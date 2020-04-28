from selenium import webdriver

from shop.locators.locators import ShoppingCartLocators


class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver

    def remove_from_cart(self):
        remove_from_cart_btn = self.driver.find_element_by_xpath(ShoppingCartLocators.remove_from_cart_xpath)
        webdriver.ActionChains(self.driver).move_to_element(remove_from_cart_btn).click(remove_from_cart_btn).perform()

    def clear_cart(self):
        clear_cart_btn = self.driver.find_element_by_class_name(ShoppingCartLocators.clear_cart_class)
        webdriver.ActionChains(self.driver).move_to_element(clear_cart_btn).click(clear_cart_btn).perform()

    def update_cart(self):
        update_cart_btn = self.driver.find_element_by_name(ShoppingCartLocators.update_cart_name)
        webdriver.ActionChains(self.driver).move_to_element(update_cart_btn).click(update_cart_btn).perform()

    def continue_shopping(self):
        continue_btn = self.driver.find_element_by_class_name(ShoppingCartLocators.continue_shopping_class)
        webdriver.ActionChains(self.driver).move_to_element(continue_btn).click(continue_btn).perform()

    def increase_qty(self):
        increase_quantity_btn = self.driver.find_element_by_class_name(ShoppingCartLocators.increase_qty_class)
        webdriver.ActionChains(self.driver).move_to_element(increase_quantity_btn).click(increase_quantity_btn).perform()

    def decrease_qty(self):
        decrease_quantity_btn = self.driver.find_element_by_class_name(ShoppingCartLocators.decrease_qty_class)
        webdriver.ActionChains(self.driver).move_to_element(decrease_quantity_btn).click(decrease_quantity_btn).perform()

    def proceed_to_checkout(self):
        proceed_to_checkout_btn = self.driver.find_element_by_xpath(ShoppingCartLocators.proceed_to_checkout_xpath)
        webdriver.ActionChains(self.driver).move_to_element(proceed_to_checkout_btn).click(proceed_to_checkout_btn).perform()

    def get_product_price(self):
        price = self.driver.find_element_by_xpath(ShoppingCartLocators.product_price_xpath).text
        return price