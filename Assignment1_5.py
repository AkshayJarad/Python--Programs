
def Reverse(No):
    for i in range(No,0,-1):
        print(i, end = " ")

def main():
    print("Enter the Number : ")
    Value = int(input())

    Reverse(Value)

if __name__ == "__main__":
    main()