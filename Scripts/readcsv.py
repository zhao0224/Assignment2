import csv
import pandas as pd

'''
CST8333 Section 350
Student Name: Jing Zhao
Student ID: 040994750
Assignment #2
version 1.3
'''


class Data_Read_Csv:
    """
    Author: Jing Zhao
    Data_Read_C is created for data read from csv file
    """

    def __init__(self, path):
        """
        Author: Jing Zhao
        This is the constructor of Data_Read_Csv. If the class has been called, it must pass the file path as an argument.
        :param path: this is use to put csc path
        """
        self.data = path

    def read(self):
        """
        Author: Jing Zhao
        This read method is called pandas read_csv method to read file.
        The result has been assigned to the variable named data_record
        :return: data_record
        """
        data_record = pd.read_csv(self.data, header=None, encoding='windows-1252')
        return data_record
