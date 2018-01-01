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

    def tr_send_post(self, api_param, dict_data=None):
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

    def tr_post_test_result(self, test_id, test_result, comment=None, elapsed="0s", version=None, defects=None,
                            assigned_to_id=None):
        """
        This method will post the result of a test case to the TestRail.
        :param test_id: Testcase id starts with TXXXX eg ( T31)
        :param test_result: pass, fail, retest, untested, blocked
        :param comment: pass or failure reason or observations
        :param elapsed: time to test.  specify like 10s, 10m or xxs/m/h
        :param version: software version
        :param defects: defect id
        :param assigned_to_id: test assigned to tester
        :return: ret_status : Boolean
                 ret_msg : return message from the API
        """
        test_result = Def.TR_DICT_RESULT[test_result.lower()]

        optional_params = {Def.TR_TC_FIELD_STATUS_ID: test_result, Def.TR_TC_FIELD_COMMENT: comment,
                           Def.TR_TC_FIELD_ELAPSED: elapsed, Def.TR_TC_FIELD_VERSION: version,
                           Def.TR_TC_FIELD_DEFECTS: defects, Def.TR_TC_FIELD_ASSIGNED_TO_ID: assigned_to_id}
        try:
            ret_msg = self.tr_send_post([Def.TR_API_ADD_RESULT, str(test_id)], optional_params)
            ret_status = True
        except Exception as e:
            ret_msg = "Error in posting results to the dashboard for test_id:" \
                      " {}\nError Message = {}".format(test_id, e.message)
            ret_status = False
        return ret_status, ret_msg

    def get_list_of_runid_for_plan(self, plan_id):
        """
        This method will get all the runid for a test plan
        :param plan_id: plan id
        :return: ret_val: Boolean
                 ret_msg: return a list of run ids for the plan or empty list
        """
        runid_list = []
        ret_val, ret_msg = self.tr_send_get(Def.TR_API_GET_PLAN, [plan_id])
        if Def.TR_ERROR_CALLING_API in ret_msg:
            ret_val = False
            ret_msg = []
        else:
            tmp_list = ret_msg[Def.TR_TEST_PLAN_ENTRIES]
            for plan_list in tmp_list:
                run = plan_list[Def.TR_KEY_RUNS]
                runid_list.append(run[0][Def.TR_KEY_ID])
            ret_msg = runid_list
        return ret_val, ret_msg

    def get_list_of_tests_for_run(self, run_id):
        """
        This method will get the list of tests for a run id
        :param run_id: run id
        :return: ret_val : Boolean
                 ret_msg : list of test for a plan id

        """
        ret_val, ret_msg = self.tr_send_get(Def.TR_API_GET_TESTS, [run_id])
        if Def.TR_ERROR_CALLING_API in ret_msg:
            ret_msg = []
            ret_val = False
        else:
            ret_val = True
        return ret_val, ret_msg


# Unit testing the helper library
class TestTRHelper:
    @classmethod
    def setup_class(cls):
        # Using the parser extract the credentials
        cls.con_par = Cp.MyParser("..\config.ini")
        server_ip = cls.con_par.retrive_value(Def.CFG_SERVER_CONFIG, Def.CFG_SERVER_URL)
        uid = cls.con_par.retrive_value(Def.CFG_SERVER_CONFIG, Def.CFG_USER_ID)
        u_pass = cls.con_par.retrive_value(Def.CFG_SERVER_CONFIG, Def.CFG_USER_PASSWD)
        cls.tr = TestRailHelper(server_ip, uid, u_pass)

    # Test for retriving all test for a run
    def test_get_tests(self):
        run_id = 3  # This test plan has three run ids
        ret_val, tmp_list = self.tr.get_list_of_runid_for_plan(run_id)
        for itm in tmp_list:
            print ("\nRun id = {}\n".format(itm))
            ret_val, ret_msg = self.tr.get_list_of_tests_for_run(itm)
            assert ret_val is True, "Error in retrieving test cases"
            print (ret_msg)
        print tmp_list

    # Test for getting all runid Positive test case
    def test_get_runid_positive(self):
        run_id = 3
        ret_val, ret_msg = self.tr.get_list_of_runid_for_plan(run_id)
        print ret_msg
        assert ret_val is True, "Error in getting the run id"

    # Test for getting all runid negative test case
    def test_get_runid_negative(self):
        run_id = 4  # This is an invalid run_id
        ret_val, ret_msg = self.tr.get_list_of_runid_for_plan(run_id)
        print ret_msg
        assert ret_val is False, "Error in getting the run_id"

    # Test for posting result
    def test_post_result_for_testcase(self):
        ret, ret_val = self.tr.tr_post_test_result(31, "Fail", "Failed executing test", "10s")
        print (ret_val)
        assert ret is True, "Error in posting result"

    # Test for get method
    def test_method_get_1(self):
        test_case_id = "1"  # case id in the testrail
        ret, value = self.tr.tr_send_get(Def.TR_API_GET_CASES, [test_case_id])
        print (value)
        assert ret is True, "Failed get method"

    # Test for get method for multiple input params
    def test_method_get_2(self):
        test_case_id = 2
        test_run_id = 4
        ret, ret_val = self.tr.tr_send_get(
            Def.TR_API_GET_RESULTS_FOR_CASE, [test_run_id, test_case_id])
        print (ret_val)
        assert ret is True, "Error in getting the results for test case"

    # Test for post method
    def test_method_post_1(self):
        ret, ret_msg = self.tr.tr_send_post(
            [Def.TR_API_ADD_RESULT_FOR_CASE, 4, "2"],
            {'status_id': 1, 'comment': 'This test worked fine!'})
        print (ret_msg)
        assert ret is True, "Failed to update the test case"
