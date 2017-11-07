""" reads command-line arguments """
import argparse
import logging

import default


def parse_arguments(args):
    """ reads command-line arguments """
    edu_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    edu_parser.add_argument(
        "-f", "--file",
        help="File containing the responses",
        type=str, required=False, default=default.DEFAULT_FILE
    )

    edu_parser.add_argument(
        "-c", "--confidential",
        help="Ignores student emails in responses",
        action="store_true", required=False
    )

    edu_parser.add_argument(
        "-t", "--topics",
        help="Sets number of topics for LDA analysis",
        type=int, required=False, default=default.DEFAULT_NUM_OF_TOPICS
    )

    edu_parser.add_argument(
        "-g",
        "--graph",
        help="Displays trend over time, average scores for each response," +
        " and box plot for each entry",
        action="store_true",
        required=False)

    edu_parser.add_argument(
        "-d", "--debug",
        help="Display diagnostic information",
        action="store_const", dest="logging_level",
        const=logging.DEBUG, default=logging.ERROR
    )

    arguments = edu_parser.parse_args(args)
    return arguments
