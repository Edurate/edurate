import csv
import datetime

def archive_information(data):
    """ Recieves 2d list of responses and saves them to csv archive """
    today = datetime.datetime.now()
    fileName = str(today.month)+"-"+str(today.day)+"-"+str(today.year)+".csv"
    print(fileName)
    with open("./archive/"+fileName, 'w+') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(data)

testData = [["Row 1", 5, 6],["Row 2", 3, 4],["Row 3", 1, 2]]

archive_information(testData)
