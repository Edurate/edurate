# Test cases for the parse_arguments function.
# To run these test suites type the following
# into the command line when in the tests/ directory:
# pytest test_parse_arguments.py

import parse_arguments
import glob
import os
import logging
from flake8.api import legacy as flake8


def test_parse_arguments1():
    """Testing the program when the user does not enter any arguments"""
    args = []
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.ERROR


def test_parse_arguments2():
    """Testing for appropriate output when a file is specified and
        the --debug argument is given. To ensure proper output,
        we assert that the program parses the correct file and that
        the logging function being used is the logging.DEBUG function"""
    args = ['--file', 'data.csv', '--debug']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.file == 'data.csv'
    assert parsed_args.logging_level == logging.DEBUG


def test_parse_arguments3():
    """Testing when a file is specified and the --confidential
        argument is given. To ensure proper output, we assert
        that the program passes the "confidential" argument"""
    args = ['--file', 'data.csv', '--confidential']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.confidential


# Linting Tests
def test_flake8():

    # list of all file names to be checked for PEP8
    filenames = list()

    # fill list with all python files found in all subdirectories
    for root, dirs, files in os.walk("edurate", topdown=False):
        pyFiles = glob.glob(root + "/*.py")
        filenames.extend(pyFiles)

    style_guide = flake8.get_style_guide(ignore=["E265", "E501", "F405"])
    report = style_guide.check_files(filenames)
    assert report.get_statistics('E') == [], 'Flake8 found violations'