import pytest
import logging, time
from datetime import datetime
from libs.ui_libs.todo_create_account_libs import CreateAccountLibs
from utils.ui_utils.ui_utils import UIUtils


def generate_test_email():
    timestamp = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    return "automation.test.{}@example.com".format(timestamp)


class TestCreateAccount:

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = UIUtils.get_driver()
        self.create_account = CreateAccountLibs(self.driver)
        yield
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

    def test_create_account(self):
        """
        Test to fill all fields on the Create Account page and click Create Account button.
        a) Go to https://manage.ac2.mist.com/signin.html#!signup/register
        b) Enter the details for the various fields.
        c) Click on the Create Account button.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {}  ################".format("test_create_account"))

        # a) Navigate to Create Account page
        self.create_account.navigate_to_create_account_page()

        assert self.create_account.is_on_create_account_page(), \
            "Failed to navigate to Create Account page"

        # b) Enter details for all fields
        # c) Click Create Account button
        self.create_account.fill_and_submit_create_account_form(
            first_name="QA",
            last_name="Automation",
            email=generate_test_email(),
            password="TestPass@1234!",
            company_name="Test Company",
            address1="123 Test St",
            address2="Suite 100"
        )

        time.sleep(5)  # Wait for potential page load after form submission

        logging.info("Create Account button clicked successfully")