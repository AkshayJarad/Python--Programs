
def CountDigit(No):
    iDigit = 0
    iCount = 0

    while(No != 0):
        iDigit = No % 10
        No = No // 10
        iCount = iCount + 1
        
    return iCount
    

def main():
    print("Enter the Number : ")
    Value = int(input())

    Ans = CountDigit(Value)

    print("Number of Digits are : ",Ans)
 

if __name__ == "__main__":
    main()