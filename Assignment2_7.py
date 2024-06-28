
def Display(No):
    for i in range(1,No+1,1):
        print("")
        for i in range(1,No+1,1):
            print(i,end = "   ")

def main():
    print("Enter the Number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()