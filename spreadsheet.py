import gspread
import logging
import csv
from oauth2client.service_account import ServiceAccountCredentials

def read_from_spreadsheet():

    logging.info(
        "Authenticating to Google Sheets to obtain Google Form data")
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('Edurate_Client.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Instructor/Course Evaluation (Responses)").sheet1

    # Extract and return all of the values
    list_of_hashes = sheet.get_all_records()
    return list_of_hashes

def create_csv(spreadsheet_list):
    # returns True when funciton is completed
    logging.info("Creating a list of lists of students")
    formated_list = list()
    for entry in spreadsheet_list:
        formated_entry = list()
        for question, response in entry.items():
            if question == 'Email Address':
                username = entry[question].partition('@')[0]
                formated_entry.append(username)
            elif question == 'Timestamp':
                time = entry[question].partition(' ')[0]
                formated_entry.append(time)
            else:
                formated_entry.append(response)

        formated_entry.insert(
            0, formated_entry.pop(
                formated_entry.index(time)))
        formated_entry.insert(
            1, formated_entry.pop(
                formated_entry.index(username)))
        formated_list.append(formated_entry)

    logging.info("Writing formatted data to CSV file")
    logging.debug("CSV file name: " + "data.csv")
    with open("./data.csv", 'w') as myfile:
        writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for item in formated_list:
            writer.writerow(item)
    return True
