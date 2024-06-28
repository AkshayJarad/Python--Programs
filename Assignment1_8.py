
def Display(No):
    for i in range(No):
        print("*", end = "         ")

def main():
    print("Enter the Number of times you want to print * on Screen : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()