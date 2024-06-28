
def Display(No):
    for i in range(2,No+1,2):
        print(i, end = "   ")

def main():
    print("Enter the Number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()