""" main fuction """
import sys
import logging

from spreadsheet import read_from_spreadsheet
from spreadsheet import create_csv
from spreadsheet import getGraphData
from spreadsheet import filterDates, flip_responses
from parse_arguments import parse_arguments
from read_responses import read_responses
from parse_arguments import parse_arguments
from graphing import graph
from archive_information import archive_information
from edurate_gensim import gensim_analysis

if __name__ == "__main__":
    print("Welcome to Edurate")
    print("https://github.com/Edurate/edurate")
    logging.info("Analyzes the Google form responses with gensim and " +
                 "returns the repeated words, graphs, or archives the file")
    edu_args = parse_arguments(sys.argv[1:])
    spreadsheet_list = read_from_spreadsheet()
    data = getGraphData(spreadsheet_list)

    if(edu_args.graph):
        print("Creating Graphs...")
        graph(data)

    create_csv(spreadsheet_list)
    responses = read_responses(edu_args.file)
    print("Non-filtered responses: " + str(responses) + "\n")
    responses = filterDates(responses)
    print("FILTERED RESPONSES")
    for response in responses:
        print(response)

    print("FLIPPED RESPONSES")
    responses = flip_responses(responses)
    for response in responses:
        print(response)
    print("Flipped responses: " + str(responses))
    q_count = 7
    for index, response in enumerate(responses[8:12]):
        print("response: " + str(response))
        print("q_count: " + str(q_count))
        gensim_analysis(response, q_count)
        q_count += 1
