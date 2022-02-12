from view import View
import controller
import timeprint
import time

'''
This is main class to start this program. 
It calls view.showMenu method. Then it calls view's optionNum method to let user input their option.
It allow sleep 6 seconds to loop.
'''
listView = View()
while True:
    print("Program by Jing Zhao 040994750")
    listView.showMenu()
    listView.optionNum()
    time.sleep(6)

