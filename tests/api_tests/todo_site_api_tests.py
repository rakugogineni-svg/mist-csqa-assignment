import pytest
import logging
from libs.api_libs.org_api_libs import OrgAPILibs
from libs.api_libs.todo_site_api_libs import SiteAPILibs

org_obj = OrgAPILibs()
site_obj = SiteAPILibs()


class TestSiteAPI():

    org_id = ""   # Class variable for Org ID
    site_id = ""  # Class variable for Site ID

    @pytest.fixture(scope="class", autouse=True)
    def setup_org(self, env):
        """
        Creates a temporary Org before the tests run and deletes it after.
        Sites require an Org to live under.
        """
        org = org_obj._op_create_org(env)
        TestSiteAPI.org_id = org['id']
        logging.info("TestSiteAPI :: setup_org :: Created Org with ID {}".format(TestSiteAPI.org_id))

        yield

        org_obj._op_delete_org(env, TestSiteAPI.org_id)
        logging.info("TestSiteAPI :: setup_org :: Deleted Org with ID {}".format(TestSiteAPI.org_id))

    def test_01_create_site(self, env):
        """
        Test to create a Site with a randomly generated name and validate the response.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {}  ################".format("test_01_create_site"))

        created_site = site_obj._op_create_site(env, TestSiteAPI.org_id)
        TestSiteAPI.site_id = created_site['id']

        assert site_obj._is_site_present(env, TestSiteAPI.site_id)

    def test_02_update_site(self, env):
        """
        Test to update the Site name to a different randomly generated name.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {}  ################".format("test_02_update_site"))

        site_payload = {"name": site_obj.create_random_site_name()}
        updated_site = site_obj._op_update_site(env, TestSiteAPI.site_id, site_payload)

        assert updated_site['name'] == site_payload['name']

    def test_03_delete_site(self, env):
        """
        Test to delete the Site and verify it no longer exists.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {}  ################".format("test_03_delete_site"))

        site_obj._op_delete_site(env, TestSiteAPI.site_id)

        assert not site_obj._is_site_present(env, TestSiteAPI.site_id)