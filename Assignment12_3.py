import psutil
import os

def DisplayProcesses():
    
    print("List of Running Processes are : ")

    print("---------------------------------------------------------------")

    for proc in psutil.process_iter(['pid','name','username']):
        print(proc.info)

    print("----------------------------------------------------------------")

def main():
    DisplayProcesses()

if __name__ =="__main__":
    main()