# display menu options for the users to view
import time
import logging

# from controller import Controller

'''
CST8333 Section 350
Student Name: Jing Zhao
Student ID: 040994750
Assignment #2
version 1.3
'''

logger = logging.getLogger(__name__)


class View:

    def __init__(self, controller):
        """
        Author: Jing Zhao
        This constructor is used to call methods in controller.
        """
        self.controller = controller

    @staticmethod
    def showMenu():
        """
        Author: Jing Zhao
        This is the menu after running project give user option to choice
        :return: no return
        """
        print()
        print("--------------------- MENU ---------------------")
        print("1. reload the data from the csv file")
        print("2. display first 100 records from csv file")
        print("3. write a new file")
        print("4. display one record or multiple records")
        print("5. add a new record")
        print("6. edit an existing record")
        print("7. delete an existing record")
        print("0. exit")

    def optionNum(self):
        """
        Author: Jing Zhao
        The optionNum function is an iterative method of communicating with the user.
        :return: no return
        """
        try:
            print("enter your choice: ")
            try:
                option = int(input(""))
                if option == 1:
                    print("reload the data from the csv file")
                    self.controller.read_all()
                elif option == 2:
                    print("display first 100 records from csv file")
                    self.controller.display()
                elif option == 3:
                    print("write a new file")
                    self.controller.write_file()
                elif option == 4:
                    print("display one record or multiple records")
                    print("How many rows you want to display?")
                    numDisplay = int(input(""))
                    if numDisplay == 0:
                        print(self.controller.show_header())
                    else:
                        displayRows = []
                        print("enter rows you want to display")
                        i = 0
                        while i < numDisplay:
                            displayRows.append(int(input()))
                            i += 1
                        self.controller.show_rows(displayRows)
                        print(len(displayRows))
                        self.controller.displayTempTable()
                elif option == 5:
                    print("add a new record")
                    str = "input the data you want to insert separator by comma"
                    print(str)
                    try:
                        input_string = input(" ")
                        self.controller.add_record(input_string)
                        self.controller.display()
                    except ValueError:
                        logger.error("string must have 9 contents")
                elif option == 6:
                    print("edit an existing record")
                    try:
                        print("enter the row you want to change")
                        rowNum = int(input(""))
                        print(self.controller.list[rowNum].toString())
                        print("input the data you want to insert seperator by comma")
                        input_string = input("")
                        self.controller.update_record(rowNum, input_string)
                        self.controller.display()
                    except ValueError as e:
                        logger.error("Must have 9 contents! Try it again")
                elif option == 7:
                    print("delete an existing record")
                    try:
                        print("length of table before delete:", len(self.controller.header))
                        self.controller.display()
                        print("enter the row you want to delete")
                        rowNum = int(input(""))
                        print(self.controller.list[rowNum].toString())
                        time.sleep(4)
                        self.controller.delete_record(rowNum)
                        self.controller.display()
                    except Exception:
                        logger.error("out of range list! Try it again")
                elif option == 0:
                    print("Thank you Bye")
                    self.controller.exit_system()
                else:
                    logger.error("out of range input please wait few seconds and reenter again")
            except ValueError:
                logger.error("Not a proper integer! Try it again")
        except Exception:
            logger.error("Must have 9 contents! Try it again")
