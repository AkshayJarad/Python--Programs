
def AddFactors(No):
    Sum = 0
    for iCnt in range(1,No,1):
        if(No % iCnt == 0):
            Sum = Sum + iCnt
    return Sum
        

def main():
    print("Enter the Number : ")
    Value = int(input())

    Ans = AddFactors(Value)

    print("Addition of Factors is : ",Ans)

if __name__ == "__main__":
    main()