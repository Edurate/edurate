import csv
from datetime import datetime
import os
import logging


def archive_information(data):
    """ Saves dates to csv file so that inmrovment can be documented"""

    today = datetime.now()
    fileName = str(today.month) + "-" + str(today.day) + \
        "-" + str(today.year) + ".csv"
    print(fileName)
    if not os.path.exists("./archive/"):
        os.makedirs("./archive/")
    with open("./archive/" + fileName, 'w+') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(data)

    logging.info("CSV gets written by 2d list for archive")


""" future feature """


def getArchivedData():
    """ Updates what is now the latest data gathered to csv file """

    latest = None
    for fil in os.listdir("./archive"):
        date = datetime.strptime(fil.split(".")[0], '%m-%d-%Y')
        if latest is None or date > latest:
            latest = date

    if (latest is None):
        return None

    fileName = str(latest.month) + "-" + str(latest.day) + \
        "-" + str(latest.year) + ".csv"
    with open("./archive/" + fileName, 'r') as csvFile:
        reader = csv.reader(csvFile)
        return list(reader)[1:]

    logging.info("Returns archive from the oldest one")
