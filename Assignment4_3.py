from functools import reduce


Range = lambda No : (70 <= No <= 90)
    
Increase = lambda No : No + 10

Product = lambda A,B : A * B



def main():
    print("Enter the Number of Elements : ")
    Size = int(input())
    Arr = []

    print("Enter the Elements : ")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    print("Input List is : ",Arr)

    FList = list(filter(Range,Arr))
    print("Filtered List is : ",FList)

    MList = list(map(Increase,FList))
    print("Maped List is : ",MList)

    RList = reduce(Product,MList)
    print("Product of all the Numbers is : ",RList)


if __name__ == "__main__":
    main()