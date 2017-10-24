import sys
import logging
from spreadsheet import read_from_spreadsheet
from spreadsheet import create_csv

if __name__ == "__main__":
    print("Welcome to Edurate")
    print("https://github.com/Edurate/edurate")

    spreadsheet_list = read_from_spreadsheet()
    create_csv(spreadsheet_list)
