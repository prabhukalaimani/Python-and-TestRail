#!/usr/bin/python
# -*- coding  utf-8 -*-
# Author: Prabhu Kalaimani
# These are the defines used by TestRail API's

# Generic defines
# Project id ( Use only the integer value from TestRail )
TR_PROJ_ID = XXX
TR_CURRENT_PROJECT = TR_PROJ_ID_OTG
DICT_SIMPLE = "simple_dict"
DICT_SUB = "sub_dict"

# Test Rail API methods
# Project API
TR_API_GET_PROJ = 'get_project'
# Test Plan API
TR_API_GET_PLANS = 'get_plans'
TR_API_GET_PLAN = "get_plan"

# Test API
TR_TESTS_GET_TESTS = "get_tests"

# Test Case API
TR_API_GET_CASES = 'get_cases'
TR_API_GET_CASE = 'get_case'
# Test Suites API
TR_API_GET_SUITES = 'get_suites'
# Test Case Results
TR_API_ADD_RESULT_FOR_CASES = 'add_result_for_case'
TR_API_ADD_RESULTS_FOR_CASES = 'add_results_for_cases'
TR_API_ADD_RESULT = 'add_result'

# Test case Fields: These are defines used in the test case fields of TestRail
TR_TC_ID = 'id'
TR_TC_TITLE = 'title'
TR_TC_SECTION_ID = 'section_id'
TR_TC_TEMPLATE_ID = 'template_id'
TR_TC_TYPE_ID = 'type_id'
TR_TC_PRIORITY_ID = 'priority_id'
TR_TC_MILESTONE_ID = 'milestone_id'
TR_TC_REFS = 'refs'
TR_TC_CREATED_BY = 'created_by'
TR_TC_CREATED_ON = 'created_on'
TR_TC_UPDATED_BY = 'updated_by'
TC_TC_UPDATED_ON = 'updated_on'
TC_TC_ESTIMATE = 'estimate'
TR_TC_ESTIMATE_FORECAST = 'estimate_forecast'
TR_TC_SUITE_ID = 'suite_id'
TR_TC_CUSTOM_AUTOMATION_TYPE = 'custom_automation_type'
TR_TC_CUSTOM_AUTOMATED = 'custom_automated'
TR_TC_CUSTOM_EDIT_STAGE = 'custom_edit_stage'
TR_TC_CUSTOM_UIDD_REQUIREMENT = 'custom_uidd_requirement'
TR_TC_CUSTOM_FEATURE = 'custom_feature'
TR_TC_CUSTOM_TEST_DESCRIPTION = 'custom_test_description'
TR_TC_CUSTOM_STEPS_SEPARATED = 'custom_steps_separated'

# Results
TR_TC_STATUS_ID = 'status_id'
TR_TC_CASE_ID = 'case_id'
TR_MANUAL_TC = 'manual_tc'
TR_AUTOMATED_TC = 'automated_tc'
TR_ALL_TC = 'all'
TC_TOTAL = 'total'
TR_TC_RESULT_COMMENT = 'comment'
TR_TC_RESULT_ELAPSED = 'elapsed'
TR_TC_RESULT_DEFAULT_EXEC_TIME = '2s'
TR_TC_RESULT_VERSION = 'version'
TR_TC_RESULT_DEFECTS = 'defects'

# Test case status and the enum value from test rail.
# This can deffer from project to project. Make sure this is updated properly
TR_TC_PASSED = 'passed'
TR_TC_FAILED = 'failed'
TR_TC_BLOCKED = 'blocked'
TR_TC_RETEST = 'retest'
TR_TC_NOT_IMPLEMENTED = 'not_implemented'
TR_TC_NOT_TESTABLE = 'not_testable'
TR_TC_RESULT_UNTESTED = 'Untested'

# TestRail result dict. Make sure this is also updated properly
TR_TC_STATUS_DICT = {1: TR_TC_PASSED, 2: TR_TC_BLOCKED, 3: TR_TC_RESULT_UNTESTED, 4: TR_TC_RETEST, 5: TR_TC_FAILED, 6: TR_TC_NOT_IMPLEMENTED, 7: TR_TC_NOT_TESTABLE}
TR_TC_RESULTS_DICT = {TR_TC_PASSED: 0, TR_TC_FAILED: 0, TR_TC_BLOCKED: 0, TR_TC_RETEST: 0, TR_TC_NOT_IMPLEMENTED: 0, TR_TC_NOT_TESTABLE:0, TR_TC_RESULT_UNTESTED: 0, TC_TOTAL: 0}

# Test plan fields
TR_TP_ID ='id'
TR_TP_NAME = 'name'
TR_TP_DESCRIPTION = 'description'
TR_TP_MILESTONE_ID = 'milestone_id'
TR_TP_ASSIGNEDTO_ID = 'assignedto_id'
TR_TP_IS_COMPLETED = 'is_completed'
TR_TP_COMPLETED_ON = 'completed_on'
TR_TP_PASSED_COUNT = 'passed_count'
TR_TP_BLOCKED_COUNT = 'blocked_count'
TR_TP_UNTESTED_COUNT = 'untested_count'
TR_TP_RESTEST_COUNT = 'retest_count'
TR_TP_FAILED_COUNT = 'failed_count'
TR_TP_PROJECT_ID = 'project_id'
TR_TP_CREATED_ON = 'created_on'
TR_TP_CREATED_BY = 'created_by'
TR_TP_URL = 'url'
TR_TP_ENTRIES = "entries"
# TestRun
TR_TP_RUNS = "runs"
TR_RUN_ID = "id"
TR_TP_TR_CONFIG = "config"
TR_TP_TR_CONFIG_IDS = "config_ids"
TR_TP_SUITE_ID = "suite_id"


# Test suite ID
TR_TS_ID = 'id'
TR_TS_NAME = 'name'
TR_TS_DESCRIPTION = 'description'
TR_TS_PROJECT_ID = 'project_id'
TR_TS_IS_MASTER = 'is_master'
TR_TS_IS_BASELINE = 'is_baseline'
TR_TS_IS_COMPLETED = "is_completed"
TR_TS_COMPLETED_ON = "completed_on"
TR_TS_URL = "url"
TR_TS_SUITE_ID = "suite_id"
TR_TS_SECTION_ID = "section_id"


