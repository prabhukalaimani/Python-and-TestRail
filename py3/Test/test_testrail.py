import os
import TestRailLib as TestRail
import trDefines as Defines

class TestTestRail:
    def setup(self):
        user_id = "XXXX"
        password = "XXXXX"
        self.tr = TestRail.TestRailLib("https://XXXXXXX", user_id, password)

    def test_get_test_cases(self):
        #suite_revel = 1913
        suite_common = 1709
        #suite_gy = 1711
        res, ret_dict = self.tr.tr_get_test_cases(suite_common, [Defines.TR_TC_TITLE, Defines.TR_TC_CREATED_BY])
        assert res
        tmp = self.tr.count_values_in_sub_dict(ret_dict)
        total = 0
        for tmp_key, tmp_value in tmp.items():
            total += tmp_value
        print("\nTotal Test cases = {}".format(total))

    # Test case for updating the test results of a test case
    def test_pass(self):
        tp = 16408
        cid = 1819009
        status, ret_msg = self.tr.tr_add_test_case_result(tp, cid, 1)
        assert status
        assert ret_msg[Defines.TR_TC_STATUS_ID] == 1

    def test_fail(self):
        tp = 16408
        cid = 1819010
        status, ret_msg = self.tr.tr_add_test_case_result(tp, cid, 5)
        assert status
        assert ret_msg[Defines.TR_TC_STATUS_ID] == 5

    def test_retest(self):
        tp = 16408
        cid = 1819010
        status, ret_msg = self.tr.tr_add_test_case_result(tp, cid, 4)
        assert status
        assert ret_msg[Defines.TR_TC_STATUS_ID] == 4

    def test_not_implemented(self):
        tp = 16407
        cid = 1857627
        status, ret_msg = self.tr.tr_add_test_case_result(tp, cid, 6)
        assert status
        assert ret_msg[Defines.TR_TC_STATUS_ID] == 6

    def test_not_testable(self):
        tp = 16410
        cid = 1870037
        status, ret_msg = self.tr.tr_add_test_case_result(tp, cid, 7)
        assert status
        assert ret_msg[Defines.TR_TC_STATUS_ID] == 7

    def test_not_blocked(self):
        tp = 16409
        cid = 1819010
        status, ret_msg = self.tr.tr_add_test_case_result(tp, cid, 2)
        assert status
        assert ret_msg[Defines.TR_TC_STATUS_ID] == 2

    # Test Cases for getting the test case in a test plan
    def test_testcase_1(self):
        test_plan = 16405
        status, auto, manual = self.tr.tr_get_testcase_in_test_plan(test_plan, extract_list=[Defines.TR_TC_TITLE, Defines.TR_TC_ID])
        assert status

    def test_testcase_negative(self):
        test_plan = 123
        status, auto, manual = self.tr.tr_get_testcase_in_test_plan(test_plan,
                                                                    extract_list=[Defines.TR_TC_TITLE, Defines.TR_TC_ID])
        assert status == False

    # Test Case for getting the test suite info in a test plan
    def test_test_suite(self):
        test_plan = 16405
        status, ret_list = self.tr.tr_get_testsuite_info_in_test_plan(test_plan)
        assert status

    def test_test_suite_negative(self):
        test_plan = 123
        status, ret_list = self.tr.tr_get_testsuite_info_in_test_plan(test_plan)
        assert status == False

    def test_suite_in_proj(self):
        status, ret_msg = self.tr.tr_get_tc_suites_in_project(extract_list=[Defines.TR_TS_DESCRIPTION, Defines.TR_TS_NAME])
        assert status

    # Test Cases for getting the test plan results. Scenarios: 1. Automated, 2. Manual 3. Automated and Manual
    def test_testresults_auto(self):
        test_plan = 15968
        status, manual_tc, automated_tc = self.tr.get_test_plan_results(test_plan, automated=Defines.TR_ALL_TC)
        tp_stats = Defines.TR_TC_RESULTS_DICT.copy()
        print("Automated = {}".format(manual_tc))
        assert status == True
        assert automated_tc[Defines.TC_TOTAL] > 0
        assert manual_tc[Defines.TC_TOTAL] > 0
        for res_item in manual_tc:
            tp_stats[res_item] += manual_tc[res_item]
        for res_item in automated_tc:
            tp_stats[res_item] += automated_tc[res_item]
        print(tp_stats)

    def test_testresults_auto_negative(self):
        test_plan = 123
        status, manual_tc, automated_tc = self.tr.get_test_plan_results(test_plan, automated=Defines.TR_AUTOMATED_TC)
        print("Automated = {}".format(automated_tc))
        assert status == False
        assert automated_tc == Defines.TR_TC_RESULTS_DICT

    def test_testresults_manual(self):
        test_plan = 16405
        status, manual_tc, automated_tc = self.tr.get_test_plan_results(test_plan, automated=Defines.TR_MANUAL_TC)
        print("Manual = {}".format(manual_tc))
        assert status == True
        assert manual_tc[Defines.TC_TOTAL] > 0

    def test_testresults_manual_negative(self):
        test_plan = 1123
        status, manual_tc, automated_tc = self.tr.get_test_plan_results(test_plan, automated=Defines.TR_MANUAL_TC)
        print("Manual = {}".format(manual_tc))
        assert status == False
        assert manual_tc== Defines.TR_TC_RESULTS_DICT

    def test_testresults_all(self):
        test_plan = 16405
        status, manual_tc, automated_tc = self.tr.get_test_plan_results(test_plan, automated=Defines.TR_ALL_TC)
        print("Manual = {} Automated = {}".format(manual_tc, automated_tc))
        assert status == True
        assert manual_tc[Defines.TC_TOTAL] > 0
        assert automated_tc[Defines.TC_TOTAL] > 0

    def test_testresults_all_negative(self):
        test_plan = 164051
        status, manual_tc, automated_tc = self.tr.get_test_plan_results(test_plan, automated=Defines.TR_ALL_TC)
        print("Manual = {} Automated = {}".format(manual_tc, automated_tc))
        assert status == False
        assert manual_tc == Defines.TR_TC_RESULTS_DICT
        assert automated_tc == Defines.TR_TC_RESULTS_DICT

    # Test for adding result for individual test using Testrun ( TXXXXX)
    def test_tr_add_result(self):
        run_id = 26235845
        status = 1
        version = "test_7.0"
        params = {Defines.TR_TC_RESULT_ELAPSED: '0', Defines.TR_TC_STATUS_ID: status, Defines.TR_TC_RESULT_VERSION: version }
        status, ret_msg = self.tr.tr_add_result(run_id,params=params)
        assert status

    # Test for setting the status of an entire test plan.
    def test_add_result_for_entire_test_plan_manual(self):
        plan_id = 16405
        status_id = 4
        status, ret_msg = self.tr.add_result_for_entire_test_plan(plan_id, status_id, automated=Defines.TR_MANUAL_TC)
        assert status
        assert ret_msg[Defines.TR_TC_STATUS_ID] == status_id

    def test_add_result_for_entire_test_plan_automated(self):
        plan_id = 16405
        status_id = 1
        status, ret_msg = self.tr.add_result_for_entire_test_plan(plan_id, status_id, automated=Defines.TR_AUTOMATED_TC)
        assert status
        assert ret_msg[Defines.TR_TC_STATUS_ID] == status_id

    def test_add_result_for_entire_test_plan_all(self):
        plan_id = 16405
        status_id = 1
        status, ret_msg = self.tr.add_result_for_entire_test_plan(plan_id, status_id, automated=Defines.TR_ALL_TC)
        assert status
        assert ret_msg[Defines.TR_TC_STATUS_ID] == status_id