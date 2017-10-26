"""
Input to all functions should be the data from csv
pip install ggplot
pip install pandas
"""

# import matplotlib.pyplot as plt
from ggplot import *
from pandas import DataFrame

def graph(data):
    """ Method to display all graphs """

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

def graph2(data3):
    """ Change over time. """

    # Converting data
    dat3 = DataFrame(data3, columns = ['A', 'B'])

    # Creating graph then assigning to g3
    g3 = ggplot(dat3, aes(x='A', y='B')) + geom_line()

    # Return graph
    return g3

def graph2(data):
    """ Distribution of scores for a given review"""

# Testing out simple graph
data3 = [[1,1],[2,4],[3,9],[4,16],[5,25],[6,36],[7,49],[8,64],[9,81],[10,100]]
print(exampleGraph(data1))
