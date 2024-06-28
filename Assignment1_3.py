
def Add(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("Enter the First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    Result = Add(Value1,Value2)

    print("Addition is : ",Result)

if __name__ == "__main__":
    main()