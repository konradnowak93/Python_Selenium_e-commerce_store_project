import allure
import pytest
from shop.locators.locators import MainPageLocators
from shop.pages.main_page import MainPage
from shop.pages.product_page import ProductPage
from shop.pages.products_list_page import ProductsList
from shop.pages.shopping_cart_page import ShoppingCartPage


@pytest.mark.usefixtures("setup")
class TestMainPageTabs:

    @allure.title("Enter tabs from main page")
    def test_click_tabs_from_mainpage(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        product_page = ProductPage(self.driver)
        products_list = ProductsList(self.driver)
        shopping_cart = ShoppingCartPage(self.driver)

        main_page.close_information_banner()

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.select_colour()
        product_page.select_size()
        product_page.add_to_cart_first_product()
        main_page.click_on_main_logo()
        main_page.click_on_checkout()
        assert "CHECKOUT" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text
        main_page.click_on_shopping_cart()
        shopping_cart.clear_cart()

        main_page.click_on_main_logo()
        main_page.click_on_checkout()
        # If we do not have any items in the shopping cart, we will be redirected to the shopping cart
        assert "CART" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

        main_page.click_on_main_logo()
        main_page.click_on_my_account()
        assert "MY ACCOUNT" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

        main_page.click_on_main_logo()
        main_page.click_on_my_wishlist()
        assert "WISHLIST" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

        main_page.click_on_main_logo()
        main_page.click_on_shopping_cart()
        assert "CART" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

    @allure.title("Switch between tabs")
    def test_switch_between_tabs(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        product_page = ProductPage(self.driver)
        products_list = ProductsList(self.driver)

        main_page.close_information_banner()

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.select_colour()
        product_page.select_size()
        product_page.add_to_cart_first_product()
        main_page.click_on_checkout()
        assert "CHECKOUT" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

        main_page.click_on_my_account()
        assert "MY ACCOUNT" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

        main_page.click_on_my_wishlist()
        assert "WISHLIST" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

        main_page.click_on_shopping_cart()
        assert "CART" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text