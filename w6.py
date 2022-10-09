import os
os.system("cls")
##########################################################
'''
#kaptiel fem i python mapen för tidshantering
from datetime import datetime, timedelta #means from the module "datetime" import the class "datetime" and class timedelta

now = datetime.now() #collect the current time

print(now) #prints call opon now which shows the current time

##########################################################
'''
from datetime import datetime, timedelta
import time


# while True:
#     now = datetime.now()
#     if now.hour < 7 or now.hour < 16:
#         print("work hours")
#         time.sleep(2)
#     else: 
#         print("sleepy time")
#         time.sleep(2)


def getWeekName(weekday:int) -> str:
    
    if weekday == 0:
        return "Monday"
    elif weekday == 1:
        return "Tuseday"
    elif weekday == 2:
        return "Wednestday"
    elif weekday == 3:
        return "Thursday"
    elif weekday == 4:
        return "Friday"
    elif weekday == 5:
        return "Saturday"
    elif weekday == 6:
        return "Sunday"
    return "Unvaild date"
    


while True:
    year, month, day = map(int, input("enter date of birth YYYY/MM/DD: ").split("/")) #use multiple input in one line wiht the sparetor /
    now = datetime(year,month,day) #use the module datetime date to calculate the weekday 0 to 6
    weekday = getWeekName(now.weekday()) #uses the function getweekname inorder to solve nameweekday 0: monday - 6: sunday
    print(f"The day you were born was {weekday}")
    re =input("press any Enter butten to restart: ")
    os.system("cls")


