import time
import allure
import pytest

from shop.locators.locators import MyAccountLocators
from shop.pages.main_page import MainPage
from shop.pages.my_account_page import MyAccount

@pytest.mark.usefixtures("setup")
class TestMainPageTabs:

    @allure.title("Log in - correct data")
    def test_log_in(self, setup):
        self.driver.get("http://shop.demoqa.com/")
        main_page = MainPage(self.driver)
        my_account_page = MyAccount(self.driver)

        main_page.close_information_banner()
        main_page.click_on_my_account()
        my_account_page.fill_random_reg_username("TestName")
        username = my_account_page.get_reg_username()
        my_account_page.fill_random_reg_mail("testuser@thisisonlytest.com")
        my_account_page.fill_reg_password("Testtesttest!")
        password = my_account_page.get_reg_password()
        my_account_page.perform_register()
        my_account_page.go_back_to_shop()

        main_page.click_on_my_account()
        my_account_page.fill_login_or_mail(username)
        my_account_page.fill_login_password(password)
        my_account_page.perform_login()

        assert "Logout" in self.driver.find_element_by_xpath(MyAccountLocators.logout_button_xpath).text