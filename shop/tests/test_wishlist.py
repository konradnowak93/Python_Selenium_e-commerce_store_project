import time
import allure
import pytest

from shop.locators.locators import WishlistLocators, ProductPageLocators
from shop.pages.main_page import MainPage
from shop.pages.product_page import ProductPage
from shop.pages.products_list_page import ProductsList
from shop.pages.wishlist_page import WishlistPage


@pytest.mark.usefixtures("setup")
class TestWishlist:

    @allure.title("Add product to wishlist")
    def test_add_product_to_wishlish(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        products_list = ProductsList(self.driver)
        product_page = ProductPage(self.driver)

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.add_to_wishlist()
        time.sleep(3)
        main_page.close_information_banner()
        main_page.click_on_my_wishlist()

        assert self.driver.find_element_by_xpath(WishlistLocators.remove_from_wishlist_button_xpath).is_displayed()

    @allure.title("Remove product from wishlist")
    def test_remove_product_from_wishlist(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        products_list = ProductsList(self.driver)
        product_page = ProductPage(self.driver)
        wishlist = WishlistPage(self.driver)

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.add_to_wishlist()
        time.sleep(3)
        main_page.close_information_banner()
        main_page.click_on_my_wishlist()
        wishlist.remove_product_from_wishlist()

        assert "successfully removed" in self.driver.find_element_by_class_name(WishlistLocators.successfully_removed_class).text

    @allure.title("Select product options")
    def test_select_product_options_btn(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        products_list = ProductsList(self.driver)
        product_page = ProductPage(self.driver)
        wishlist = WishlistPage(self.driver)

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.add_to_wishlist()
        time.sleep(3)
        main_page.close_information_banner()
        main_page.click_on_my_wishlist()
        wishlist.select_product_options()

        assert self.driver.find_element_by_xpath(ProductPageLocators.add_to_cart_first_product_xpath).is_displayed()