
import datetime
import time
import schedule

def Schedule_Minute():
    print("Schedular executes after each minute : ",datetime.datetime.now())

def Schedule_Hour():
    print("Schedular executes after each hour : ",datetime.datetime.now())

def Schedule_Sunday():
    print("Schedular executes after each Sunday : ",datetime.datetime.now())

def Schedule_Second():
    print("Schedular executes after each Second : ",datetime.datetime.now())

def main():
    print("Current Time is : ",datetime.datetime.now())

    schedule.every(1).minutes.do(Schedule_Minute)
    schedule.every(1).hour.do(Schedule_Hour)
    schedule.every(1).sunday.do(Schedule_Sunday)
    schedule.every(1).second.do(Schedule_Second)

    while True:
        schedule.run_pending()
        time.sleep(1)   

if __name__ == "__main__":
    main()