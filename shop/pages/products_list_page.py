from shop.locators.locators import ProductsListLocators


class ProductsList:

    def __init__(self, driver):
        self.driver = driver

    def find_first_product(self):
        products_list = self.driver.find_elements_by_xpath(ProductsListLocators.products_list_xpath)
        product_names = [name.get_attribute("textContent") for name in products_list]
        first_on_list = product_names[0]
        return first_on_list

    def find_second_product(self):
        products_list = self.driver.find_elements_by_xpath(ProductsListLocators.products_list_xpath)
        product_names = [name.get_attribute("textContent") for name in products_list]
        second_on_list = product_names[1]
        return second_on_list