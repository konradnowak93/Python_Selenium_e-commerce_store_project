import random
from selenium import webdriver
from shop.locators.locators import MyAccountLocators

class MyAccount:

    def __init__(self, driver):
        self.driver = driver

    def fill_random_reg_username(self, reg_username):
        self.reg_username = reg_username + str(random.randint(0, 10000))
        self.driver.find_element_by_id(MyAccountLocators.register_username_id).click()
        self.driver.find_element_by_id(MyAccountLocators.register_username_id).send_keys(self.reg_username)

    def fill_static_username(self, reg_username):
        self.driver.find_element_by_id(MyAccountLocators.register_username_id).click()
        self.driver.find_element_by_id(MyAccountLocators.register_username_id).send_keys(reg_username)

    def fill_random_reg_mail(self, reg_mail):
        self.reg_mail = str(random.randint(0, 10000)) + reg_mail
        self.driver.find_element_by_id(MyAccountLocators.register_mail_id).click()
        self.driver.find_element_by_id(MyAccountLocators.register_mail_id).send_keys(self.reg_mail)

    def fill_static_mail(self, reg_mail):
        self.driver.find_element_by_id(MyAccountLocators.register_mail_id).click()
        self.driver.find_element_by_id(MyAccountLocators.register_mail_id).send_keys(reg_mail)

    def fill_reg_password(self, reg_password):
        self.driver.find_element_by_id(MyAccountLocators.register_password_id).click()
        self.driver.find_element_by_id(MyAccountLocators.register_password_id).send_keys(reg_password)

    def perform_register(self):
        self.driver.find_element_by_name(MyAccountLocators.register_button_name).click()

    def go_back_to_shop(self):
        hover_element = self.driver.find_element_by_xpath(MyAccountLocators.go_back_to_shop_button_xpath)
        webdriver.ActionChains(self.driver).move_to_element(hover_element).click(hover_element).perform()

    def fill_login_or_mail(self, login):
        self.driver.find_element_by_id(MyAccountLocators.login_username_or_email_id).click()
        self.driver.find_element_by_id(MyAccountLocators.login_username_or_email_id).send_keys(login)

    def fill_login_password(self, login_password):
        self.driver.find_element_by_id(MyAccountLocators.login_password_id).click()
        self.driver.find_element_by_id(MyAccountLocators.login_password_id).send_keys(login_password)

    def perform_login(self):
        self.driver.find_element_by_name(MyAccountLocators.login_button_name).click()

    def get_reg_username(self):
        reg_username = self.driver.find_element_by_id(MyAccountLocators.register_username_id).get_attribute('value')
        return reg_username

    def get_reg_password(self):
        reg_password = self.driver.find_element_by_id(MyAccountLocators.register_password_id).get_attribute('value')
        return reg_password