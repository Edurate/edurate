import gspread
import logging
import csv
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
def read_from_spreadsheet():
    """ reads the google spreadsheet """
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

def getGraphData(spreadsheet_list, conf):
    new = list()
    for key in spreadsheet_list[0].keys():
        new.append(key)
    output = list()
    output.append(new)
    for dictionary in spreadsheet_list:
        new = list()
        date = False
        for key, value in dictionary.items():
            if key == "Email Address" and conf:
                continue
            elif key == "Timestamp":
                new.append(value.split(" ")[0])
            else:
                new.append(value)
        output.append(new)

    return output

def create_csv(spreadsheet_list):
    """ creates the csv file """
    # returns True when funciton is completed
    logging.info("Creating a list of lists of students")
    formatted_list = list()
    # grabs questions from spreadsheet
    for entry in spreadsheet_list:
        questions = [None]*12
        for question, response in entry.items():
            if question[:2] == '1.':
                questions.pop(2)
                questions.insert(2, question)
            elif question[:2] == '2.':
                questions.pop(3)
                questions.insert(3, question)
            elif question[:2] == '3.':
                questions.pop(4)
                questions.insert(4, question)
            elif question[:2] == '4.':
                questions.pop(5)
                questions.insert(5, question)
            elif question[:2] == '5.':
                questions.pop(6)
                questions.insert(6, question)
            elif question[:2] == '6.':
                questions.pop(7)
                questions.insert(7, question)
            elif question[:2] == '7.':
                questions.pop(8)
                questions.insert(8, question)
            elif question[:2] == '8.':
                questions.pop(9)
                questions.insert(9, question)
            elif question[:2] == '9.':
                questions.pop(10)
                questions.insert(10, question)
            elif question[:3] == '10.':
                questions.pop(11)
                questions.insert(11, question)
        break
    # grabs responses to questions from each user
    for entry in spreadsheet_list:
        maxDate = datetime(2000, 1, 1, 0, 0).date()
        formatted_entry = [None]*12
        for question, response in entry.items():
            if question == 'Timestamp':
                time = entry[question].partition(' ')[0]
                formatted_entry.pop(0)
                date = datetime.strptime(time, '%m/%d/%Y').date()
                if(date > maxDate):
                    maxDate = date
                formatted_entry.insert(0, date)
            elif question == 'Email Address':
                username = entry[question].partition('@')[0]
                formatted_entry.pop(1)
                formatted_entry.insert(1, username)
            elif question[:2] == '1.':
                formatted_entry.pop(2)
                formatted_entry.insert(2, entry[question])
            elif question[:2] == '2.':
                formatted_entry.pop(3)
                formatted_entry.insert(3, entry[question])
            elif question[:2] == '3.':
                formatted_entry.pop(4)
                formatted_entry.insert(4, entry[question])
            elif question[:2] == '4.':
                formatted_entry.pop(5)
                formatted_entry.insert(5, entry[question])
            elif question[:2] == '5.':
                formatted_entry.pop(6)
                formatted_entry.insert(6, entry[question])
            elif question[:2] == '6.':
                formatted_entry.pop(7)
                formatted_entry.insert(7, entry[question])
            elif question[:2] == '7.':
                formatted_entry.pop(8)
                formatted_entry.insert(8, entry[question])
            elif question[:2] == '8.':
                formatted_entry.pop(9)
                formatted_entry.insert(9, entry[question])
            elif question[:2] == '9.':
                formatted_entry.pop(10)
                formatted_entry.insert(10, entry[question])
            elif question[:3] == '10.':
                formatted_entry.pop(11)
                formatted_entry.insert(11, entry[question])
            else:
                formatted_entry.append(response)

        formatted_list.append(formatted_entry)
        for entry in formatted_list:
            if(entry[0] < maxDate):
                formatted_list.pop(formatted_list.index(entry))
    formatted_list.insert(0, questions)

    logging.info("Writing formatted data to CSV file")
    logging.debug("CSV file name: " + "data.csv")
    with open("./data.csv", 'w') as myfile:
        writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for item in formatted_list:
            writer.writerow(item)
    return True
