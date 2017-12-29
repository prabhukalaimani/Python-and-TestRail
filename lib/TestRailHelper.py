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
        """
        This is a wrapper method for calling the API using post method.
        This uses api params which is a list and dict_data which is a
        dictionary object based on the API
        :param api_param: parameters that is passed with the API
        :param dict_data: dictionary of optional parameters
        :return: ret_status, ret_msg
                 ret_status : Boolean ( True or False)
                 ret_msg : message from the API call
        """
        tmp_string = ""
        param_string = ""
        for itm in api_param:
            tmp_string = tmp_string + str(itm) + "/"
        # Remove the last / from the string
        param_string = tmp_string[:-1]
        try:
            ret_msg = self.trclient.send_post(param_string, dict_data)
            ret_status = True
        except Exception as e:
            ret_msg = "Error in calling Post method for API {}\\n Error Message = {} ".format(param_string, e.message)
            ret_status = False
        return ret_status, ret_msg

    def tr_send_get(self, api_string, data_list):
        """
        This is a wrapper method for send_get. The input parameters are sent
        as list.The list data are formatted and then passed on to the
        Api method.
        :param api_string: API to be called using the get method
        :param data_list: list of input parameters
        :return: ret_status, ret_msg
                 ret_status : Boolean ( True or False)
                 ret_msg : message from the API call
        """
        param_string = ""
        tmp_string = ""
        # format the input parameters from the list
        for itm in data_list:
            tmp_string = tmp_string + str(itm) + "/"
        # Remove the last '/' from the string
        param_string = tmp_string[:-1]
        # call the get method
        try:
            ret_msg = self.trclient.send_get(api_string + "/" + param_string)
            ret_status = True
        except Exception as e:
            ret_msg = "Error in calling get method for API {}\\n Eroor Message = {} ".format(api_string, e.message)
            ret_status = False
        return ret_status, ret_msg


    def post_result(self, test_id, test_result, comment="", elapsed="0s", version="", defects="", assignedto_id=""):
        """
        This method will post the result to the TestRail.
        :param test_id: Testcase id starts with TXXXX eg ( T31)
        :param test_result: pass, fail, retest, untested, blocked
        :param comment: pass or failure reason or observations
        :param elapsed: time to test.  specify like 10s, 10m or xxs/m/h
        :param version: software version
        :param defects: defect id
        :param assignedto_id: test assigned to tester
        :return: ret_status : Boolean
                 ret_msg : return message from the API
        """
        optional_params = {}
        test_result = Def.TR_DICT_RESULT[test_result.lower()]

        optional_params = {'status_id': test_result, 'comment': comment,
                           'elapsed': elapsed, 'version': version,
                           'defects': defects, 'assignedto_id': assignedto_id }
        try:
            ret_msg = self.tr_send_post([Def.TR_API_ADD_RESULT, str(test_id)], optional_params)
            ret_status = True
        except Exception as e:
            ret_msg = "Error in posting results to the dashboard for test_id: {}\nError Message = {}".format(test_id, e.message)
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

    # Test for posting result
    def test_post_result_for_testcase(self):
        ret, ret_val = self.tr.post_result(31,"Fail","Failed executing test", "10s")
        print (ret_val)
        assert ret is True, "Error in posting result"

    # Test for get method
    def test_method_get_1(self):
        test_case_id = "1" # case id in the testrail
        ret, value = self.tr.tr_send_get(Def.TR_API_GET_CASES, [test_case_id])
        print (value)
        assert ret is True, "Failed get method"

    # Test for get method for multiple input params
    def test_method_get_2(self):
        test_case_id = 2
        test_run_id = 4
        ret, ret_val = self.tr.tr_send_get(Def.TR_API_GET_RESULTS_FOR_CASE, [test_run_id, test_case_id])
        print (ret_val)
        assert ret is True, "Error in getting the results for test case"

    # Test for post method
    def test_method_post_1(self):
        ret, ret_msg = self.tr.tr_send_post( [Def.TR_API_ADD_RESULT_FOR_CASE, 4, "2"] , { 'status_id': 1, 'comment': 'This test worked fine!' })
        print (ret_msg)
        assert ret is True, "Failed to update the test case"


