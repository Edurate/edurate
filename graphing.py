"""
Input to all functions should be the data from csv
pip install ggplot
pip install pandas
"""

# import matplotlib.pyplot as plt
from ggplot import *
from pandas import DataFrame
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

def graph(data):
    """ Method to display all graphs """

    # Converts the input data into a pandas DataFrame
    data_frame = DataFrame(data[1:], columns = data[0])

    # Graph objects returned from functions
    g1 = graph1(data_frame)

    # Display generated graphs
    print(g1)

def exampleGraph(data):
    """ Simple example on how to create a graph and return it."""

    # Convert data so ggplot can use it
    dat = DataFrame(data1, columns = ['A','B'])

    # Create graph and assign the object to g
    g = ggplot(dat, aes(x='A', y='B')) + geom_line()

    # Return graph
    return g

def graph1(data):
    """ Average score as time goes on """

    # Get all columns that are numerical questions
    numQuestions = data.select_dtypes(include=['int64']).columns.values

    # Melt data so that each question is in a seperate row
    newData = pd.melt(data, id_vars=["Date","Name"], value_vars=numQuestions, var_name="Question",value_name="Score")

    # Get rid of unecessary column
    newData = newData.drop('Name', axis=1)

    # Convert date string into an actual date type
    newData['Date'] = pd.to_datetime(newData['Date'], format="%m/%d/%Y")

    # Group all rows with same date and question, and then take the average.
    newData = newData.groupby(['Date','Question']).mean().reset_index()

    # Create graph with seperate lines for each question
    g = ggplot(aes(x='Date',y="Score",colour="Question"),newData) +\
        geom_point() +\
        geom_line() +\
        scale_x_date(labels = date_format("%Y-%m-%d")) +\
        labs(x = "Date", y = "Average Question Score") +\
        ggtitle("Question Scores Over Time")

    # Return graph
    return g

def graph2(data):
    """ Change over time. """

# Testing data for what we think the input data will be
exampleData = [["Date","Name","Textual Question", "Question 1", "Question 2", "Question 3"],["10/23/2017","dillam","Answer to textual question",1,2,7],["10/23/2017","austin","Answer to textual question",3,2,1],["10/23/2017","bob","Answer to textual question",2,3,1],["10/23/2017","john","Answer to textual question",1,4,5],["10/23/2017","joe","Answer to textual question",5,5,4],["10/30/2017","dillam","Answer to textual question",2,2,6],["10/30/2017","austin","Answer to textual question",5,2,1],["10/30/2017","bob","Answer to textual question",2,3,10],["10/30/2017","john","Answer to textual question",3,4,2],["10/30/2017","joe","Answer to textual question",5,2,4],["11/7/2017","dillam","Answer to textual question",2,1,3],["11/7/2017","austin","Answer to textual question",5,5,5],["11/7/2017","bob","Answer to textual question",6,4,5],["11/7/2017","john","Answer to textual question",5,4,7],["11/7/2017","joe","Answer to textual question",5,5,6]]

# Test out the graphing function
graph(exampleData)
