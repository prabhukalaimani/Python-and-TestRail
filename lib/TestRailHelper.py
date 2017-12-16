# -*- coding: utf-8 -*-
##############################################################################
# ஆசிரியர்  : பிரபு கலைமணி
# பயன்பாடு : இந்த கோப்பு
# http://docs.gurock.com/testrail-api2/start
# FileName :
# usage : This file will read the config.ini file and will return the key
# Date : 12/14/2017
##############################################################################


class TestRailHelper:
    def __init__(self):
        self.server_url = ""
        self.server_password = ""

    def get_testplans(self, project_id):
        pass

    def get_case(self, caseid):
        pass

    def get_testcases(self, runid):
        pass

    def get_testcase_value(self, tcid):
        pass

# Unit testing the helper library
class TestTRHelper:
    @classmethod
    def setup_class(cls):
        cls.server_url = ""
        cls.server_password = ""
        pass