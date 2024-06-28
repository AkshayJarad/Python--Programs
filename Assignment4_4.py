from functools import reduce


Even = lambda No : (No % 2 == 0)
    
Square = lambda No : No * No

Add = lambda A,B : A + B



def main():
    print("Enter the Number of Elements : ")
    Size = int(input())
    Arr = []

    print("Enter the Elements : ")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    print("Input List is : ",Arr)

    FList = list(filter(Even,Arr))
    print("Filtered List is : ",FList)

    MList = list(map(Square,FList))
    print("Maped List is : ",MList)

    RList = reduce(Add,MList)
    print("Addition of all the Numbers is : ",RList)


if __name__ == "__main__":
    main()