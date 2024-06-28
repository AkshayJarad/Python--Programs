
def Display(No):
    for i in range(1,No+1,1):
        print("")
        for j in range(1,i+1):
            print(j, end = "   ")

def main():
    print("Enter the Number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()