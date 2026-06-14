import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.ui_utils.ui_utils import UIUtils

CREATE_ACCOUNT_URL = "https://manage.ac2.mist.com/signin.html#!signup/register"

LOCATOR_FIRST_NAME    = (By.XPATH, "//input[@name='firstName' or @placeholder='First Name' or contains(@placeholder,'First')]")
LOCATOR_LAST_NAME     = (By.XPATH, "//input[@name='lastName' or @placeholder='Last Name' or contains(@placeholder,'Last')]")
LOCATOR_EMAIL         = (By.XPATH, "//input[@name='email' or @type='email' or @placeholder='Email']")
LOCATOR_PASSWORD      = (By.XPATH, "//input[@name='password' or @type='password']")
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

    def click_create_account_button(self):
        logging.info("CreateAccountLibs :: Clicking Create Account button")
        self.ui_utils.click_element(*LOCATOR_CREATE_BUTTON)

    def fill_and_submit_create_account_form(self, first_name, last_name, email, password):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_create_account_button()

    def is_on_create_account_page(self) -> bool:
        return "signup/register" in self.ui_utils.get_current_url()