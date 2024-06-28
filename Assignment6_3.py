import threading

def EvenList(No):
    Ans = 0
    for i in No:
        if(i % 2 == 0):
            Ans = Ans + i
    print("Addition of Even Elements from list is : ",Ans)

def OddList(No):
    Ans = 0
    for i in No:
        if(i % 2 != 0):
            Ans = Ans + i
    print("Addition of Odd Elements from list is : ",Ans)

def main():
    Arr = [1,2,3,4,5,6,7,8,9,10]

    T1 = threading.Thread(target = EvenList, args = (Arr,))
    T2 = threading.Thread(target = OddList, args = (Arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()