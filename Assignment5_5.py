
iFact = 1

def Factorial(No):
    global iFact

    if(No >= 1):
       iFact = iFact * No
       No = No - 1
       Factorial(No)
    return iFact
   



def main():
    print("Enter the Number : ")
    Value = int(input())

    Result = Factorial(Value)

    print("Factorial is : ",Result)

if __name__ == "__main__":
    main()