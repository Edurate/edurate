"""Input to all functions should be the data from csv"""

import logging
import warnings
import pandas as pd
from pandas import DataFrame
import ggplot
warnings.filterwarnings('ignore')



def graph(data):
    """ Takes only most recent input data and then displays graphs """
    # get all data because we need to see trend over time
    data = convert_to_ints(data)
    # display generated graphs
    print(graph1(data))
    print(graph2(data))
    print(graph3(data))
    logging.info("Calls and prints graphical data")


def convert_to_ints(data):
    """ The numerical answers in the input comes in as strings.
        Convert these to integers so they can be graphed. """
    output = list()
    for row in data:
        cur = list()
        for item in row:
            try:
                cur.append(int(item))
            except ValueError:
                cur.append(item)
        output.append(cur)
    return output


def find_time_stamp(data):
    """ Finds the timestamp from the responses """
    columns = data[0]
    for i in range(0, len(columns)):
        if columns[i] == "Timestamp":
            return i


def graph1(score_data):
    """ Average score as time goes on;
        Creates and returns graph 1, a line graph. """

    date_column = score_data[0][find_time_stamp(score_data)]

    data = DataFrame(score_data[1:], columns=score_data[0])

    # Get all columns that arlabels = date_format("%Y-%m-%d")e numerical
    # questions so we know what to graph
    num_questions = data.select_dtypes(include=['int64']).columns.values

    # Melt data so that each question is in a seperate row
    new_data = pd.melt(
        data,
        id_vars=date_column,
        value_vars=num_questions,
        var_name="Question",
        value_name="Score")

    # Convert date string into an actual date type
    new_data[date_column] = pd.to_datetime(
        new_data[date_column], format="%m/%d/%Y")

    # Group all rows with same date and question, and then take the average.
    new_data = new_data.groupby([date_column, 'Question']).mean().reset_index()
    new_data['All'] = "Indiviual Questions"

    new_data2 = new_data.groupby(date_column).mean().reset_index()
    new_data2['Question'] = "All Questions"
    new_data2['All'] = "Average of All Questions"

    new_data = pd.concat([new_data, new_data2])

    new_data[date_column] = new_data[date_column].astype('int64')

    # Create time graph with seperate lines for each question
    ret = ggplot.ggplot(ggplot.aes(x=date_column, y="Score", colour="Question"), new_data) +\
        ggplot.geom_point() +\
        ggplot.geom_line() +\
        ggplot.facet_grid("All") +\
        ggplot.scale_x_continuous(labels=[""], breaks=0) +\
        ggplot.labs(x="Time", y="Average Question Score") +\
        ggplot.ggtitle("Question Scores Over Time")
    return ret


def graph2(score_data):
    """ Average scores for each question on most recent date;
        Creates and returns graph 2, a bar graph. """

    date_column = score_data[0][find_time_stamp(score_data)]

    columns_data = score_data[0]
    for i in range(0, len(columns_data)):
        columns_data[i] = columns_data[i].split('.')[0]

    data = DataFrame(score_data[1:], columns=columns_data)

    # Get all columns that are numerical questions so we know what to graph
    num_questions = data.select_dtypes(include=['int64']).columns.values

    # Melt data so that each question is in a seperate row
    new_data = pd.melt(
        data,
        id_vars=date_column,
        value_vars=num_questions,
        var_name="Question",
        value_name="Score")

    # Convert date string into actual data type
    new_data[date_column] = pd.to_datetime(
        new_data[date_column], format="%m/%d/%Y")

    # Latest Dates
    recent_date = new_data[date_column].max()

    # Removing all dates that are recent
    new_data = new_data[new_data.Timestamp == recent_date]

    # Group all rows with question, and then take the average.
    new_data = new_data.groupby(['Question']).mean().reset_index()

    # Create bar graph with data from past week
    ret = ggplot.ggplot(ggplot.aes(x="Question", weight="Score"), new_data) +\
        ggplot.geom_bar() +\
        ggplot.ggtitle("Most Recent Average Scores")
    return ret


def graph3(score_data):
    """ Box plot for scores;
        Creates and returns graph 3, a box plot. """

    date_column = score_data[0][find_time_stamp(score_data)]
    data = DataFrame(score_data[1:], columns=score_data[0])

    # Get all columns that are numerical questions
    num_questions = data.select_dtypes(include=['int64']).columns.values

    # Melt data so that each question is in a seperate row
    new_data = pd.melt(
        data,
        id_vars=[
            date_column,
            "Name"],
        value_vars=num_questions,
        var_name="Question",
        value_name="Score")

    # Get rid of unecessary column
    new_data = new_data.drop('Name', axis=1)

    # Convert date string into an actual date type
    new_data[date_column] = pd.to_datetime(
        new_data[date_column], format="%m/%d/%Y")

    # Create box plot graph
    box_plot = ggplot.ggplot(ggplot.aes(x=date_column, y='Score'), new_data) +\
        ggplot.geom_boxplot() +\
        ggplot.ggtitle("Distribution of Question Scores over Time")
    return box_plot
