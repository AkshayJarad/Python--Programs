
def CheckNum(No):
    if(No % 2 == 0):
        print("Number is Even")
    else:
        print('Number is Odd')

def main():
    print("Enter the number : ")
    Value = int(input())

    CheckNum(Value)

if __name__ == "__main__":
    main()