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
