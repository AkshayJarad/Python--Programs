
def CheckNum(No):
    if(No > 0):
        print("Positive Number")
    elif(No < 0):
        print("Negative Number")
    else:
        print("Zero")

def main():
    print("Enter the Number : ")
    Value = int(input())

    CheckNum(Value)

if __name__ == "__main__":
    main()