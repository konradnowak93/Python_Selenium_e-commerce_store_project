from selenium import webdriver
from selenium.webdriver.support.select import Select
from shop.locators.locators import CheckoutLocators


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def insert_billing_name(self):
        self.driver.find_element_by_id(CheckoutLocators.billing_first_name_id).click()
        self.driver.find_element_by_id(CheckoutLocators.billing_first_name_id).send_keys("TestName")

    def insert_billing_lastname(self):
        self.driver.find_element_by_id(CheckoutLocators.billing_last_name_id).click()
        self.driver.find_element_by_id(CheckoutLocators.billing_last_name_id).send_keys("TestLastname")

    def insert_billing_company(self):
        self.driver.find_element_by_id(CheckoutLocators.billing_company_id).click()
        self.driver.find_element_by_id(CheckoutLocators.billing_company_id).send_keys("TestCompany")

    def select_billing_country(self):
        countries_list = Select(self.driver.find_element_by_xpath(CheckoutLocators.countries_list_xpath))
        countries_list.select_by_visible_text("Poland")

    def insert_house_and_street(self):
        self.driver.find_element_by_id(CheckoutLocators.house_and_street_id).click()
        self.driver.find_element_by_id(CheckoutLocators.house_and_street_id).send_keys("Test Street 1")

    def insert_billing_apartment(self):
        self.driver.find_element_by_id(CheckoutLocators.apartment_id).click()
        self.driver.find_element_by_id(CheckoutLocators.apartment_id).send_keys("10")

    def insert_billing_postcode(self):
        self.driver.find_element_by_id(CheckoutLocators.billing_postcode_id).click()
        self.driver.find_element_by_id(CheckoutLocators.billing_postcode_id).send_keys("36-200")

    def insert_billing_city(self):
        self.driver.find_element_by_id(CheckoutLocators.billing_city_id).click()
        self.driver.find_element_by_id(CheckoutLocators.billing_city_id).send_keys("Test City")

    def insert_billing_phone(self):
        self.driver.find_element_by_id(CheckoutLocators.billing_phone_id).click()
        self.driver.find_element_by_id(CheckoutLocators.billing_phone_id).send_keys("+48 111 222 333")

    def insert_billing_email(self):
        self.driver.find_element_by_id(CheckoutLocators.billing_email_id).click()
        self.driver.find_element_by_id(CheckoutLocators.billing_email_id).send_keys("918273645test@qweasdzxc.pl")

    def place_order(self):
        place_order_btn = self.driver.find_element_by_id(CheckoutLocators.place_order_id)
        webdriver.ActionChains(self.driver).move_to_element(place_order_btn).click(place_order_btn).perform()

    def tick_terms_checkbox(self):
        self.driver.find_element_by_xpath(CheckoutLocators.terms_conditions_xpath).click()