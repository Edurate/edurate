import sys
import logging

from parse_arguments import parse_arguments

if __name__ == "__main__":
    print("Welcome to Edurate")
    print("https://github.com/Edurate/edurate")
    edu_args = parse_arguments(sys.argv[0:])
