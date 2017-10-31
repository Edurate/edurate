import sys
import logging

from spreadsheet import read_from_spreadsheet
from spreadsheet import create_csv
from spreadsheet import getGraphData
from spreadsheet import *
from parse_arguments import parse_arguments
from read_responses import read_responses
from parse_arguments import parse_arguments
from graphing import graph
from edurate_gensim import gensim_analysis

if __name__ == "__main__":
    print("Welcome to Edurate")
    print("https://github.com/Edurate/edurate")

    edu_args = parse_arguments(sys.argv[1:])
    print(edu_args.file)
    if(edu_args.confidential):
        print("Confidential")
    if(edu_args.archive):
        print("Archive")
    if(edu_args.graph):
        print("Graph")
    spreadsheet_list = read_from_spreadsheet()
    data = getGraphData(spreadsheet_list, edu_args.confidential)
    if(edu_args.confidential):
        print("Confidential")
    if(edu_args.archive == True):
        print("Archive")
    if(edu_args.graph == True):
        print("Graph")
        graph(data)
