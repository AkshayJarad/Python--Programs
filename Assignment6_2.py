import threading

def EvenFactor(No):
    Ans = 0
    for i in range(1,No+1):
        if(No % i == 0):
            if(i % 2 == 0):
                Ans = Ans + i
    print("Addition of Even Factors is : ",Ans)

def OddFactor(No):
    Ans = 0
    for i in range(1,No+1):
        if(No % i == 0):
            if(i % 2 != 0):
                Ans = Ans + i
    print("Addition of Odd Factors is : ",Ans)
                
def main():
    print("Enter the Number : ")
    Value = int(input())

    T1 = threading.Thread(target = EvenFactor, args = (Value,))
    T2 = threading.Thread(target = OddFactor, args = (Value,))

    T1.start()
    T1.join()

    T2.start()
    T2.join()

    print("Exit From main")

if __name__ == "__main__":
    main()