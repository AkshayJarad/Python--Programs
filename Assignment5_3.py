
def DisplayReverse(No):
    
    if(No >= 1):
        print(No, end = "     ")
        No = No - 1
        DisplayReverse(No)


def main():
    print("Enter the Number : ")
    Value = int(input())

    DisplayReverse(Value)

if __name__ == "__main__":
    main()