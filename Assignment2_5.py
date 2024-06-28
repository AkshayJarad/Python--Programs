
def CheckPrime(No):
    if(No < 0):
        No = -No

    for iCnt in range(2,No-1,1):
        if(No % iCnt == 0):
            return False
    return True



def main():
    print("Enter the Number : ")
    Value = int(input())
    
    Ans = CheckPrime(Value)

    if(Ans == True):
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

if __name__ == "__main__":
    main()