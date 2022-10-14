import os
from time import time
from webbrowser import get
os.system("cls")
##########################################################
'''
#kaptiel fem i python mapen för tidshantering
from datetime import datetime, timedelta #means from the module "datetime" import the class "datetime" and class timedelta

now = datetime.now() #collect the current time

print(now) #prints call opon now which shows the current time

##########################################################

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
##########################################################

from datetime import datetime, timedelta
import time


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
    birthday = datetime(year,month,day) #use the module datetime date to calculate the weekday 0 to 6
    weekday = getWeekName(birthday.weekday()) #uses the function getweekname inorder to solve nameweekday 0: monday - 6: sunday
    now = datetime.now()
    diff = (now - birthday)
    print(f"The day you were born was {weekday} and you are now {diff.days} old")
    re =input("press any Enter butten to restart: ")
    os.system("cls")

##########################################################

#calculate till sommaren vectaion
from datetime import datetime, timedelta
vecation = datetime(2023,6,25)
now = datetime.now()
diff = vecation - now

print(diff.days)

##########################################################

#calculate facktura due date
from datetime import datetime, timedelta

dateOfBil = datetime.now()

billdeadLine = dateOfBil + timedelta(days=30)
if billdeadLine.weekday() == 5: #if saturday it dateofbil of date is sen on friday
    billdeadLine -= timedelta(days=-1)

elif billdeadLine.weekday() == 6: #if sunday it dateofbil of date is sen on monday
    billdeadLine += timedelta(days=1)

convertBilDeadLine = billdeadLine.strftime("%Y-%m-%d") #gives the year, month, day
print(f"Duedate for invoice: {convertBilDeadLine}")

##########################################################
# Count olympic Years
from datetime import datetime

def getAllOlymicYears(start:int)-> int:
    now = datetime.now().year
    years = []
    for olympic in range(start,now+1,4):
        years.append(olympic)
    return years

startyear = int(input("Enter the year you want to start count: "))
years = getAllOlymicYears(startyear)

for year in years:
    print(f"The olympic: {year}")

##########################################################

from datetime import datetime

def getAllOlymicYears(start:int)-> int: #Type hinting
    now = datetime.now().year
    years = []
    for olympic in range(start,now+1,4):
        years.append(olympic)
    return years

startyear = int(input("Enter the year you want to start count: "))
years = getAllOlymicYears(startyear)

for year in years:
    print(f"The olympic: {year}")

##########################################################
'''

class Robot:
    def __init__(self, Name,  Color, Weight): #constructor 
        self.name = Name
        self.color = Color
        self.weight = Weight

    def introduce_self(self):
        print(f"My name is {self.name}")

# r1 = Robot()
# r1.name = "tom"
# r1.color = "red"
# r1.weight = 30

# r2 = Robot()
# r2.name = "jerry"
# r2.color = "blue"
# r2.weight = 18 

r1 = Robot ("tom","red",30)
r2 = Robot ("jerry","blue",18)
r1.introduce_self()
r2.introduce_self()



