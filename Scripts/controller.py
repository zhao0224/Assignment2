# Import panadas which can read url link
import pandas as pd
# Import other class
from readcsv import Data_Read_Csv as db
from model import Model
import timeprint
import time



def instuction():
    '''
     CST8333 Section 350
     Student Name: Jing Zhao
     Student ID: 040994750
     Assignment #2
     version 1.2
    '''
class Controller:
    '''
    This controller class contain a list which will store all function return
    header is used to store the column names
    temp_table is used to store the list temprary in memory.
    '''
    list = []
    header = []
    temp_table = []


    def read_all(self):
        '''
         This read_all function is used to read csv file 101 rows, the first row index 0 is the colunm names in csv file.
        :return: There is no return for this function.
        '''

        try:
            #set csv path to a variable data_path
            # csv_file = 'https://www.cer-rec.gc.ca/open/incident/pipeline-incidents-comprehensive-data.csv'
            csv_file ='C:/Users\Admin\Desktop\pipeline-incidents-comprehensive-data.csv'
            #call Data_Read_Csv class in readcsv.py and display tail 10 lines, use variable data_pipeline as refernce in future use
            data_pipeline = db(csv_file).read().head(101)

            # loop over the csv data table, create a list table_row for store each row from the csv file
            # Pandas' dataframe to read data like excel, which use column name as index, row as line id
            # eg table[1][1]-->[1] reflect excel Column A, row is line 1

            for i in range(len(data_pipeline[0])):
                row_content = (Model(data_pipeline[0][i], data_pipeline[1][i], data_pipeline[2][i], data_pipeline[3][i],
                                     data_pipeline[4][i], data_pipeline[5][i], data_pipeline[10][i], data_pipeline[12][i],
                                     data_pipeline[17][i]))

                self.list.append(row_content)
            self.header.append(self.list[0])
        except:
            print("CSV file read error")


    def show_rows(self, displayRows):
        '''
        This show_rows function is passing rows number from user request and then return the dataset of these rows
        :param displayRows: this is a list for how many rows user request to display in future
        :return: temp_table. This temp-table stores all list for rows required to be displayed
        '''
        try:
            for num in displayRows:
                self.temp_table.append(self.list[num])
            return self.temp_table
        except:
            print("Error happen, please make sure input integer")


    def write_file(self):
        '''
        This write_file function allow user write the list to a new file named newFile.csv
        :return: There is no return.
        '''
        dataFrame=[]
        for obj in self.list:
            dataFrame.append(obj.toList())
        newFile = pd.DataFrame(dataFrame)
        newFile.to_csv('newFile.csv')


    def add_record(self, input_string):
        '''
        The add_record function allows the user to add additional records to the database. After the user enters a string,
        it will be converted to an object by using the constructor in the model data structure.
        :param input_string: accept from user input
        :return: no return
        '''
        try:
            newContent = input_string.split(",")
            newRecord = Model(newContent[0], newContent[1], newContent[2], newContent[3], \
                          newContent[4], newContent[5], newContent[6], newContent[7], newContent[8])
        except:
            print("must have 9 contents")
        self.list.append(newRecord)


    def update_record(self, rowNum, input_string):
        '''
        This update_record function is accepting two parameters, one is row number,
        another one is the new record for replacing the old record
        :param rowNum: is the primary key for table
        :param input_string: is the record that user want to update
        :return: the whole updated list
        '''
        try:
            newContent = input_string.split(",")
            newRecord = Model(newContent[0], newContent[1], newContent[2], newContent[3], \
                              newContent[4], newContent[5], newContent[6], newContent[7], newContent[8])
            self.list.remove(self.list[rowNum])
            self.list.insert(rowNum, newRecord)
        except:
            print("must have 9 contents")
        return self.list


    def delete_record(self, rowNum):
        '''
        This delete_record function is accepting primary key and remove whole line
        :param rowNum: get from user input and indicate to
        :return:
        '''
        try:
            self.list.remove(self.list[rowNum])
        except:
            print("Something wrong. Table has ", len(self.list), "rows only, out of range error")

        return self.list


    def display(self):
        '''

        :return:
        '''
        for row in self.list:
            print(row.toString())


    def displayTempTable(self):
        '''

        :return:
        '''
        for row in self.temp_table:
            print(row.toString())


    def option(self):
        '''

        :return:
        '''
        self.view.optionNum()


    def show_header(self):
        '''

        :return:
        '''
        for name in self.header:
           return name.toList()


