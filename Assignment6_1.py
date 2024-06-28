import threading

def EvenDisplay(No):
    print("Even Elements are : ")
    x = 0
    for i in range(No):
        print(i)
        x = x + 2

def OddDisplay(No):
    print("Odd Elements are : ")
    x = 1
    for i in range(No):
        print(i)
        x = x + 2    

def main():
    print("Enter the Number : ")
    Value = int(input())

    T1 = threading.Thread(target = EvenDisplay, args = (Value,))
    T2 = threading.Thread(target = OddDisplay, args = (Value,))

    T1.start()
    T1.join()

    T2.start()
    T2.join()


if __name__ == "__main__":
    main()