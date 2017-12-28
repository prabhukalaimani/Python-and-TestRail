# -*- coding: utf-8 -*-
##############################################################################
# ஆசிரியர்  : பிரபு கலைமணி
# பயன்பாடு : இந்த கோப்பு காண்பிக் பைலை  குறியீட்டு நீக்கம்  செய்யும்
# FileName : ConfigParser
# usage : This file will read the config.ini file and will return the key
# Date : 12/14/2017
##############################################################################

import configparser
import os
import pytest

class MyParser():
    """
    This class contains the method required for file parser
    """
    def __init__(self, config_file):
        if os.path.isfile(config_file):
            self.config_file = config_file
        else:
            raise IOError("File not found in the path")
        self.conf_hanle = configparser.ConfigParser()
        self.conf_hanle.read(self.config_file)


    def retrive_value(self, section, key):
        """
        This function will retrieve value of the key present in the config.ini file
        :param key: Key in the config file
        :return: value for the key
        """
        ret_value = ""
        try:
            ret_value = self.conf_hanle.get(section, key)
        except Exception:
            ret_value = "key not found in section of the ini file. Please check the secontion and key"
        return ret_value

    def get_sections(self):
        """
        This function will return the section found in the ini file
        :return: List of sections found in the ini file
        """
        return self.conf_hanle.sections()


class TestConfigParser:
    @classmethod
    def setup_class(cls):
        cls.handle = MyParser("..\\config.ini")

    def test_conf_section_data(self):
        """
        Test to check if the values are retieved properly
        :return:
        """
        section_val = "Server_Config"
        key_val = "user_password"
        val = self.handle.retrive_value(section_val, key_val)
        assert val == 12345,  "Value could not be extracted"

    def test_conf_sections(self):
        """
        This test will test if the sections can be retrieved
        :return:
        """
        sections = self.handle.get_sections()
        assert sections is not [], "No section found in the ini file"