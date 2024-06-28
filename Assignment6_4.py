import threading
import os

def CountSmall(str):
    iCnt = 0
    print("PID is : ",os.getpid())
    for i in str:
        if(i.islower()):
            iCnt = iCnt + 1
    print("Addition of Small characters from string is : ",iCnt)

def CountCapital(str):
    iCnt = 0
    print("PID is : ",os.getpid())
    for i in str:
        if(i.isupper()):
            iCnt = iCnt + 1
    print("Addition of Capital characters fromm the string is : ",iCnt)

def CountDigits(str):
    iCnt = 0
    print("PID is : ",os.getpid())
    for i in str:
        if(i.isdigit()):
            iCnt = iCnt + 1
    print("Addition of Digits from the string is : ",iCnt)

def main():
    print("Enter the String : ")
    str = input()

    T1 = threading.Thread(target = CountSmall, args = (str,))
    T2 = threading.Thread(target = CountCapital, args = (str,))
    T3 = threading.Thread(target = CountDigits, args = (str,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()