""" Reads the .cvs file and returns the information stored inside """
import csv
from pathlib import Path
# send function name of the file to be read and if names are confidential
def read_responses(filepath, conf):
    # checks if the file exists
    if Path(filepath).is_file() is False:
        return "filenotfound"
    # places all of the data in the file into csvdata
    with open(filepath, newline='') as csvfile:
        csvdata = list(csv.reader(csvfile, delimiter=','))

    responses = list()
    for record in csvdata:
        #temp = list()
        # date of response
        responses.append(record[0])
        # if the responses are not confidential, include name
        if(conf == False):
            responses.append(record[1])
        # responses to the questions
        for value in record[2:]:
            responses.append(value)
        #responses.append(temp)
    return responses
