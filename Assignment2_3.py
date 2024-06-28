
def Factorial(No):
    Sum = 1
    for i in range(No,1,-1):
        Sum = Sum * i
    return Sum
       
        

def main():
    print("Enter the Number : ")
    Value = int(input())

    Ans = Factorial(Value)

    print("Factorial is : ",Ans)

if __name__ == "__main__":
    main()