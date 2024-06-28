from MarvellousNum import *
    

def main():
    print("Enter the Number of Elemments : ")
    Size = int(input())
    ListPrime = []

    for i in range(Size):
        no = int(input())
        ListPrime.append(no)

    FList = list(filter(ChkPrime,ListPrime))
    print("Prime Numbers are : ",FList)

    RList = reduce(AddPrime,FList)
    print("Addition of Prime Numbers is : ",RList)

if __name__ == "__main__":
    main()