
def SumDigits(No):
    iDigit = 0

    while(No != 0):
        iDigit = iDigit + (No % 10)
        No = No // 10
        
    return iDigit
    

def main():
    print("Enter the Number : ")
    Value = int(input())

    Ans = SumDigits(Value)

    print("Number of Digits are : ",Ans)
 

if __name__ == "__main__":
    main()