import allure
import pytest
from shop.locators.locators import MyAccountLocators
from shop.pages.main_page import MainPage
from shop.pages.my_account_page import MyAccount

@pytest.mark.usefixtures("setup")
class TestMainPageTabs:

    @allure.title("Account registration - correct data")
    def test_register_account(self, setup):
        self.driver.get("http://shop.demoqa.com/")
        main_page = MainPage(self.driver)
        my_account_page = MyAccount(self.driver)

        main_page.close_information_banner()
        main_page.click_on_my_account()
        my_account_page.fill_random_reg_username("TestName")
        my_account_page.fill_random_reg_mail("testuser@thisisonlytest.com")
        my_account_page.fill_reg_password("Testtesttest!")
        my_account_page.perform_register()

        assert "Back to ToolsQA Demo Site" in self.driver.find_element_by_xpath(MyAccountLocators.back_to_blog_button_xpath).text