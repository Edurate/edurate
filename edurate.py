import sys
import logging
from edurate_gensim import create_tokens
from spreadsheet import read_from_spreadsheet
from spreadsheet import create_csv
from parse_arguments import parse_arguments
from read_responses import read_responses

if __name__ == "__main__":
    print("Welcome to Edurate")
    print("https://github.com/Edurate/edurate")

    print("Welcome to Edurate")
    print("https://github.com/Edurate/edurate")
    edu_args = parse_arguments(sys.argv[1:])
    print(edu_args.file)
    if(edu_args.confidential):
        print("Confidential")
    if(edu_args.spam):
        print("Spam")

    spreadsheet_list = read_from_spreadsheet()
    create_csv(spreadsheet_list)
    # sends file name supplied by user and if confidential
    # and gets the responses from the csv file
    res = read_responses(edu_args.file, edu_args.confidential)
    #for response in res:
            #print(response)
    create_tokens(res)
