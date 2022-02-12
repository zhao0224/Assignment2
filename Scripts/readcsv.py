import csv
import pandas as pd


class Data_Read_Csv:
    '''
        Data_Read_C is created for data read from csv file
    '''

    def __init__(self, path):
        '''
        This is the constructor of Data_Read_Csv. If the class has been called, it must pass the file path as an argument.
        :param path: this is use to put csc path
        '''
        self.data = path


    def read(self):
        '''
        This read method is called pandas reac_csv method to read file.
        The result has been assigned to the variable named data_record
        :return: data_record
        '''
        data_record = pd.read_csv(self.data, header=None, encoding='windows-1252')
        return data_record





