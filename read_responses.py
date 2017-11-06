import csv
from pathlib import Path

""" Reads the .cvs file and returns the information stored inside """

# send function name of the file to be read and if names are confidential


def read_responses(filepath):
    # checks if the file exists
    if Path(filepath).is_file() is False:
        return "File Not Found"
    # places all of the data in the file into csvdata
    with open(filepath, newline='') as csvfile:
        csvdata = list(csv.reader(csvfile, delimiter=','))

    responses = list()
    for record in csvdata[1:]:
        # date of response
        row = list()
        row.append(record[0])
        # if the responses are not confidential, include name
        row.append(record[1])
        # responses to the questions
        for value in record[2:]:
            row.append(value)
        responses.append(row)
    return responses
