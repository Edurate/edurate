"""Performs NLP on student responses to teaching evaluation."""
import sys
import logging

import spreadsheet
from parse_arguments import parse_arguments
from read_responses import read_responses
from graphing import graph
from edurate_gensim import gensim_analysis

if __name__ == "__main__":
    print("Welcome to Edurate")
    print("https://github.com/Edurate/edurate")
    logging.info("Analyzes the Google form responses with gensim and " +
                 "returns the repeated words, graphs, or archives the file")
    edu_args = parse_arguments(sys.argv[1:])
    spreadsheet_list = spreadsheet.read_from_spreadsheet()
    data = spreadsheet.get_graph_data(spreadsheet_list)

    if(edu_args.graph):
        print("Creating Graphs...")
        graph(data)

    spreadsheet.create_csv(spreadsheet_list)
    responses = read_responses(edu_args.file)
    responses = spreadsheet.filter_dates(responses)
    responses = spreadsheet.flip_responses(responses)

    question_number = 7
    for index, response in enumerate(responses[8:12]):
        gensim_analysis(response, question_number)
        question_number += 1
