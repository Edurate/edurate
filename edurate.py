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
    EDU_ARGS = parse_arguments(sys.argv[1:])
    SPREADSHEET_LIST = spreadsheet.read_from_spreadsheet()
    DATA = spreadsheet.get_graph_data(SPREADSHEET_LIST)

    if EDU_ARGS.graph:
        print("Creating Graphs...")
        graph(DATA)

    spreadsheet.create_csv(SPREADSHEET_LIST)
    RESPONSES = read_responses(EDU_ARGS.file)
    RESPONSES = spreadsheet.filter_dates(RESPONSES)
    RESPONSES = spreadsheet.flip_responses(RESPONSES)

    QUESTION_NUMBER = 7
    for index, response in enumerate(RESPONSES[8:12]):
        gensim_analysis(response, QUESTION_NUMBER)
        QUESTION_NUMBER += 1
