import time
import allure
import pytest
from shop.locators.locators import CheckoutLocators
from shop.pages.checkout_page import CheckoutPage
from shop.pages.main_page import MainPage
from shop.pages.product_page import ProductPage
from shop.pages.products_list_page import ProductsList
from shop.pages.shopping_cart_page import ShoppingCartPage

@pytest.mark.usefixtures("setup")
class TestCheckout:

    @allure.title("Fill billing details")
    def test_fill_billing_details(self, setup):
        self.driver.get("http://shop.demoqa.com/shop/")
        main_page = MainPage(self.driver)
        products_list = ProductsList(self.driver)
        product_page = ProductPage(self.driver)
        shopping_cart = ShoppingCartPage(self.driver)
        checkout = CheckoutPage(self.driver)

        first_product = products_list.find_first_product()
        main_page.click_on_search_field()
        main_page.fill_search_field(first_product)
        product_page.select_colour()
        product_page.select_size()
        product_page.add_to_cart_first_product()
        product_page.view_cart()
        shopping_cart.proceed_to_checkout()
        checkout.insert_billing_name()
        checkout.insert_billing_lastname()
        checkout.insert_billing_company()
        checkout.select_billing_country()
        checkout.insert_house_and_street()
        checkout.insert_billing_apartment()
        checkout.insert_billing_postcode()
        checkout.insert_billing_city()
        checkout.insert_billing_phone()
        checkout.insert_billing_email()
        time.sleep(3)
        checkout.tick_terms_checkbox()
        checkout.place_order()

        assert "Your order has been received" in self.driver.find_element_by_class_name(CheckoutLocators.order_received_class).text