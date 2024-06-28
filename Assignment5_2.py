i = 1

def DisplayDigits(No):
    global i
    if(i <= No):
        print(i, end = "     ")
        i = i + 1
        DisplayDigits(No)


def main():
    print("Enter the Number : ")
    Value = int(input())

    DisplayDigits(Value)

if __name__ == "__main__":
    main()