""" reads command line arguments """
import argparse
import logging

from default import DEFAULT_FILE


def parse_arguments(args):
    edu_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    edu_parser.add_argument(
        "-f", "--file",
        help="File containing the responses",
        type=str, required=False, default=DEFAULT_FILE
    )

    edu_parser.add_argument(
        "-c", "--confidential",
        help="Ignores student emails in responses",
        action="store_true", required=False
    )

    edu_parser.add_argument(
        "-a", "--archive",
        help="Writes information from the spreadsheet to Archive directory",
        action="store_true", required=False
    )

    edu_parser.add_argument(
        "-g",
        "--graph",
        help="Displays trend over time, average scores for each response, box plot for each entry",
        action="store_true",
        required=False
    )

    edu_parser.add_argument(
        "-d", "--debug",
        help="Display diagnostic information",
        action="store_const", dest="logging_level",
        const=logging.DEBUG, default=logging.ERROR
    )

    edu_parser.add_argument(
    "-add", "--add_question",
    help="Adds a question to the google form",
    required=False, action="store_true"
    )

    edu_parser.add_argument(
    "-del", "--delete_question",
    help="Removes a question to the google form",
    required=False, action="store_true"
    )

    arguments = edu_parser.parse_args(args)
    return arguments
