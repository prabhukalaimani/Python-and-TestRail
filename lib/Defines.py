# -*- coding: utf-8 -*-
##############################################################################
# ஆசிரியர்  : பிரபு கலைமணி
# பயன்பாடு : இந்த கோப்பில்  குறிமுறைகாண சர மதிப்புருக்கள் இருக்கின்றது
# File Name : Defines for program
# usage : This file has all the string literals used in the code
# Date : 12/16/2017
##############################################################################


# TestRail API defines for cases ( Test Cases )
TR_API_GET_CASE = "get_case"
TR_API_GET_CASES = "get_cases"
TR_API_ADD_CASE = "add_case"
TR_API_UPDATE_CASE = "update_case"
TR_API_DELETE_CASE = "delete_case"

# TestRail API defines for case fields
TR_API_GET_CASE_FIELDS = "get_case_fields"

# TestRail API defines for case types
TR_API_GET_CASE_TYPES = "get_case_types"

# TestRail API defines for config
TR_API_GET_CONFIGS = "get_configs"
TR_API_ADD_CONFIG_GROUP = "add_config_group"
TR_API_ADD_CONFIG = "add_config"
TR_API__UPDATE_CONFIG_GROUP = "update_config_group"
TR_API_UPDATE_CONFIG = "update_config"
TR_API_DELETE_CONFIG_CONFIG = "delete_config_group"
TR_API_DELETE_CONFIG = "delete_config"

# TestRail API defines for milestone
TR_API_GET_MILESTONE = "get_milestone"
TR_API_GET_MILESTONES = "get_milestones"
TR_API_ADD_MILESTONE = "add_milestone"

TR_API_UPDATE_MILESTONE = "update_milestone"
TR_API_DELETE_MILESTONE = "delete_milestone"

# TestRail API defines for plan
TR_API_GET_PLAN = "get_plan"
TR_API_GET_PLANS = "get_plans"
TR_API_ADD_PLAN = "add_plan"
TR_API_ADD_PLAN_ENTRY = "add_plan_entry"
TR_API_UPDATE_PLAN = "update_plan"
TR_API_UPDATE_PLAN_ENTRY = "update_plan_entry"
TR_API_CLOSE_PLAN = "close_plan"
TR_API_DELETE_PLAN = "delete_plan"
TR_API_DELETE_PLAN_ENTRY = "delete_plan_entry"

# TestRail API defines for priorities
TR_API_GET_PRIORITIES = "get_priorities"

# TestRail API defines for projects
TR_API_GET_PROJECT = "get_project"
TR_API_GET_PROJECTS = "get_projects"
TR_API_ADD_PROJECT = "add_project"
TR_API_UPDATE_PROJECT = "update_project"
TR_API_DELETE_PROJECT = "delete_project"

# TestRail API defines for result
TR_API_GET_RESULTS = "get_results"
TR_API_GET_RESULTS_FOR_CASE = "get_results_for_case"
TR_API_GET_RESULTS_FOR_RUN = "get_results_for_run"
TR_API_ADD_RESULT = "add_result"
TR_API_ADD_RESULT_FOR_CASE = "add_result_for_case"
TR_API_ADD_RESULTS = "add_results"
TR_API_ADD_RESULTS_FOR_CASES = "add_results_for_cases"

# TestRail API defines for result fields
TR_API_GET_RESULT_FIELDS = "get_result_fields"

# TestRail API defines for runs
TR_API_GET_RUN = "get_run"
TR_API_GET_RUNS = "get_runs"
TR_API_ADD_RUN = "add_run"
TR_API_UPDATE_RUN = "update_run"
TR_API_CLOSE_RUN = "close_run"
TR_API_DELETE_RUN = "delete_run"

# TestRail API defines for sections
TR_API_GET_SECTION = "get_section"
TR_API_GET_SECTIONS = "get_sections"
TR_API_ADD_SECTION = "add_section"
TR_API_UPDATE_SECTION = "update_section"
TR_API_DELETE_SECTION = "delete_section"

# TestRail API defines for statuses
TR_API_GET_STATUSES = "get_statuses"

# TestRail API defines for suite
TR_API_GET_SUITE = "get_suite"
TR_API_GET_SUITES = "get_suites"
TR_API_ADD_SUITE = "add_suite"
TR_API_UPDATE_SUITE = "update_suite"
TR_API_DELETE_SUITE = "delete_suite"

# TestRail API defines for templates
TR_API_GET_TEMPLATES = "get_templates"

# TestRail API defines for tests
TR_API_GET_TEST = "get_test"
TR_API_GET_TESTS = "get_tests"

# TestRail API defines for user
TR_API_GET_USER = "get_user"
TR_API_GET_USER_BY_EMAIL = "get_user_by_email"
TR_API_GET_USERS = "get_users"

# Dictionary Keys ( defined in TestRail )
TR_KEY_TITLE = "title"
TR_KEY_RUNS = "runs"
TR_KEY_ID = "id"
TR_KEY_PLAN_STATUS = "status"
TR_KEY_PLAN_ID = "plan_id"
TR_KEY_CASE_ID = "case_id"
TR_KEY_CASE_REFERENCE = "refs"
TR_KEY_RUN_ID = "run_id"
TR_KEY_FILE_NAME = "file_name"
TR_KEY_CLASS_NAME = "class_name"
TR_KEY_TESTPLAN_DESCRIPTION = "description"

# Config literals
CFG_SERVER_CONFIG = "Server_Config"
CFG_SERVER_URL = "server_url"
CFG_USER_ID = "user_id"
CFG_USER_PASSWD = "user_password"

# Test result dictionary
TR_DICT_RESULT = {'pass': 1, 'blocked': 2, 'untested': 3, 'retest': 4, 'fail': 5}

# TestCase attributes ( NOTE: Modify or add new attributes based on your TestRail settings)
# These are the field names of a test case
TR_TC_FIELD_STATUS_ID = 'status_id'
TR_TC_FIELD_COMMENT = 'comment'
TR_TC_FIELD_ELAPSED = 'elapsed'
TR_TC_FIELD_VERSION = 'version'
TR_TC_FIELD_DEFECTS = 'defects'
TR_TC_FIELD_ASSIGNED_TO_ID = 'assignedto_id'

# Test plan attributes
TR_TEST_PLAN_ENTRIES = "entries"


# Error Messages
TR_ERROR_CALLING_API = "HTTP 400"

# Test Stats fields
TR_STATS_TOTAL_RUNS = "total_runs"
TR_STATS_TOTAL_TESTS = "total_tests"
TR_STATS_RUN_ID_LIST = "run_id_list"
TR_STATS_TC_LIST = "tc_list"
TR_STATS_PASSED = "passed"
TR_STATS_FAILED = "failed"
TR_STATS_RETEST = "retest"
TR_STATS_BLOCKED = "blocked"


