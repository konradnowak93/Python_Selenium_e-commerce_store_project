import time
import allure
import pytest
from shop.locators.locators import MainPageLocators
from shop.pages.main_page import MainPage
from shop.pages.product_page import ProductPage
from shop.pages.products_list_page import ProductsList


@pytest.mark.usefixtures("setup")
class TestMainPageTabs:

    @allure.title("Click on Checkout tab from the main page (products in the shopping cart)")
    def test_click_checkout_from_mainpage_cart(self, setup):
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
        self.driver.execute_script("scroll(0, 350)")
        product_page.add_to_cart_first_product()
        time.sleep(3)
        main_page.click_on_main_logo()
        main_page.click_on_checkout()
        assert "CHECKOUT" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

    @allure.title("Click on Checkout tab from the main page (no products in the shopping cart)")
    def test_click_checkout_from_mainpage_emptycart(self, setup):
        self.driver.get("http://shop.demoqa.com")
        main_page = MainPage(self.driver)

        main_page.close_information_banner()
        main_page.click_on_checkout()
        # If we do not have any items in the shopping cart, we will be redirected to the shopping cart
        assert "CART" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

    @allure.title("Click on My Account tab from the main page")
    def test_click_myaccount_from_mainpage(self, setup):
        self.driver.get("http://shop.demoqa.com")
        main_page = MainPage(self.driver)

        main_page.close_information_banner()
        main_page.click_on_my_account()
        assert "MY ACCOUNT" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

    @allure.title("Click on Wishlist tab from the main page")
    def test_click_wishlist_from_mainpage(self, setup):
        self.driver.get("http://shop.demoqa.com")
        main_page = MainPage(self.driver)

        main_page.close_information_banner()
        main_page.click_on_my_wishlist()
        assert "WISHLIST" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

    @allure.title("Click on Shopping cart tab from the main page")
    def test_click_cart_from_mainpage(self, setup):
        self.driver.get("http://shop.demoqa.com")
        main_page = MainPage(self.driver)

        main_page.close_information_banner()
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
        self.driver.execute_script("scroll(0, 350)")
        product_page.add_to_cart_first_product()
        time.sleep(3)
        main_page.click_on_main_logo()
        main_page.click_on_checkout()
        assert "CHECKOUT" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

        main_page.click_on_my_account()
        assert "MY ACCOUNT" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

        main_page.click_on_my_wishlist()
        assert "WISHLIST" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text

        main_page.click_on_shopping_cart()
        assert "CART" in self.driver.find_element_by_class_name(MainPageLocators.page_title_class).text