import controller
import unittest
import model

class TestFunction(unittest.TestCase):
    '''
    This is the test class that using unit test method to test add record function, and delete record function in controller
    '''
    con = controller.Controller()
    con.read_all()


    def test_add_record(self):
        '''
        This test_add_record function is test add_record function in controller.
        parse the string str to add_record, then according to add_record, it will call model's data structrue to convert string to
        an object, then add to the list. If add successfull, the length of list will add 1 and the str can't direct equal to the last
        line as added because it converted to object. But it could convert the last line object to string by call toString method,
        then we can test two strings are euqal or not.
        :return:

        '''
        str = "INC2220-087,Release of Substance,09/02/2009,Zama Lake,Ontario,NOVA Gas Transmission Ltd.,Natural Gas - Sweet,No,Corrosion and Cracking"
        lenBeforeAdd=len(self.con.list)
        self.con.add_record(str)
        self.assertEqual(len(self.con.list),lenBeforeAdd+1)
        self.assertEqual(self.con.list[len(self.con.list)-1].toString(),str)


    # def test_delete_record(self):
    #     '''
    #
    #     :return:
    #     '''
    #     lenBeforeDelete= len(self.con.list)
    #     self.con.delete_record(89)
    #     self.con.delete_record(79)
    #     self.assertEqual(len(self.con.list), (lenBeforeDelete-2))


unittest.main