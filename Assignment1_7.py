

def Display(No):
    if(No % 5 == 0):
        return True
    else:
        return False


def main():
    print("Enter the Number : ")
    Value = int(input())

    Result = Display(Value)

    if(Result == True):
        print("Divisible by 5")
    else:
        print("Not Divisible by 5")

if __name__ == "__main__":
    main()