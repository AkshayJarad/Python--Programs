
def Frequency(Arr,Freq):
    return Arr.count(Freq)

def main():
    print("Enter the number of Elements : ")
    size = int(input())
    Arr = []

    print("Enter the Elements : ")
    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Enter the Number for Frequency Calculation : ")
    Freq = int(input())

    ret = Frequency(Arr,Freq)

    print("Frequency is : ",ret)


if __name__ == "__main__":
    main()