#!/usr/bin/python
"""
Author: Prabhu Kalaimani
Purpose: The purpose of this wrapper is to call the TestRail utility methods from jenkins or other
command line tools. This file is a wrapper for TestRailLib.py file. This wrapper will combine methods
available in the TestRailLib.py file and return the output which can be used by Jenkins and other tools
to report or process test cases in TestRail.
Note: Most of the methods will returns a status and return values(output)
"""

import argparse
import TestRailLib as TestRail
import trDefines as Defines

# TestRail Setup
# TBD: Read from a ini file
user_id = "xxxxxx"
password = "xxxxx"
# Create a TestRail instance.
tr = TestRail.TestRailLib("https://xxxx", user_id, password)

# Methods used by Jenkins and other tools
def get_total_tc_of_suite(args):
    """
    Get the total Testcases of a test suite
    :param args: suite_id
    :return:
    """
    total_tc = 0
    tmp_list = args.param_list
    if tmp_list is None:
        tmp_list = [Defines.TR_TC_ID]
    status, ret_dict = tr.tr_get_test_cases(args.suite_id, tmp_list)
    if status:
        total_tc = len(ret_dict)
    print(status, total_tc)
    return status,total_tc

def b(opt3="", opt4=""):
    print("temp function")



# Create an Arguments parser and then create a sub parser for the utility functions
parser = argparse.ArgumentParser(prog="TestRail Wrapper Applicaiton")
utility_function = parser.add_subparsers(help='Utility commands')

# Create a sub parser to parse the function
# Utility method 1: tr_get_test_cases params
# Usage: TBD
parser_tr_get_test_cases = utility_function.add_parser('tr_get_test_cases', help="Function tr_get_test_cases help")
parser_tr_get_test_cases.add_argument("suite_id")
parser_tr_get_test_cases.add_argument("--param_list", type=str, help="Enter the parameter list with double quotes. Example \"[param-1, pram-2..param-n ]\"")
parser_tr_get_test_cases.set_defaults(func=get_total_tc_of_suite)

# Function 2
parser_b = utility_function.add_parser('b', help='b help')
parser_b.add_argument("opt3")
parser_b.set_defaults(func=b)
parser_b.add_argument("--opt4")


# Parse the arguments and call the respective utility method
args= parser.parse_args()
print("\n" + "-" * 80)
i = 1
print("Calling function {}".format(args.func.__name__))
for itm in args.__dict__:
    if itm not in "func":
        print("Argument {} : {}".format(i,args.__dict__[itm]))
        i= i+1
print("-" * 80 + "\n")
args.func(args)
