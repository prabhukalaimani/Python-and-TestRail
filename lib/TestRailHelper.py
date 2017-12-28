# -*- coding: utf-8 -*-
##############################################################################
# ஆசிரியர்  : பிரபு கலைமணி
# பயன்பாடு : இந்த கோப்பு
# http://docs.gurock.com/testrail-api2/start
# FileName :
# usage : This file will read the config.ini file and will return the key
# Date : 12/14/2017
##############################################################################
from testrail import *
import Defines as Def
import ConfigParser as Cp


class TestRailHelper:
    def __init__(self, server_url, server_user, server_password):
        try:
            self.trclient = APIClient(server_url)
            self.trclient.user = server_user
            self.trclient.password = server_password
        except (KeyError, IOError):
            raise IOError("TestRail not configured properly..Please check the credentials")

    def tr_send_post(self, api_param, dict_data={}):
        tmp_string = ""
        param_string = ""
        for itm in api_param:
            tmp_string = tmp_string + itm + "/"
        # Remove the last / from the string
        param_string = tmp_string[:-1]
        try:
            ret_msg = self.trclient.send_post(param_string, dict_data)
            ret_status = True
        except Exception as e:
            ret_msg = "Error in calling Post method for API {}\\n Error Message = {} ".format(param_string, e.message)
            ret_status = False
        return ret_status, ret_msg

    def tr_send_get(self, api_string, data):
        """
        This is will call the api using get method
        :param api_string: api name
        :param data: optional parameters
        :return:
        """
        param_data = api_string + "/" + str(data)
        try:
            ret_msg = self.trclient.send_get(param_data)
            ret_status = True
        except Exception as e:
            ret_msg = "Error in calling get method for API {}\\n Eroor Message = {} ".format(api_string, e.message)
            ret_status = False
        return ret_status, ret_msg

# Unit testing the helper library
class TestTRHelper:
    @classmethod
    def setup_class(cls):
        # Using the parser extract the credentials
        cls.con_par = Cp.MyParser("..\config.ini")
        server_ip = cls.con_par.retrive_value(Def.CFG_SERVER_CONFIG, Def.CFG_SERVER_URL )
        uid = cls.con_par.retrive_value(Def.CFG_SERVER_CONFIG, Def.CFG_USER_ID )
        u_pass = cls.con_par.retrive_value(Def.CFG_SERVER_CONFIG, Def.CFG_USER_PASSWD )
        cls.tr = TestRailHelper("https://tigers.testrail.io", "guest@tigers.com", 12345)

    # Test for get method
    def test_method_get(self):
        test_case_id = 1 # case id in the testrail
        ret, value = self.tr.tr_send_get(Def.TR_API_GET_CASES, test_case_id)
        print value
        assert ret is True, "Failed get method"

    # Test for post method
    def test_method_post(self):
        runid = "1"
        caseid = "1"
        status_id = 1  # pass
        comment = "Test passed"
        ret, ret_msg = self.tr.tr_send_post( [Def.TR_API_ADD_RESULT_FOR_CASE, "4", "2"] , { 'status_id': 1, 'comment': 'This test worked fine!' })
        print ret_msg
        assert ret is True, "Failed to update the test case"


