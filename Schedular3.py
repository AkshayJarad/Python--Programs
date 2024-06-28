
import datetime
import time
import schedule

def Schedule_Minute():
    print("Schedular executes after each minute : ",datetime.datetime.now())

def main():
    print("Cuurent Time is : ",datetime.datetime.now())

    schedule.every(1).minutes.do(Schedule_Minute)
    

if __name__ == "__main__":
    main()