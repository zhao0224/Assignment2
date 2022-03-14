# Import panadas which can read url link
import pandas as pd
# Import other class
from readcsv import Data_Read_Csv as db
from model import Model
import timeprint
import time
import logging
from view import View

"""
 CST8333 Section 350
 Student Name: Jing Zhao
 Student ID: 040994750
 Assignment #2
 version 1.3
"""
logger = logging.getLogger(__name__)


class Controller:
    """
    Author: Jing Zhao
    This controller class contain a list which will store all function return
    header is used to store the column names
    temp_table is used to store the list temprary in memory.
    """

    list = []
    header = []
    temp_table = []

    def __init__(self):
        self.view = View(self)

    def read_all(self):
        """
        Author: Jing Zhao
        This read_all function is used to read csv file 101 rows, the first row index 0 is the colunm names in csv file.
        :return: There is no return for this function.
        """

        try:
            # set csv path to a variable data_path
            # csv_file = 'https://www.cer-rec.gc.ca/open/incident/pipeline-incidents-comprehensive-data.csv'
            csv_file = "C:/Users/Admin/Desktop/pipeline-incidents-comprehensive-data.csv"
            # call Data_Read_Csv class in read-csv.py and display tail 10 lines, use variable data_pipeline as
            # reference in future use
            data_pipeline = db(csv_file).read().head(101)

            # loop over the csv data table, create a list table_row for store each row from the csv file
            # Pandas' dataframe to read data like excel, which use column name as index, row as line id
            # eg table[1][1]-->[1] reflect excel Column A, row is line 1

            for i in range(len(data_pipeline[0])):
                row_content = (Model(data_pipeline[0][i], data_pipeline[1][i], data_pipeline[2][i], data_pipeline[3][i],
                                     data_pipeline[4][i], data_pipeline[5][i], data_pipeline[10][i],
                                     data_pipeline[12][i],
                                     data_pipeline[17][i]))

                self.list.append(row_content)
            self.header.append(self.list[0])
        except IOError:
            logger.error("CSV file read error")

    def show_rows(self, displayRows):
        """
        Author: Jing Zhao
        This show_rows function is passing rows number from user request and then return the dataset of these rows
        :param displayRows: this is a list for how many rows user request to display in future
        :return: temp_table. This temp-table stores all list for rows required to be displayed
        """
        for num in displayRows:
            self.temp_table.append(self.list[num])
        return self.temp_table

    def write_file(self):
        """
        Author: Jing Zhao
        This write_file function allow user write the list to a new file named newFile.csv
        :return: There is no return.
        """
        dataFrame = []
        for obj in self.list:
            dataFrame.append(obj.toList())
        newFile = pd.DataFrame(dataFrame)
        newFile.to_csv('newFile.csv')

    def add_record(self, input_string):
        """
        Author: Jing Zhao
        The add_record function allows the user to add additional records to the database. After the user enters a string,
        it will be converted to an object by using the constructor in the model data structure.
        :param input_string: accept from user input
        :return: no return
        """

        newContent = input_string.split(",")
        newRecord = Model(newContent[0], newContent[1], newContent[2], newContent[3],
                          newContent[4], newContent[5], newContent[6], newContent[7], newContent[8])

        self.list.append(newRecord)

    def update_record(self, rowNum, input_string):
        """
        Author: Jing Zhao
        This update_record function is accepting two parameters, one is row number,
        another one is the new record for replacing the old record
        :param rowNum: is the primary key for table
        :param input_string: is the record that user want to update
        :return: self.list which is the list inlcudes new record
        """

        newContent = input_string.split(",")
        newRecord = Model(newContent[0], newContent[1], newContent[2], newContent[3], newContent[4], newContent[5],
                          newContent[6], newContent[7], newContent[8])
        self.list.remove(self.list[rowNum])
        self.list.insert(rowNum, newRecord)

    def delete_record(self, rowNum):
        """
        Author: Jing Zhao
        This delete_record function is accepting primary key and remove whole line
        :param rowNum: get from user input and indicate which row(primary key) want to delete
        :return: self.list which is the list updated record
        """
        self.list.remove(self.list[rowNum])

    def exit_system(self):
        """
        Author: Jing Zhao
        This exit_system function is let user exit the whole project
        """
        exit()

    def display(self):
        """
        Author: Jing Zhao
        This display function is used to print each line of the list
        :return: result no return, directly display only
        """
        for row in self.list:
            print(row.toString())

    def displayTempTable(self):
        """
        Author: Jing Zhao
        This display TempTable is used to print each line of the temp_table
        :return: result no return, directly display only
        """
        for row in self.temp_table:
            print(row.toString())

    def show_header(self):
        """
        Author: Jing Zhao
        This show_header is used to display header only when it has been called
        :return: header list
        """
        for name in self.header:
            return name.toList()

    def main(self):
        """
        Author: Jing Zhao
        Controller main method to run whole project
        """
        while True:
            print("Program by Jing Zhao 040994750")
            self.view.showMenu()
            self.view.optionNum()
            time.sleep(2)



