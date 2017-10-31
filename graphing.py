"""
Input to all functions should be the data from csv
pip3 install ggplot
"""

import warnings
warnings.filterwarnings('ignore')

from ggplot import *
from pandas import DataFrame
from pandas import Series
import pandas as pd
from datetime import datetime
import logging

def graph(data):
    """ Takes only most recent input data and then displays graphs """

    # Get all data because we need to see trend over time
    data = convertToInts(data) + getArchivedData()

    g1 = graph1(data)
    g2 = graph2(data)
    g3 = graph3(data)

    # Display generated graphs
    print(g1)
    print(g2)
    print(g3)

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
        return convertToInts(list(reader))

def convertToInts(data):
    """ The numerical answers in the input comes in as strings. Convert these to integers so they can be graphed. """
    output = list()
    for row in data:
        cur = list()
        for item in row:
            try:
                cur.append(int(item))
            except(ValueError):
                cur.append(item)
        output.append(cur)
    return output

def graph1(scoreData):
    """ Average score as time goes on """

    dateColumn = scoreData[0][0]

    data = DataFrame(scoreData[1:], columns = scoreData[0])

    # Get all columns that arlabels = date_format("%Y-%m-%d")e numerical questions so we know what to graph
    numQuestions = data.select_dtypes(include=['int64']).columns.values

    # Melt data so that each question is in a seperate row
    newData = pd.melt(data, id_vars=dateColumn, value_vars=numQuestions, var_name="Question",value_name="Score")

    # Convert date string into an actual date type
    newData[dateColumn] = pd.to_datetime(newData[dateColumn], format="%m/%d/%Y")

    # Group all rows with same date and question, and then take the average.
    newData = newData.groupby([dateColumn,'Question']).mean().reset_index()
    newData['All'] = "Indiviual Questions"

    newData2 = newData.groupby(dateColumn).mean().reset_index()
    newData2['Question'] = "All Questions"
    newData2['All'] = "Average of All Questions"

    newData = pd.concat([newData, newData2])

    newData[dateColumn] = newData[dateColumn].astype('int64')

    # Create time graph with seperate lines for each question
    g = ggplot(aes(x=dateColumn,y="Score",colour="Question"), newData) +\
        geom_point() +\
        geom_line() +\
        facet_grid("All") +\
        scale_x_continuous(labels=[""],breaks=0) +\
        labs(x = "Time", y = "Average Question Score") +\
        ggtitle("Question Scores Over Time")

    # Return graph
    return g

def graph2(scoreData):
    """ Average scores for each question on most recent date """

    dateColumn = scoreData[0][0]

    data = DataFrame(scoreData[1:], columns = scoreData[0])

    # Get all columns that are numerical questions so we know what to graph
    numQuestions = data.select_dtypes(include=['int64']).columns.values

    # Melt data so that each question is in a seperate row
    newData = pd.melt(data, id_vars=dateColumn, value_vars=numQuestions, var_name="Question",value_name="Score")

    # Convert date string into actual data type
    newData[dateColumn] = pd.to_datetime(newData[dateColumn], format="%m/%d/%Y")

    # Latest Dates
    recent_date = newData[dateColumn].max()

    # Removing all dates that are recent
    newData = newData[newData.Date==recent_date]

    # Group all rows with question, and then take the average.
    newData = newData.groupby(['Question']).mean().reset_index()

    # Create bar graph with data from past week
    g2 = ggplot(aes(x = "Question", weight = "Score"), newData) +\
        geom_bar() +\
        ggtitle("Most Recent Average Scores")

    # Return graph
    return g2

def graph3(scoreData):
    """ Box plot for scores """

    dateColumn = scoreData[0][0]

    data = DataFrame(scoreData[1:], columns = scoreData[0])

    # Get all columns that are numerical questions
    numQuestions = data.select_dtypes(include=['int64']).columns.values

    # Melt data so that each question is in a seperate row
    newData = pd.melt(data, id_vars=[dateColumn,"Name"], value_vars=numQuestions, var_name="Question",value_name="Score")

    # Get rid of unecessary column
    newData = newData.drop('Name', axis=1)

    # Convert date string into an actual date type
    newData[dateColumn] = pd.to_datetime(newData[dateColumn], format="%m/%d/%Y")

    # Create box plot graph
    g3 = ggplot(aes(x = dateColumn, y = 'Score'), newData) +\
         geom_boxplot() +\
         ggtitle("Distribution of Question Scores over Time")

    # Return graph
    return g3
