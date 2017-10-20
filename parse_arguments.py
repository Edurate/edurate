""" reads command line arguments """
import argparse
import logging

def parse_arguments(args):
    edu_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    edu_parser.add_argument(
        "-c", "--confidential",
        help="Ignores student emails in responses",
        action="store_true", required=False
    )
    
    edu_parser.add_argument(
        "-v", "--verbose",
        help="Display confirmation information",
        action="store_const", dest="logging_level", const=logging.INFO
    )
    
    arguments = edu_parser.parse_args(args)
    return arguments