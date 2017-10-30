import gspread
import logging
import csv
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
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
        maxDate = datetime(2000, 1, 1, 0, 0).date()
        formated_entry = [None]*12
        for question, response in entry.items():    
            if question == 'Timestamp':
                time = entry[question].partition(' ')[0]
                formated_entry.pop(0)
                date = datetime.strptime(time, '%m/%d/%Y').date()
                if(date > maxDate):
                    maxDate = date
                formated_entry.insert(0, date)
            elif question == 'Email Address':
                username = entry[question].partition('@')[0]
                formated_entry.pop(1)
                formated_entry.insert(1, username)             
            elif question[:2] == '1.':
                formated_entry.pop(2)
                formated_entry.insert(2, entry[question])
            elif question[:2] == '2.':
                formated_entry.pop(3)
                formated_entry.insert(3, entry[question])
            elif question[:2] == '3.':
                formated_entry.pop(4)
                formated_entry.insert(4, entry[question])
            elif question[:2] == '4.':
                formated_entry.pop(5)
                formated_entry.insert(5, entry[question])
            elif question[:2] == '5.':
                formated_entry.pop(6)
                formated_entry.insert(6, entry[question])
            elif question[:2] == '6.':
                formated_entry.pop(7)
                formated_entry.insert(7, entry[question])
            elif question[:2] == '7.':
                formated_entry.pop(8)
                formated_entry.insert(8, entry[question])
            elif question[:2] == '8.':
                formated_entry.pop(9)
                formated_entry.insert(9, entry[question])
            elif question[:2] == '9.':
                formated_entry.pop(10)
                formated_entry.insert(10, entry[question])
            elif question[:3] == '10.':
                formated_entry.pop(11)
                formated_entry.insert(11, entry[question])
            else:
                formated_entry.append(response)

        formated_list.append(formated_entry)
    for entry in formated_list:
        if(entry[0] < maxDate):
            formated_list.pop(formated_list.index(entry))
            
    logging.info("Writing formatted data to CSV file")
    logging.debug("CSV file name: " + "data.csv")
    with open("./data.csv", 'w') as myfile:
        writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for item in formated_list:
            writer.writerow(item)
    return True
