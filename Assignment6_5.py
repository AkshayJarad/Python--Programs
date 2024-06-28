import threading

def Thread1(No):
    print("In straight order : ")
    for i in range(1,No+1):
        print(i)

def Thread2(No):
    print("In reverse order : ")
    for i in range(No,0,-1):
        print(i)


def main():
    Value = 10

    T1 = threading.Thread(target = Thread1, args = (Value,))
    T2 = threading.Thread(target = Thread2, args = (Value,))

    T1.start()
    T1.join()

    T2.start()
    T2.join()


if __name__ == "__main__":
    main()