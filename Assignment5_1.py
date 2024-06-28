i = 1

def Display(No):
    global i
    if(i <= No):
        print("*", end = "     ")
        i = i + 1
        Display(No)


def main():
    print("Enter the Number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()