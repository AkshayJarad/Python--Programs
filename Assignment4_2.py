
Multiplication = lambda No1,No2 : No1 * No2

def main():
    print("Enter the First Number : ")
    Value1 = int(input())

    print("Enter the Second Number : ")
    Value2 = int(input())

    Result = Multiplication(Value1,Value2)
    print("Multiplication is : ",Result)

if __name__ == "__main__":
    main()