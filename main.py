from datetime import date , time , datetime
today = date.today()
now = datetime.now()
print("today's date is", today)
print("\current date and time is", now)
print("\ndate components",today.year, today.month, today.day)
import random
import time
def getRandomDate( startDate, endDate):
    print("print random  date between", startDate, "and", endDate)
    randomGenerator = random.random()
    dateformat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startDate, dateformat))
    endTime = time.mktime(time.strptime(startDate,dateformat))
    randomTime = startTime +  randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateformat,time.localtime(randomTime))
    return randomDate
print("random date =", getRandomDate("2/3/2017","1/6/2024"))