""" main fuction """
import sys
import logging

from spreadsheet import read_from_spreadsheet
from spreadsheet import create_csv
from spreadsheet import getGraphData
from spreadsheet import filterDates
from parse_arguments import parse_arguments
from read_responses import read_responses
from parse_arguments import parse_arguments
from graphing import graph
from archive_information import archive_information
from edurate_gensim import gensim_analysis
from questions import add_question
from questions import remove_question

if __name__ == "__main__":
    print("Welcome to Edurate")
    print("https://github.com/Edurate/edurate")

    edu_args = parse_arguments(sys.argv[1:])
    spreadsheet_list = read_from_spreadsheet()
    data = getGraphData(spreadsheet_list, edu_args.confidential)
    if(edu_args.archive == True):
        print("Archive")
        archive_information(data)
    if(edu_args.graph == True):
        print("Graph")
        graph(data)
    if(edu_args.add_question == True):
        url = input("Please enter the url to your google form: ")
        add_question(url)
    if(edu_args.delete_question == True):
        url = input("Please enter the url to your google form: ")
        remove_question(url)
    create_csv(spreadsheet_list)
    res = read_responses(edu_args.file, edu_args.confidential)
    gensim_analysis(res)
