import csv
from datetime import datetime, timedelta
import os


def archive_information(data):
    """ Recieves 2d list of responses and saves them to csv archive """

    data = data + getArchivedData()

    today = datetime.now()
    fileName = str(today.month)+"-"+str(today.day)+"-"+str(today.year)+".csv"
    print(fileName)
    with open("./archive/"+fileName, 'w+') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(data)

def getArchivedData():
    """ Returns all old data from latest archived csv """

    latest = None
    for fil in os.listdir("./archive"):
        date = datetime.strptime(fil.split(".")[0], '%m-%d-%Y')
        if latest == None or date > latest:
            latest = date

    if (latest == None):
        return None

    fileName = str(latest.month)+"-"+str(latest.day)+"-"+str(latest.year)+".csv"
    with open("./archive/"+fileName, 'r') as csvFile:
        reader = csv.reader(csvFile)
        return list(reader)[1:]

testData = [["Date","Name","Textual Question", "Question 1", "Question 2", "Question 3"],["11/7/2017","dillam","Answer to textual question","2","1","3"],["11/7/2017","austin","Answer to textual question","5","5","5"],["11/7/2017","bob","Answer to textual question","6","4","5"],["11/7/2017","john","Answer to textual question","5","4","7"],["11/7/2017","joe","Answer to textual question","5","5","6"]]

archive_information(testData)
