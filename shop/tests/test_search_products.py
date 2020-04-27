import allure
import pytest
from shop.locators.locators import ProductsListLocators
from shop.pages.main_page import MainPage

@pytest.mark.usefixtures("setup")
class TestSearchProducts:

    @allure.title("Search an available product")
    def test_search_available_product(self, setup):
        self.driver.get("http://shop.demoqa.com/")
        main_page = MainPage(self.driver)

        main_page.click_on_search_field()
        main_page.fill_search_field("dress")

        assert self.driver.find_element_by_xpath(ProductsListLocators.products_list_xpath).is_displayed()