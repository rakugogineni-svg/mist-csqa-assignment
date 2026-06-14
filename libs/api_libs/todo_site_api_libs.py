import logging
import json
import os
from datetime import datetime
from libs.api_libs.constants import api_constants
from utils.api_utils.api_utils import CommonAPIUtils


class GenericSiteLibs(object):

    def create_random_site_name(self):
        return "Automation Site " + str(datetime.now())[0:16]

    def get_sample_site_config(self):
        site_config_file = os.path.abspath(__file__ + "/../") + "/configs/sample_site_config.json"
        with open(site_config_file) as site_default_payload:
            data = json.load(site_default_payload)
        return data


class SiteAPILibs(GenericSiteLibs):

    def __init__(self):
        pass

    def _op_create_site(self, env, org_id, site_payload=None):
        logging.info("{} :: {} :: Trying to create a Site".format(
            self.__class__.__name__, self.__class__._op_create_site.__name__))
        url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_ORG_SITES.format(org_id)
        create_site_data = super(SiteAPILibs, self).get_sample_site_config()
        if site_payload is not None:
            create_site_data.update(site_payload)
        else:
            create_site_data['name'] = super(SiteAPILibs, self).create_random_site_name()
        response = CommonAPIUtils().post_request_with_status_code_validation(url, create_site_data, 200)
        return response

    def _op_update_site(self, env, site_id, site_payload):
        logging.info("{} :: {} :: Trying to update a Site".format(
            self.__class__.__name__, self.__class__._op_update_site.__name__))
        url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_SITE_DETAILS.format(site_id)
        response = CommonAPIUtils().put_request_with_status_code_validation(url, site_payload, 200)
        return response

    def _op_delete_site(self, env, site_id):
        logging.info("{} :: {} :: Trying to delete a Site".format(
            self.__class__.__name__, self.__class__._op_delete_site.__name__))
        url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_SITE_DETAILS.format(site_id)
        CommonAPIUtils().delete_request_with_status_code_validation(url, 200)

    def _op_get_site(self, env, site_id):
        url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_SITE_DETAILS.format(site_id)
        try:
            return CommonAPIUtils().get_request_with_status_code_validation(url, 200)
        except AssertionError:
            return None

    def _is_site_present(self, env, site_id):
        site = self._op_get_site(env, site_id)
        if site and 'id' in site:
            return True
        return False