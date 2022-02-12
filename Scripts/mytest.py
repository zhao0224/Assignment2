import controller
import unittest
import model

class TestFunction(unittest.TestCase):
    con = controller.Controller()
    con.read_all()


    def test_add_record(self):
        str = "INC2220-087,Release of Substance,09/02/2009,Zama Lake,Ontario,NOVA Gas Transmission Ltd.,Natural Gas - Sweet,No,Corrosion and Cracking"
        # con=controller.Controller()
        # con.read_all()
        lenBeforeAdd=len(self.con.list)
        self.con.add_record(str)
        self.assertEqual(len(self.con.list),lenBeforeAdd+1)
        self.assertEqual(self.con.list[len(self.con.list)-1].toString(),str)


    def test_delete_record(self):
        lenBeforeDelete= len(self.con.list)
        self.con.delete_record(100)
        self.assertEqual(len(self.con.list), lenBeforeDelete-1)


unittest.main