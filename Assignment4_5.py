from functools import reduce


def Prime(No):
    for i in range(2,No):
        if(No % i == 0):
            return False
    return No
    
def Multiply(No):
    Ans = 0
    Ans = No * 2
    return Ans

def Maximum(A,B):
    if(A > B):
        return A
    else:
        return B



def main():
    print("Enter the Number of Elements : ")
    Size = int(input())
    Arr = []

    print("Enter the Elements : ")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    print("Input List is : ",Arr)

    FList = list(filter(Prime,Arr))
    print("Filtered List is : ",FList)

    MList = list(map(Multiply,FList))
    print("Maped List is : ",MList)

    RList = reduce(Maximum,MList)
    print("Maximum Number from the List is : ",RList)


if __name__ == "__main__":
    main()