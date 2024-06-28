from functools import reduce

def Maximum(A,B):
    if(A > B):
        return A
    else:
        return B
    

def main():
    print("Enter the number of Elements : ")
    Size = int(input())
    Arr = []

    print("Enter the Elements : ")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    print("Elements of the List are : ",Arr)

    Result = reduce(Maximum,Arr)

    print("Maximum number is : ",Result)

if __name__ == "__main__":
    main()