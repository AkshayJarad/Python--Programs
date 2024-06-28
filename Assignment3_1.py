from functools import reduce

def Add(A,B):
    Ans = A + B
    return Ans

def main():
    print("Enter the number of Elements : ")
    Size = int(input())
    Arr = []

    print("Enter the Elements : ")
    for i in range(0,Size):
        no = int(input())
        Arr.append(no)
    print("Elements are : ",Arr)

    Result = reduce(Add,Arr)

    print("Addition is : ",Result)

if __name__  == "__main__":
    main()
