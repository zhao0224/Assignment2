import unittest
import controller
import model

'''
CST8333 Section 350
Student Name: Jing Zhao
Student ID: 040994750
Assignment #2
version 1.2
'''


class MyTestCase(unittest.TestCase):
    """
    Author: Jing Zhao This is the test class that using unit test method to test add record function, and delete
    record function in controller
    """
    con = controller.Controller()
    con.read_all()

    def test_add_record(self):
        """
        Author: Jing Zhao This test_add_record function is test add_record function in controller. parse the string
        str to add_record, then according to add_record, it will call model's data structrue to convert string to an
        object, then add to the list. If add successfull, the length of list will add 1 and the str can't direct
        equal to the last line as added because it converted to object. But it could convert the last line object to
        string by call toString method, then we can test two strings are euqal or not. :return: fail or pass

        """
        str = "INC2220-087,Release of Substance,09/02/2009,Zama Lake,Ontario,NOVA Gas Transmission Ltd.,Natural Gas - " \
              "Sweet,No,Corrosion and Cracking "
        lenBeforeAdd = len(self.con.list)
        self.con.add_record(str)
        self.assertEqual(len(self.con.list), lenBeforeAdd + 1)
        self.assertEqual(self.con.list[len(self.con.list) - 1].toString(), str)


if __name__ == '__main__':
    unittest.main()
