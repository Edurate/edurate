""" reads command line arguments """
import argparse
import logging

def parse_arguments(args):
    edu_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        
    edu_parser.add_argument(
        "-f", "--file",
        help="File containing last name of students",
        type=str, required=True
    )
    
    edu_parser.add_argument(
        "-c", "--confidential",
        help="Ignores student emails in responses",
        action="store_true", required=False
    )
    
    edu_parser.add_argument(
        "-d", "--debug",
        help="Display diagnostic information",
        action="store_const", dest="logging_level",
        const=logging.DEBUG, default=logging.ERROR
    )
    
    edu_parser.add_argument(
        "-v", "--verbose",
        help="Display confirmation information",
        action="store_const", dest="logging_level", 
        const=logging.INFO
    )
    
    edu_parser.add_argument(
        "-s", "--spam",
        help="Removes spam and other unneccessary information",
        action="store_true", required=False
    )
    
    arguments = edu_parser.parse_args(args)
    return arguments
