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

def graph2(data):
    """ Change over time. """

# Testing out simple graph
data1 = [[1,1],[2,4],[3,9],[4,16],[5,25],[6,36],[7,49],[8,64],[9,81],[10,100]]
print(exampleGraph(data1))
