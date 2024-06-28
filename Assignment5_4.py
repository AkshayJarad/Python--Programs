i = 0
iDigit = 0
iSum = 0

def SumDigits(No):
    global i
    global iDigit
    global iSum
    if(i <= No):
        iDigit = No % 10
        No = No // 10
        i = i + 1
        iSum = iSum + iDigit
        SumDigits(No)
    return iSum


def main():
    print("Enter the Number : ")
    Value = int(input())

    Result = SumDigits(Value)

    print("Summation is : ",Result)

if __name__ == "__main__":
    main()