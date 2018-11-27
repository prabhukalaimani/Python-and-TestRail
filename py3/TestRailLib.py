#!/usr/bin/python
"""
Author: Prabhu Kalaimani
Purpose:
The purpose of the library is to use the api's provided by TestRail.
This utility is developed using python 3 environment.
Note: We need the Testrail binding methods which can be downloaded from
from https://github.com/gurock/testrail-api
"""

from testrail import APIClient, APIError
import urllib.error as err
import trDefines as Defines
import logging
import logging.config
import os


class TestRailLib:
    """
    This class contains methods for accessing TestRail API's.
    For more information : https://www.gurock.com/testrail
    """
    def __init__(self, tr_server, user_name, password):
        """
        This method will initialize the TestRail server using the user name and password provided
        :param tr_server: Name of the Test Rail server
        :param user_name: TestRail user id
        :param password:  TestRail password
        """
        file_dir = os.path.split(os.path.realpath(__file__))[0]
        logging.config.fileConfig(os.path.join(file_dir, "trlogger.ini"))
        # Configure the logger
        self._log = logging.getLogger('testrail')
        self._log.info("Starting TestRail application ")

        # TestRail Connection status
        # Note: This variable is used to ensure we have a valid TestRail Instance
        self._connection_status = False
        try:
            # Check if the URL is valid
            self._client = APIClient(tr_server)
            self._client.password = password
            self._client.user = user_name
            self._connection_status = True
            # Check if the url, user name and password is set correctly by accessing an API
            self._client.send_get(Defines.TR_API_GET_PROJ + "/" + str(Defines.TR_PROJ_ID_OTG))
            self._log.info("Connected to TestRail server {} with user-id {}".format(tr_server, user_name))
        except err.URLError:
            self._log.exception("Url: {} is not valid".format(tr_server))
            raise err.URLError("Error: Please check the URL")
        except APIError:
            self._log.critical(
                "User-id or Password is not correct. Failed to connect with TestRail url: {}".format(tr_server))
            raise APIError("Error: Please check user id and password")

    def __extract_dictionary(self, src_dict, extract_list, dict_type=Defines.DICT_SUB, ret_dict_key=Defines.TR_TP_ID):
        """
        This method will extract and create a new dictionary based on the attributes passed.
        The extraction can be done on a single plain dictionary or dictionary within a dictionary.
        Note: The ret_dict_key must be an unique identifier as its the ret_dict key.
        :param src_dict: Source dictionary
        :param extract_list:  List of keys to be extracted
        :param dict_type: This parameter determines if we need to extract values from simple dictionary
        or sub dictionaries
        :param ret_dict_key:  Key that must be used for return dictionary
        :return: List of dictionary with ret_dict_key as key.
        Example output ret_dict = { 1:{'description':'Example 1'} , 2: {'description': 'Example 2} }
        """
        if extract_list:
            # Extracting list containing dictionary of dictionary ( sub dictionary)
            # Example [ 1:{'description':'Example 1'} , 2: {'description': 'Example 2} ]
            if dict_type in Defines.DICT_SUB:
                ret_dict = []
                # This code applies on sub dictionary
                for src_key in src_dict:
                    tmp_list = {}
                    for extract_key in extract_list:
                        # Check if the key is present in source dictionary ( dictionary of dictionary)
                        if extract_key in src_key:
                            tmp_list[extract_key] = src_key[extract_key]
                        else:
                            self._log.info(
                                "{} is invalid key or not present in the source dictionary".format(extract_key))
                    # update the return dictionary with key as the plan id
                    if dict_type in Defines.DICT_SUB:
                        ret_dict.append({src_key[ret_dict_key]: tmp_list})
                    else:
                        ret_dict.append(tmp_list)
            else:
                # Extracting items from Plain dictionary
                # In simple scenario it will return a dictionary not a list
                ret_dict = {}
                for extract_key in extract_list:
                    if extract_key in src_dict:
                        ret_dict[extract_key] = src_dict[extract_key]
        else:
            self._log.debug("Nothing to extract. All items will be returned")
            ret_dict = src_dict
        return ret_dict

    def count_values_in_sub_dict(self, dict_list, grp_item_key):
        """
        This method will group and count the keys of a sub dictionary
        See the example in the doc string for output
        :param dict_list: Input dictionary
        :param grp_item_key: key which needs to be grouped
        :return: count of the values in the sub dictionary
        Example : [ A:{color:'a'}, B:{color:'b'}, C:{color:'a'}, D:{color:'a'}]
        output: {a:3, b1}
        """
        ret_dict = {}
        cnt = 1
        try:
            for list_items in dict_list:
                for key, value in list_items.items():
                    if value[grp_item_key] in ret_dict:
                        ret_dict[value[grp_item_key]] = ret_dict[value[grp_item_key]] + 1
                    else:
                        ret_dict[value[grp_item_key]] = cnt
        except KeyError:
            self._log.exception("KeyError Exception for key ")
        return ret_dict

    def tr_api_post(self, api, params):
        """
        This method is a wrapper method to call the POST methods of TestRail
        :param api:  Test Rail API
        :param params: Post parameters for the Test Rail API.
        :return: True, message or False, Message
                 True with and the return message will vary depending on
                 the api requested
                 False with and the return message will be the exception caught
        """
        status = False
        try:
            return_msg = self._client.send_post(api, params)
            status = True
            self._log.info("Successfully sent data using POST method. API = {} Data = {}".format(api, params))
        except APIError as e:
            self._log.exception("API Exception for api POST {} - Exception: {}".format(api, e))
            return_msg = e
        return status, return_msg

    def tr_api_get(self, api, params):
        """
        This method is a wrapper method to call the GET methods of TestRail
        apends the TestRail API and the parameters.
        :param api: TestRail api to be called ( Example: get_case)
        :param params: The GET parameters for  API Methods
        :return: True, message or False, Message
                 True with and the return message will vary depending on
                 the api requested
                 False with and the return message will be the exception caught
        """
        status = False
        try:
            return_msg = self._client.send_get(api+"/"+str(params))
            status = True
            self._log.info("Successfully sent data using GET method. API = {} Data = {}".format(api, params))
        except APIError as e:
            self._log.exception("API Exception for api GET {} - Exception: {}".format(api, e))
            return_msg = e
        return status, return_msg

    # Methods for TestRail Test Plans
    def tr_get_all_plans(self, project_id, project_fields):
        """
        This method will extract all the plans for a project. We can specify what attribute of TestRail project
        We want to extract using project_fields.
        :param project_id: Project id ( Example 1)
        :param project_fields: This is a list of fields needed for project
         Example: project passed count, failed count etc
        :return: status( Boolean) and ret_list : list of Plans with attributes from project_fields
        """
        ret_dict = None
        status, ret_list = self.tr_api_get(Defines.TR_API_GET_PLANS, project_id)
        if status:
            ret_dict = self.__extract_dictionary(ret_list, project_fields)
        return status, ret_dict

    def tr_get_tc_suites_in_project(self, project_id=Defines.TR_CURRENT_PROJECT, extract_list=None):
        """
        This method will get the suites available in the TestRail project
        :param project_id: Project id
        :param extract_list: The attribute required to be extracted from test suites
        :return: Dictionary of project test suites with the attributes mentioned in extract_list
        """
        # If the extract list is none at least extract the description
        if extract_list is None:
            extract_list = [Defines.TR_TS_DESCRIPTION]

        ret_dict = {}
        ret_status, suite_list = self.tr_api_get(Defines.TR_API_GET_SUITES, project_id)
        if ret_status:
            ret_dict = self.__extract_dictionary(suite_list, extract_list, ret_dict_key=Defines.TR_TS_ID)
        else:
            self._log.error("Error in getting test suites")
        return ret_status, ret_dict

    def tr_get_tescase_in_run(self, run_id, extract_list=None):
        """
        This method will extract all the test for a run. You can pass what you want to extract using extract_list.
        :param run_id: Test run id
        :param extract_list: attributes that needs to be extracted
        :return: list of dictionaries containing the test case information
        """
        ret_list = []
        # if the extract list is None. Extract the Description and automated fields
        if extract_list is None:
            extract_list = [Defines.TR_TC_CUSTOM_TEST_DESCRIPTION, Defines.TR_TC_CUSTOM_AUTOMATED]
        status, tc_list = self.tr_api_get(Defines.TR_TESTS_GET_TESTS, run_id)
        if status:
            # For each test extract the required elements
            for tst in tc_list:
                ret_list.append(self.__extract_dictionary(tst, extract_list, dict_type=Defines.DICT_SIMPLE))
            self._log.info("Extracted test cases successfully from run {}".format(run_id))
        else:
            self._log.error("Error in extracting the test cases for run {}".format(run_id))
        return status, ret_list

    def tr_get_test_cases(self, suite_id, extract_list=None):
        """
        This method will get all the test cases of a suite. A suite in TestRail contains collection of
        test cases
        :param suite_id: suite id from TestRail
        :param extract_list: attribuites needed to extract for each test case. Use the TR_TC_XXXX attributes
        :return: Status , dictionary of test cases available for the suite
        """
        ret_dict = {}
        # if the extract list is none extract the description and created by fields
        if extract_list is None:
            extract_list = [Defines.TR_TC_CUSTOM_TEST_DESCRIPTION, Defines.TR_TC_CREATED_BY]
        qry_str = str(Defines.TR_CURRENT_PROJECT) + "&" + Defines.TR_TS_SUITE_ID + "=" + str(suite_id)
        status, ret_list = self.tr_api_get(Defines.TR_API_GET_CASES, qry_str)
        if status:
            ret_dict = self.__extract_dictionary(ret_list, extract_list, ret_dict_key=Defines.TR_TC_ID)
        else:
            self._log.error("Error in getting the test case")
        return status, ret_dict

    def tr_get_test_case_info(self, tc_id, extract_list=None):
        ret_dict_list = None
        # Extract title as default value
        if extract_list is None:
            extract_list = [Defines.TR_TC_TITLE]
        status, ret_list = self.tr_api_get(Defines.TR_API_GET_CASE, tc_id)
        if status:
            ret_dict_list = self.__extract_dictionary(ret_list, extract_list, dict_type=Defines.DICT_SIMPLE,
                                                      ret_dict_key=Defines.TR_TC_ID)
        else:
            self._log.error("Error in executing API {}".format(Defines.TR_API_GET_CASE))
        return status, ret_dict_list

    def tr_get_test_plan(self, plan_id, ):
        """
        This method will get the plan in a test run.
        A run id start with RXXXX format in TestRail
        :param plan_id:
        :return:
        """
        status, ret_msg = self.tr_api_get(Defines.TR_API_GET_PLAN, plan_id)
        if not status:
            self._log.error("Error while getting the plan details for plan {}".format(plan_id))
        return status, ret_msg

    def tr_get_testsuite_info_in_test_plan(self, plan_id):
        """
        This method will get the list of test suites in a test plan. The return dictionary
        will also contain the config information of a test suite.
        :param plan_id:
        :return:
        """
        # Testplan - > Test runs -> config
        ret_dict_list = []
        # First get the test plan details. Test plan will contain test suites.
        # Test suites can have multiple Configurations
        status, ret_msg = self.tr_get_test_plan(plan_id)
        if status:
            # Get the runs of the test plan. This can be extracted using the entries field in the test plan
            tp_entries = ret_msg[Defines.TR_TP_ENTRIES]
            if tp_entries:
                # For each entries ( Test suites) get the suite information and the config information.
                # Ex: a test suite A can be tested on different configs like iOS or Android
                for entries_item in tp_entries:
                    runs = entries_item[Defines.TR_TP_RUNS]
                    for run in runs:
                        tmp = {run[Defines.TR_TS_ID]: {Defines.TR_TP_SUITE_ID: run[Defines.TR_TP_SUITE_ID],
                                                       Defines.TR_TP_TR_CONFIG: run[Defines.TR_TP_TR_CONFIG],
                                                       Defines.TR_TP_TR_CONFIG_IDS: run[Defines.TR_TP_TR_CONFIG_IDS]}}
                        ret_dict_list.append(tmp)
            else:
                # The plan has no suites. Make an entry in the logger
                self._log.error(
                    "Test plan has no test suites selected. Check and add test suites to the test plan {}".format(
                        plan_id))
        else:
            self._log.error("Error in calling tr_get_test_plan for the run_id-{}".format(plan_id))
        return status, ret_dict_list

    def tr_get_testcase_in_test_plan(self, plan_id, extract_list=None):
        """
        This method will collect the test in a test plan using the test plan id and segregates into automated
        and manual test cases.
        :param plan_id:  Test plan id
        :param extract_list: Attribute which need to be extracted
        :return: status (Boolean), automated test cases, manual test cases
        """
        automated_test_case_list = []
        manual_test_case_list = []
        # default extract list to id
        if extract_list is None:
            extract_list = [Defines.TR_TC_ID]
        status, tp_info_list = self.tr_get_testsuite_info_in_test_plan(plan_id)
        # Make sure if the automation key is present in the extract list.
        # This step is required as we need to segregate manual and automated test cases
        if Defines.TR_TC_CUSTOM_AUTOMATED not in extract_list:
            extract_list.append(Defines.TR_TC_CUSTOM_AUTOMATED)
            self._log.info("Adding {} key to the extract list".format(Defines.TR_TC_CUSTOM_AUTOMATED))
        if status:
            self._log.error("Extracted dictionary of plan {}".format(plan_id))
            for run_dic in tp_info_list:
                # For each item(suite) in test plan, extract the run-id(key) and the config params (keys)
                for run_id, tp_suite_info in run_dic.items():
                    status, tc_list = self.tr_get_tescase_in_run(run_id, extract_list)
                    for tc in tc_list:
                        if tc['custom_automated']:
                            automated_test_case_list.append(tc)
                        else:
                            manual_test_case_list.append(tc)
        else:
            self._log.error("Error in extracting information from test plan {}".format(plan_id))
        return status, automated_test_case_list, manual_test_case_list

    def get_test_plan_results(self, plan_id, automated):
        """
        This method will get all the test cases status (results) for  a test plan.
        This method will first find the runs of a test plan and then segregates the
        test to manual and automated lists
        :param plan_id: Plan id
        :param automated:
                        Define.TR_MANUAL_TC = Manual test cases
                        Defines.TR_AUTOMATED_TC = Automated test cases
                        Defines.TR_ALL_TC = Manual and automated test cases
        :return:    status ( Boolean),
                    manual_tc ( Manual test case list) ,
                    automated_tc( Automated test case list)

        """
        automated_tc = Defines.TR_TC_RESULTS_DICT.copy()
        manual_tc = Defines.TR_TC_RESULTS_DICT.copy()
        # Get all the test cases for the test plan
        # If automation is True get only automated test case
        status, automated_test_case_list, manual_test_case_list = self.tr_get_testcase_in_test_plan(plan_id, extract_list=[Defines.TR_TC_STATUS_ID])
        # Get the results based on automated flag
        if status:
            try:
                if automated in Defines.TR_MANUAL_TC or automated in Defines.TR_ALL_TC:
                    for tc in manual_test_case_list:
                        status_id = tc[Defines.TR_TC_STATUS_ID]
                        manual_tc[Defines.TR_TC_STATUS_DICT[status_id]] = manual_tc[Defines.TR_TC_STATUS_DICT[status_id]] + 1
                if automated in Defines.TR_AUTOMATED_TC or automated in Defines.TR_ALL_TC:
                    for tc in automated_test_case_list:
                        status_id = tc[Defines.TR_TC_STATUS_ID]
                        automated_tc[Defines.TR_TC_STATUS_DICT[status_id]] = automated_tc[Defines.TR_TC_STATUS_DICT[status_id]] + 1
                manual_tc[Defines.TC_TOTAL] = sum(manual_tc.values())
                automated_tc[Defines.TC_TOTAL] = sum(automated_tc.values())
            except KeyError:
                # Raise the error else the result will not match with TestRail. The missing key needs to be fixed.
                self._log.exception("Please check the TR_TC_STATUS_DICT parameters. Looks like these a mismatch with TestRail")
                raise KeyError("Please check the TR_TC_STATUS_DICT parameters. Looks like these a mismatch with TestRail")
            self._log.info("Manual test case = {}".format(manual_tc))
            self._log.info("Automated test case = {}".format(automated_tc))
        return status, manual_tc, automated_tc

    def tr_add_test_case_result(self, run_id, case_id, status_id, jir_defect=None, version=None, comments=None, elapsed=None):
        """
        This method will post result for a test case. We meed run id or the test plan and case id of the test
        to post results.
        :param run_id: (Mandatory) Run id of the test plan (Note: Suite id which starts with R example: RXXXX)
        :param case_id: (Mandatory) Case if of the test case (Note: Case id starts with C example: CXXXX)
        :param status_id: (Mandatory) One of the valid status id
        (1:pass,2:blocked,3:Untested,4:retest,5:failed,6:Not implemented,7:Not Testable)
        :param jir_defect: Any old or know jira defect for this test case
        :param version: Test code version ( firmware version)
        :param comments: Amu test comments for failure or pass
        :param elapsed: Time for the test. Default is 2 seconds
        :return: status( Boolean) , updated test case dictionary
        """
        # Set the default values
        if elapsed is None:
            elapsed = Defines.TR_TC_RESULT_DEFAULT_EXEC_TIME

        test_result = {
            Defines.TR_TC_STATUS_ID: status_id,
            Defines.TR_TC_RESULT_COMMENT: comments,
            Defines.TR_TC_RESULT_ELAPSED: elapsed,
            Defines.TR_TC_RESULT_VERSION: version,
            Defines.TR_TC_RESULT_DEFECTS: jir_defect
        }
        # Make the api string
        api_str = Defines.TR_API_ADD_RESULT_FOR_CASES + "/" + str(run_id) + "/" + str(case_id)
        self._log.info("Adding results using API string {}".format(api_str))
        # Call the API post method
        status, return_msg = self.tr_api_post(api_str, test_result)
        return status, return_msg

    def tr_add_result(self, run_id, params=None):
        """
        This method will add result to individual test run ( Starts with TXXXXX)
        :param run_id: Test case Test run id
        :param params: Parameters to set like status, comments etc
        :return: status( Boolean) and return dictionary with updates
        """
        if params is None:
            params = {Defines.TR_TC_RESULT_ELAPSED: '0', Defines.TR_TC_STATUS_ID: 5}
        api_str = Defines.TR_API_ADD_RESULT + "/" + str(run_id)
        status, return_msg = self.tr_api_post(api_str, params)
        if not status:
            self._log.error("Error in adding results for run_id {}".format(run_id))
        return status, return_msg

    def add_result_for_entire_test_plan(self, test_plan_id, status_id, automated=Defines.TR_ALL_TC, comments=None, elapsed=None, version=None):
        """
        This method will set the parameters like status, comment version etc for the entire test plan.
        You can use this function for resetting the entire plan before you start. Mostly useful in
        nightly test preparation
        """
        if elapsed is None:
            elapsed = '0'
        return_msg = None
        # Collect all the test cases of a test plan
        status, automated_test_case_list, manual_test_case_list = self.tr_get_testcase_in_test_plan(test_plan_id, extract_list=[Defines.TR_RUN_ID])

        tc_list = []
        if automated in Defines.TR_AUTOMATED_TC:
            tc_list.append(automated_test_case_list)
        elif automated in Defines.TR_MANUAL_TC:
            tc_list.append(manual_test_case_list)
        else:
            tc_list.append(manual_test_case_list)
            tc_list.append(automated_test_case_list)

        for item in tc_list:  # manual_test_case_list:
            for tc in item:
                api_str = Defines.TR_API_ADD_RESULT + "/" + str(tc[Defines.TR_RUN_ID])
                param = {
                    Defines.TR_TC_RESULT_ELAPSED: str(elapsed),
                    Defines.TR_TC_STATUS_ID: status_id,
                    Defines.TR_TC_RESULT_COMMENT: comments,
                    Defines.TR_TC_RESULT_VERSION: version
                }
                status, return_msg = self.tr_api_post(api_str, param)
        return status, return_msg
