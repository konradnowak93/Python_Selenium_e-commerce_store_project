import allure
import pytest
from shop.locators.locators import ProductPageLocators, ShoppingCartLocators, ProductsListLocators, CheckoutLocators
from shop.pages.main_page import MainPage
from shop.pages.product_page import ProductPage
from shop.pages.products_list_page import ProductsList
from shop.pages.shopping_cart_page import ShoppingCartPage

@pytest.mark.usefixtures("setup")
class TestShoppingCart:

    @allure.title("Add available product to the shopping cart")
    def test_add_product_to_cart(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        products_list = ProductsList(self.driver)
        product_page = ProductPage(self.driver)

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.select_colour()
        product_page.select_size()
        product_page.add_to_cart_first_product()

        assert "has been added to your cart" in self.driver.find_element_by_class_name(ProductPageLocators.product_added_to_cart_class).text

    @allure.title("Remove a product from the shopping cart")
    def test_remove_from_shopping_cart(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        products_list = ProductsList(self.driver)
        product_page = ProductPage(self.driver)
        shopping_cart = ShoppingCartPage(self.driver)

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.select_colour()
        product_page.select_size()
        product_page.add_to_cart_first_product()
        product_page.view_cart()
        shopping_cart.remove_from_cart()

        assert "removed" in self.driver.find_element_by_class_name(ShoppingCartLocators.successfully_removed_class).text

    @allure.title("Clear the shopping cart")
    def test_clear_shopping_cart(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        products_list = ProductsList(self.driver)
        product_page = ProductPage(self.driver)
        shopping_cart = ShoppingCartPage(self.driver)

        first_product = products_list.find_first_product()
        second_product = products_list.find_second_product()
        #select first product
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.select_colour()
        product_page.select_size()
        product_page.add_to_cart_first_product()
        #select second product
        main_page.click_on_search_field()
        main_page.fill_search_field(second_product)
        product_page.select_colour()
        product_page.select_size()
        product_page.add_to_cart_second_product()
        product_page.view_cart()
        shopping_cart.clear_cart()

        assert "empty" in self.driver.find_element_by_xpath(ShoppingCartLocators.successfully_emptied_xpath).text

    @allure.title("Update the shopping cart")
    def test_update_shopping_cart(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        products_list = ProductsList(self.driver)
        product_page = ProductPage(self.driver)
        shopping_cart = ShoppingCartPage(self.driver)

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.select_colour()
        product_page.select_size()
        product_page.add_to_cart_first_product()
        product_page.view_cart()
        shopping_cart.increase_qty()
        shopping_cart.update_cart()

        assert "updated" in self.driver.find_element_by_xpath(ShoppingCartLocators.successfully_updated_xpath).text

    @allure.title("Continue shopping")
    def test_continue_shopping(self, setup):
        self.driver.get("http://shop.demoqa.com/shop")
        main_page = MainPage(self.driver)
        products_list = ProductsList(self.driver)
        product_page = ProductPage(self.driver)
        shopping_cart = ShoppingCartPage(self.driver)

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.select_colour()
        product_page.select_size()
        product_page.add_to_cart_first_product()
        product_page.view_cart()
        shopping_cart.continue_shopping()

        assert self.driver.find_element_by_xpath(ProductsListLocators.products_list_xpath).is_displayed()

    @allure.title("Proceed to checkout")
    def test_proceed_to_checkout(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        products_list = ProductsList(self.driver)
        product_page = ProductPage(self.driver)
        shopping_cart = ShoppingCartPage(self.driver)

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.select_colour()
        product_page.select_size()
        product_page.add_to_cart_first_product()
        product_page.view_cart()
        shopping_cart.proceed_to_checkout()

        assert self.driver.find_element_by_id(CheckoutLocators.order_review_heading_id).is_displayed()