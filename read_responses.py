import csv
from pathlib import Path

""" Reads the .cvs file and returns the information stored inside """

# send function name of the file to be read and if names are confidential


def read_responses(filepath, conf):
    # checks if the file exists
    if Path(filepath).is_file() is False:
        return "File Not Found"
    # places all of the data in the file into csvdata
    with open(filepath, newline='') as csvfile:
        csvdata = list(csv.reader(csvfile, delimiter=','))
    generate_responses(csvdata)
    return responses

def generate_responses(csvdata_list):		
    responses = list()
    for record in csvdata_list:
        # date of response
        responses.append(record[0])
        # if the responses are not confidential, include name
        if(conf is False):
            responses.append(record[1])
        # responses to the questions
        for value in record[2:]:
            responses.append(value)
