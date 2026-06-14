import logging, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.ui_utils.ui_utils import UIUtils

CREATE_ACCOUNT_URL = "https://manage.ac2.mist.com/signin.html#!signup/register"

LOCATOR_FIRST_NAME    = (By.XPATH, "//input[@name='firstName' or @placeholder='First Name' or contains(@placeholder,'First')]")
LOCATOR_LAST_NAME     = (By.XPATH, "//input[@name='lastName' or @placeholder='Last Name' or contains(@placeholder,'Last')]")
LOCATOR_EMAIL         = (By.XPATH, "//input[@name='email' or @type='email' or @placeholder='Email']")
LOCATOR_PASSWORD      = (By.XPATH, "//input[@name='password' or @type='password']")
LOCATOR_COMPANY_NAME = (By.XPATH, "//input[@name='companyName']")
LOCATOR_ADDRESS_1 = (By.XPATH, "//input[@name='data-input-field']")
LOCATOR_ADDRESS_2 = (By.XPATH, "//input[@name='companyAddress2']")
# LOCATOR_CITY = (By.XPATH, "//input[@name='city']")
# LOCATOR_ZIP = (By.XPATH, "//input[@name='zipCode']")
# LOCATOR_COUNTRY_DROPDOWN = (By.XPATH, "//select[2]")
# LOCATOR_STATE_DROPDOWN = (By.XPATH, "//select[1]")
LOCATOR_ADDRESS_SUGGESTIONS_DROPDOWN_FIRST_ITEM = (By.XPATH, "//div[contains(@class,'addressDropdown')]//li[1]")
LOCATOR_CREATE_BUTTON = (By.XPATH, "//button | //input[@type='submit'] | //input[@type='button']")


class CreateAccountLibs:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.ui_utils = UIUtils(driver)

    def navigate_to_create_account_page(self):
        logging.info("CreateAccountLibs :: Navigating to Create Account page")
        self.ui_utils.navigate_to(CREATE_ACCOUNT_URL)

    def enter_first_name(self, first_name: str):
        self.ui_utils.send_keys(*LOCATOR_FIRST_NAME, first_name)

    def enter_last_name(self, last_name: str):
        self.ui_utils.send_keys(*LOCATOR_LAST_NAME, last_name)

    def enter_email(self, email: str):
        self.ui_utils.send_keys(*LOCATOR_EMAIL, email)

    def enter_password(self, password: str):
        self.ui_utils.send_keys(*LOCATOR_PASSWORD, password)

    def enter_company_name(self, company_name: str):
        self.ui_utils.send_keys(*LOCATOR_COMPANY_NAME, company_name)

    def enter_company_address_1(self, address: str):
        self.ui_utils.send_keys(*LOCATOR_ADDRESS_1, address)
        time.sleep(1)  # Wait for the address to be populated after selection
        self.ui_utils.click_element(*LOCATOR_ADDRESS_SUGGESTIONS_DROPDOWN_FIRST_ITEM)
        time.sleep(1)  # Wait for the address to be populated after selection

    def enter_company_address_2(self, address: str):
        self.ui_utils.send_keys(*LOCATOR_ADDRESS_2, address)

    # def enter_city(self, city: str):
    #     self.ui_utils.send_keys(*LOCATOR_CITY, city)

    # def enter_zip(self, zip_code: str):
    #     self.ui_utils.send_keys(*LOCATOR_ZIP, zip_code)

    # def select_country(self, country: str):
    #     self.ui_utils.select_dropdown_by_text(*LOCATOR_COUNTRY_DROPDOWN, country)

    # def select_state(self, state: str):
    #     self.ui_utils.select_dropdown_by_text(*LOCATOR_STATE_DROPDOWN, state)

    def click_create_account_button(self):
        logging.info("CreateAccountLibs :: Clicking Create Account button")
        self.ui_utils.click_element(*LOCATOR_CREATE_BUTTON)

    def fill_and_submit_create_account_form(self, first_name, last_name, email, password, company_name, address1, address2):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_company_name(company_name)
        self.enter_company_address_1(address1)
        self.enter_company_address_2(address2)
        # self.select_country(country)
        # self.enter_city(city)
        # self.enter_zip(zip_code)
        # self.select_state(state)
        self.click_create_account_button()

    def is_on_create_account_page(self) -> bool:
        return "signup/register" in self.ui_utils.get_current_url()